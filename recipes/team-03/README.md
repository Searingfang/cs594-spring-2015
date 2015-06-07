#Multilayered API calls

**Problem:** RESTful API calls Requiring information from more API calls.

**Solution:** We will use Youtube for this example. Youtube has several parts to the API so while you can get a video list, you will get a larger amount of results with a search list.

Ingredients:
python 2.7
requests Library for python
Youtube API key

Step 1:
Make an API call to Youtube for a search list that gets the video ids

```
url = "https://www.googleapis.com/youtube/v3/search?part=id&maxResults=50&order=viewCount&type=video&key=[YOUR_API_KEY_HERE]"
r = requests.get(url)
struc = r.json()
```

Step 2:
Take the results from that API call's results and put them in an API call for a video list that can get more detailed information of the videos

```
url = "https://www.googleapis.com/youtube/v3/videos?part=id%2Cstatistics%2Csnippet%2CcontentDetails&maxResults=50&key=[YOUR_API_KEY_HERE]"
idList = []
for x in result[u'items']:
    idList.append(x[u'id'][u'videoId'])
r = requests.get(url + '&id=' + ','.join(idList))
struc = r.json()
```

Step 3:
Print your results
```
for y in struc[u'items']:
    print y[u'snippet'][u'title']
```

Now you're done gathering information from an API call based on information from another API call.

Extra Step:
Youtube results are given in pages of 50 each so to get all the information you have to iterate through the pages after the initial call.

Completed code
```
import requests

results = []
videos = []
url = "https://www.googleapis.com/youtube/v3/search?part=id&maxResults=50&order=viewCount&type=video&key=[YOUR_API_KEY_HERE]"
r = requests.get(url)
struc = r.json()
results.append(struc)
while u'nextPageToken' in struc:
    r = requests.get(url + '&pageToken=' + struc[u'nextPageToken'])
    struc = r.json()
    results.append(struc)
url = "https://www.googleapis.com/youtube/v3/videos?part=id%2Cstatistics%2Csnippet%2CcontentDetails&maxResults=50&key=[YOUR_API_KEY_HERE]"
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
```
