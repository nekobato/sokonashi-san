import sys
import lightblue
import urllib
import urllib2


a = sys.argv

addr = lightblue.gethostaddr()
echo = a[1]

q = {"deviceaddr": addr, "echo": echo}
q = urllib.urlencode(q)

req = urllib2.Request('http://sokonashi.nekobato.net/echo.php')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_data(q)
res = urllib2.urlopen(req)

print res.read()
