capturemock_examples
====================

Examples of using capturemock

```
(capturemock)marca@marca-mac2:~/dev/git-repos/capturemock_examples$ python test_requests.py
resp = <Response [999]>
resp.url = u'http://www.google.com/'
resp.status_code = 999
resp.text = u'This is a fake response from CaptureMock!'
resp.headers = CaseInsensitiveDict({'X-Foo': 'Bar', 'Server': 'Fake
(capturemock)', 'Content-Type': 'text/plain; charset=UTF-8'})
resp.headers['Content-Type'] = 'text/plain; charset=UTF-8'
```
