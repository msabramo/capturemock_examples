capturemock_examples
====================

[![Build
Status](https://travis-ci.org/msabramo/capturemock_examples.svg?branch=master)](https://travis-ci.org/msabramo/capturemock_examples)

Examples of using
[CaptureMock](https://pypi.python.org/pypi/CaptureMock) to record and
replay calls in Python code.

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

See also:

* https://github.com/msabramo/capturemock_test_sqlalchemy

