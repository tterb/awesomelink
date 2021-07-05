import json
from django.core.exceptions import FieldError
from django.db.models import Q
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from ratelimit.decorators import ratelimit
from rest_framework.decorators import api_view

from .constants import (
    AWESOMELINK_DNE_ERROR,
    AWESOMELINK_UNAPPROVED_ERROR,
    AWESOMLINK_ORDER_BY,
    INVALID_PARAM_ERROR,
)
from .forms import (
    AwesomeLinkForm,
    FlagForm,
    RatingForm,
)
from .helpers import get_random_link
from .models import AwesomeLink
from .serializers import (
    AwesomeLinkSerializer,
    AwesomeLinkListSerializer,
)


@api_view(['GET'])
def awesomelink_list(request):
    """
    Retrieve an list of all AwesomeLinks
    """
    serializer = AwesomeLinkListSerializer()
    queryset = AwesomeLink.objects.filter(is_approved=True)
    data = dict()
    data['count'] = queryset.count()
    data['links'] = json.loads(serializer.serialize(queryset))
    return JsonResponse(data)

@api_view(['GET'])
def awesomelink_count(request):
    """
    Get the total number of AwesomeLinks
    """
    return JsonResponse({
        'count': AwesomeLink.objects.filter(is_approved=True).count(),
    })

@api_view(['GET'])
def awesomelink_pending(request):
    """
    Retrieve a list of pending AwesomeLinks
    """
    if request.user and request.user.is_superuser:
        awesomelinks = list(AwesomeLink.objects.filter(is_approved=False).order_by('created'))
        context = { 'awesomelinks': awesomelinks }
        return render(request, 'links/pending.html', context)
    return HttpResponse('401 Unauthorized', status=401)


@api_view(['GET'])
def awesomelink_detail(request, pk):
    """
    Retrieve details for the specified AwesomeLink
    """
    try:
        awesomelink = AwesomeLink.objects.get(pk=pk)
        serializer = AwesomeLinkSerializer(awesomelink, attach=['is_approved', 'is_embeddable'])
        return JsonResponse(serializer.data)
    except AwesomeLink.DoesNotExist:
        return JsonResponse({ 'error': AWESOMELINK_DNE_ERROR }, status=404)

@never_cache
def awesomelink_view(request):
    """
    Redirect to a random AwesomeLink
    """
    awesomelinks = AwesomeLink.objects.filter(is_approved=True)
    awesomelink = get_random_link(awesomelinks)
    context = {'awesomelink': awesomelink}
    awesomelink.click()
    if awesomelink.is_embeddable:
        return render(request, 'links/frame.html', context)
    return HttpResponseRedirect(awesomelink.url)

@api_view(['GET'])
def awesomelink_specific(request, pk):
    """
    Redirect to a specific AwesomeLink
    """
    try:
        # Should only redirect if link is approved
        awesomelink = AwesomeLink.objects.get(pk=pk)
        if awesomelink.is_approved:
            context = {'awesomelink': awesomelink}
            awesomelink.click()
            if awesomelink.is_embeddable:
                return render(request, 'links/frame.html', context)
            return HttpResponseRedirect(awesomelink.url)
        return JsonResponse({ 'error': AWESOMELINK_UNAPPROVED_ERROR }, status=403)
    except AwesomeLink.DoesNotExist:
        return JsonResponse({ 'error': AWESOMELINK_DNE_ERROR }, status=404)

@csrf_exempt
@api_view(['POST'])
@ratelimit(key='ip', rate='2/m')
def awesomelink_rate(request):
    """
    Rate an AwesomeLink
    """
    form = RatingForm(request.data)
    if form.is_valid():
        form_data = form.cleaned_data
        try:
            awesomelink = AwesomeLink.objects.get(pk=form_data['pk'])
            awesomelink.rate(form_data['rating'])
            serializer = AwesomeLinkSerializer(awesomelink)
            return JsonResponse(serializer.data)
        except AwesomeLink.DoesNotExist:
            return JsonResponse({'error': AWESOMELINK_DNE_ERROR}, status=404)
    # Return the first validation message that is thrown
    validation_error = list(form.errors.values())[0][0]
    return JsonResponse({'error': validation_error}, status=400)

@csrf_exempt
@api_view(['POST'])
@ratelimit(key='ip', rate='2/m')
def awesomelink_flag(request):
    """
    Flag the AwesomeLink with the specified pk
    """
    form = FlagForm(request.data)
    if form.is_valid():
        form_data = form.cleaned_data
        try:
            # There shouldn't be a case for flagging an unapproved link
            awesomelink = AwesomeLink.objects.get(pk=form_data['pk'], is_approved=True)
            # Don't want to actually flag anything until the functionality is implemented
            # awesomelink.flag()
            serializer = AwesomeLinkSerializer(awesomelink)
            return JsonResponse(serializer.data)
        except AwesomeLink.DoesNotExist:
            return JsonResponse(AWESOMELINK_DNE_ERROR, code=404)
    # Return the first validation message that is thrown
    validation_error = list(form.errors.values())[0][0]
    return JsonResponse({'error': validation_error}, status=400)

@csrf_exempt
@api_view(['POST'])
@ratelimit(key='ip', rate='2/m')
def awesomelink_submit(request):
    """
    Submit a new AwesomeLink
    """
    form = AwesomeLinkForm(data=request.data)
    if form.is_valid():
        awesomelink = form.save()
        serializer = AwesomeLinkSerializer(awesomelink)
        return JsonResponse(serializer.data, status=201)
    # Return the first validation message that is thrown
    validation_error = list(form.errors.values())[0][0]
    return JsonResponse({'error': validation_error}, status=400)
