import lightblue


def finddevices():
    addrs = []
    devices = lightblue.finddevices()
    mydevice = lightblue.gethostaddr()
    for d in devices:
        addrs.append(d)
    addrs.append(mydevice)
    return addrs

if __name__ == "__main__":
    addrs = finddevices()
    print addrs
