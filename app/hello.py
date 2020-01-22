print('hello people')

url = 'https://github.com/PillarTechnology/phonebooth/releases/tag/latest'

# url = 'https://github.com/tflander/python-tag-release-spike/releases/tag/latest'

def downloadFile(URL=None):
    import httplib2
    h = httplib2.Http(".cache")
    resp, content = h.request(URL, "GET")
    return content

print(downloadFile(url))
