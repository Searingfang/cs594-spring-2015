# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 21:25:06 2015

@author: todd
"""

import requests

results = []
videos = []
url = "https://www.googleapis.com/youtube/v3/search?part=id&maxResults=50&order=viewCount&type=video&key=AIzaSyDMg-eb-hHji1WEF_H_je1SXSt9HsMeofU"
r = requests.get(url)
struc = r.json()
results.append(struc)
while u'nextPageToken' in struc:
    r = requests.get(url + '&pageToken=' + struc[u'nextPageToken'])
    struc = r.json()
    results.append(struc)
url = "https://www.googleapis.com/youtube/v3/videos?part=id%2Cstatistics%2Csnippet%2CcontentDetails&maxResults=50&key=AIzaSyDMg-eb-hHji1WEF_H_je1SXSt9HsMeofU"
for result in results:
    idList = []
    for x in result[u'items']:
        idList.append(x[u'id'][u'videoId'])
    r = requests.get(url + '&id=' + ','.join(idList))
    struc = r.json()
    videos.append(struc)
for x in xrange(len(videos)):
    for y in videos[x][u'items']:
        print y[u'snippet'][u'title']