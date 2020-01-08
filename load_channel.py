import os
import re
import json
from urllib.parse import urlparse
from vvip_video.settings import BASE_DIR


def get_host_ms(host):
    if os.name =='nt':
        # windows
        command = f'ping {host}'
        print_ = os.popen(command)
        ping_res = print_.read()
        ms_list = re.findall(r'时间=(\d*)ms',ping_res)
    else:
        # unix /linux
        command = f'ping -c 4 {host}'
        print_ = os.popen(command)
        ping_res = print_.read()
        ms_list = re.findall(r'time=(\d*)\.\d* ms',ping_res)
    try:
        assert len(ms_list) == 4, 'ping error !!!'
        ms = sum(map(int,ms_list))/4
    except:ms = 99999
    return ms

def refresh_channels():
    CHANNELS = list()
    path = os.path.join(BASE_DIR,'common','channel.json')
    with open(path,encoding='utf-8') as f:
        channel_list = json.loads(f.read())['list']
    for channel in channel_list:
        print(channel)
        host = urlparse(channel['url']).netloc
        if host:
            ms = get_host_ms(host)
            if ms < 99999:
                channel['ms'] = ms
                CHANNELS.append(channel)
    print('Channel load finish !!!')
    channel_current_path = os.path.join(BASE_DIR,'common','channel_current.json')
    with open(channel_current_path,'w',encoding='utf-8') as f:
        f.write(json.dumps(CHANNELS))

def load_channels():
    channel_current_path = os.path.join(BASE_DIR, 'common', 'channel_current.json')
    with open(channel_current_path) as f:
        CHANNELS = json.loads(f.read())
    return CHANNELS


if __name__ == '__main__':
    refresh_channels()