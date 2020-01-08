from django.shortcuts import render
from django.http import JsonResponse

from load_channel import load_channels


def index(request):
    return render(request, 'index.html')

def get_channels(request):
    CHANNELS = load_channels()
    resp = JsonResponse(CHANNELS,safe=False)
    return resp


