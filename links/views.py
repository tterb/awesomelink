from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView

from .forms import RatingForm
from .helpers import get_random_link
from .models import AwesomeLink
from .serializers import AwesomeLinkSerializer, AwesomeLinkListSerializer


class awesomelink_list(ListCreateAPIView):
    """
    Retrieve an list of all AwesomeLinks
    """
    serializer_class = AwesomeLinkListSerializer
    queryset = AwesomeLink.objects.filter(is_approved=True)

def awesomelink_count(request):
    """
    Get the total number of AwesomeLinks
    """
    return JsonResponse({
        'count': AwesomeLink.objects.filter(is_approved=True).count(),
    })

@api_view(['GET'])
def awesomelink_detail(request, pk):
    """
    Retrieve details for the specified AwesomeLink
    """
    try:
        awesomelink = AwesomeLink.objects.get(pk=pk)
        serializer = AwesomeLinkSerializer(awesomelink)
        return JsonResponse(serializer.data)
    except AwesomeLink.DoesNotExist as awesomelink_dne:
        raise Http404('AwesomeLink does not exist') from awesomelink_dne

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

def awesomelink_specific(request, pk):
    """
    Redirect to a specific AwesomeLink
    """
    try:
        # Should only redirect if link is approved
        awesomelink = AwesomeLink.objects.get(pk=pk, is_approved=True)
        context = {'awesomelink': awesomelink}
        awesomelink.click()
        if awesomelink.is_embeddable:
            return render(request, 'links/frame.html', context)
        return HttpResponseRedirect(awesomelink.url)
    except AwesomeLink.DoesNotExist as awesomelink_dne:
        raise Http404('AwesomeLink does not exist') from awesomelink_dne

@csrf_exempt
@api_view(['POST'])
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
        except AwesomeLink.DoesNotExist as awesomelink_dne:
            raise Http404('AwesomeLink does not exist') from awesomelink_dne
    response = HttpResponse('Invalid \"rating\" parameter value')
    response.status_code = 400
    return response

@csrf_exempt
@api_view(['POST'])
def awesomelink_flag(request):
    """
    Flag the AwesomeLink with the specified pk
    """
    try:
        data = request.data
        awesomelink = AwesomeLink.objects.get(pk=data['pk'])
        # Don't want to actually flag anything until the functionality is implemented
        # awesomelink.flag()
        serializer = AwesomeLinkSerializer(awesomelink)
        return JsonResponse(serializer.data)
    except AwesomeLink.DoesNotExist as awesomelink_dne:
        raise Http404('AwesomeLink does not exist') from awesomelink_dne

@csrf_exempt
@api_view(['POST'])
def awesomelink_submit(request):
    """
    Submit a new AwesomeLink
    """
    serializer = AwesomeLinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
