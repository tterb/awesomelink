from django.core.exceptions import SuspiciousOperation
from django.db.models import Q
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from rest_framework import (
    generics,
    mixins,
    permissions,
    status,
)
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .forms import RatingForm
from .helpers import get_random_link
from .models import AwesomeLink
from .serializers import AwesomeLinkSerializer, AwesomeLinkListSerializer


class AwesomeLinkList(generics.ListCreateAPIView):
    """
    Retrieve an list of all AwesomeLinks
    """
    serializer_class = AwesomeLinkListSerializer
    queryset = AwesomeLink.objects.filter(is_approved=True)

@api_view(['GET'])
def AwesomeLinkDetail(request, pk):
    """
    Retrieve details for the specified AwesomeLink
    """
    try:
        awesome_link = AwesomeLink.objects.get(pk=pk)
        serializer = AwesomeLinkSerializer(awesome_link)
        return JsonResponse(serializer.data)
    except AwesomeLink.DoesNotExist:
        raise Http404('AwesomeLink does not exist')

def AwesomeLinkRedirect(request):
    """
    Redirect to a random AwesomeLink
    """
    awesome_links = AwesomeLink.objects.filter(is_approved=True)
    awesome_link = get_random_link(awesome_links)
    context = {'awesome_link': awesome_link}
    awesome_link.click()
    return render(request, 'links/frame.html', context)
    # return HttpResponseRedirect(awesome_link.url)

def AwesomeLinkSpecific(request, pk):
    """
    Redirect to a specific AwesomeLink
    """
    try:
        # Should only redirect if link is approved
        awesome_link = AwesomeLink.objects.get(pk=pk, is_approved=True)
        awesome_link.click()
        return HttpResponseRedirect(awesome_link.url)
    except AwesomeLink.DoesNotExist:
        raise Http404('AwesomeLink does not exist')

@csrf_exempt
@api_view(['POST'])
def AwesomeLinkRate(request):
    """
    Rate an AwesomeLink
    """
    form = RatingForm(request.data)
    if form.is_valid():
        form_data = form.cleaned_data
        try:
            awesome_link = AwesomeLink.objects.get(pk=form_data['pk'])
            awesome_link.rate(form_data['rating'])
            serializer = AwesomeLinkSerializer(awesome_link)
            return JsonResponse(serializer.data)
        except AwesomeLink.DoesNotExist:
            raise Http404('AwesomeLink does not exist')
    response = HttpResponse('Invalid \"rating\" parameter value')
    response.status_code = 400
    return response

@csrf_exempt
@api_view(['POST'])
def AwesomeLinkFlag(request):
    """
    Flag the AwesomeLink with the specified pk
    """
    try:
        data = request.data
        awesome_link = AwesomeLink.objects.get(pk=data['pk'])
        # Don't want to actually flag anything until the functionality is implemented
        # awesome_link.flag()
        serializer = AwesomeLinkSerializer(awesome_link)
        return JsonResponse(serializer.data)
    except AwesomeLink.DoesNotExist:
        raise Http404('AwesomeLink does not exist')

def AwesomeLinkCount(request):
    """
    Get the current number of AwesomeLinks
    """
    return JsonResponse({
        'count': AwesomeLink.objects.filter(is_approved=True).count(),
    })

@csrf_exempt
@api_view(['POST'])
def AwesomeLinkSubmit(request):
    """
    Submit a new AwesomeLink
    """
    submission_data = JSONParser().parse(request)
    serializer = AwesomeLinkSerializer(data=submission_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

