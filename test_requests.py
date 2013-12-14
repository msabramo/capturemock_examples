from capturemock import capturemock, RECORD, REPLAY

@capturemock("requests")
def requests_get():
    import requests

    resp = requests.get("http://www.google.com/")
    print("resp = %r" % resp)
    print("resp.url = %r" % resp.url)
    print("resp.status_code = %r" % resp.status_code)
    print("resp.text = %r" % resp.text)
    print("resp.headers = %r" % resp.headers)
    print("resp.headers['Content-Type'] = %r" % resp.headers['Content-Type'])

requests_get()
