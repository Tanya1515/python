import requests

#Get video with REST API request by https://rutube.ru/api/video/recommendation/<video_id>/?mode=pilot&header=1&seed=1&client=wdp

video_id = 'a0f5ea1ff48debe622eb603f491f7365'
link = 'https://rutube.ru/api/video/recommendation/' + video_id + '/?mode=pilot&header=1&seed=1&client=wdp'

resp = requests.get(link)
if resp.status_code == 200:
    res = resp.json

open('video.yaml', 'wb').write(resp.content) #save video content to video.yaml