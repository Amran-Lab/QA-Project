import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://130.211.114.138:5000/')
    assert 200 == r.status
def test_about():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://130.211.114.138:5000/about')
    assert 200 == r.status

def test_login():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://130.211.114.138:5000/login')
    assert 404 == r.status
