import os
import re
import json
from urllib.parse import urlparse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


from vvip_video.settings import BASE_DIR


CHANNELS = list()
def get_host_ms(host):
    # windows
    if os.name =='nt':
        command = f'ping {host}'
        print_ = os.popen(command)
        ping_res = print_.read()
        ms_list = re.findall(r'时间=(\d*)ms',ping_res)
    # unix /linux
    else:
        command = f'ping -c 4 {host}'
        print_ = os.popen(command)
        ping_res = print_.read()
        ms_list = re.findall(r'time=(\d*)\.\d* ms',ping_res)
    try:
        assert len(ms_list) == 4, 'ping error !!!'
        ms = sum(map(int,ms_list))/4
    except:ms = 99999
    return ms

def load_channel():
    path = os.path.join(BASE_DIR,'common','channel.json')
    with open(path,encoding='utf-8') as f:
        channel_list = json.loads(f.read())['list']
    for channel in channel_list:
        host = urlparse(channel['url']).netloc
        if host:
            ms = get_host_ms(host)
            if ms < 99999:
                channel['ms'] = ms
                CHANNELS.append(channel)
                break
    print('Channel load finish !!!')
load_channel()


def index(request):
    return render(request, 'index.html')


def get_channels(request):
    resp = JsonResponse(CHANNELS,safe=False)
    return resp


