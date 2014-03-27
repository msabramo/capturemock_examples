from capturemock import capturemock, RECORD, REPLAY


@capturemock("requests", mode=REPLAY)
def test_requests_get():
    import requests

    resp = requests.get("http://www.google.com/")
    assert isinstance(resp, requests.Response)
    assert repr(resp) == '<Response [999]>'
    assert resp.url == u'http://www.google.com/'
    assert resp.status_code == 999
    assert resp.text == u'This is a fake response from CaptureMock!'
    assert len(repr(resp.headers)) > 0
    assert resp.headers['Content-Type'] == 'text/plain; charset=UTF-8'


@capturemock("requests", mode=REPLAY)
def requests_get_interactive():
    import requests

    resp = requests.get("http://www.google.com/")
    print("resp = %r" % resp)
    print("resp.url = %r" % resp.url)
    print("resp.status_code = %r" % resp.status_code)
    print("resp.text = %r" % resp.text)
    print("resp.headers = %r" % resp.headers)
    print("resp.headers['Content-Type'] = %r" % resp.headers['Content-Type'])


if __name__ == '__main__':
    requests_get_interactive()
