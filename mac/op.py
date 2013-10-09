import httplib2


def main():
    h = httplib2.Http()
    resp, content = h.request("http://nekobato.net/", "GET")


if __name__ == '__main__':
    main()