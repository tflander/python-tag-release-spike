print('hello people')
print('fake pencil feature added')

url = 'https://github.com/PillarTechnology/phonebooth/releases/tag/latest'

# url = 'https://github.com/tflander/python-tag-release-spike/releases/tag/latest'

def downloadFile(URL=None):
    import httplib2
    h = httplib2.Http(".cache")

    h.add_credentials('toddfbass@gmail.com', 'PinkBalloonHeart123!')

    resp, content = h.request(URL, "GET")
    return content

print(downloadFile(url))





