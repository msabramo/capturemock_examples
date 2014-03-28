from capturemock import capturemock, REPLAY


@capturemock(["urllib2", "urllib", "httplib"], mode=REPLAY)
def test_urllib2():
    # Test capturemock replay by replaying from a file that simulates Google
    # responding with a fake error.
    #
    # Note that we have to capture urllib2 as well as urllib and httplib.
    # This is because the response from urllib2.urlopen is in the urllib module
    # and the `headers` attribute of the response is of a class defined in the
    # httplib module.

    import urllib
    import urllib2

    resp = urllib2.urlopen("http://www.google.com/")
    assert resp.code == 702
    assert resp.url == "http://www.google.com/when-pigs-fly"
    assert resp.headers['X-Fake-Message'] == 'This is a fake response header'
    assert resp.read() == 'Simulating a fake error'


@capturemock(["urllib2", "urllib", "httplib"], mode=REPLAY)
def urllib2_interactive():
    # Test capturemock replay by replaying from a file that simulates Google
    # responding with a fake error.
    #
    # Note that we have to capture urllib2 as well as urllib and httplib.
    # This is because the response from urllib2.urlopen is in the urllib module
    # and the `headers` attribute of the response is of a class defined in the
    # httplib module.

    import urllib
    import urllib2

    resp = urllib2.urlopen("http://www.google.com/")
    print("resp.code = %r" % resp.code)
    print("resp.url = %r" % resp.url)
    # print("resp.headers = %r" % resp.headers.keys())
    print("resp.headers['X-Fake-Message'] = %r"
            % resp.headers['X-Fake-Message'])
    print("resp.read() => %r" % resp.read())


if __name__ == '__main__':
    urllib2_interactive()
