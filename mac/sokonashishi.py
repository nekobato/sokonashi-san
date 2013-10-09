import lightblue
import json
import urllib
import urllib2
import sys


def getaddrs():
    devices = lightblue.finddevices()
    addrs = []
    for d in devices:
        addrs.append(d[0])
    addrs.append(lightblue.gethostaddr())
    return json.dumps(addrs)


def getlastupdate():
    file = open('lastupdate', 'r+')
    return str(file.read())


def gettimelinecache():
    file = open('cache', 'r+').read()
    return json.loads(file)


def gettimeline(addrs, lastupdate=None):
    query = {
        addrs: addrs,
        lastupdate: lastupdate
    }
    query = urllib.urlencode(query)
    req = urllib2.Request('http://sokonashi.nekobato.net/timeline.php')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_data(query)

    res = urllib2.urlopen(req)
    body = res.read()

    return body


def main():
    addrs = getaddrs()
    res = gettimeline(addrs)
    resObj = json.loads(res)
    for i in resObj:
        print i[1] + " : " + i[0]


if __name__ == '__main__':
    main()
