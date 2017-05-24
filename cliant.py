import httplib
import json
import urllib
import traceback

svr = '127.0.0.1:8000'
h = None
data = None

def connect():
    global h
    if h != None: return
    h = httplib.HTTPConnection(svr)

def close():
    global h
    if h == None: return
    h.close()
    h = None

def get():
    connect()
    try:
        h.request('GET', '/study/12345678')
    except:
        traceback.print_exc()
        close()
        return
    response = h.getresponse()
    if response.status == httplib.OK:
        body = response.read()
        global data
        data = json.loads(body)
        print data
    else:
        print response.status
    close()

def put():
    global data
    if data == None: return
    connect()

    data['Components']['GW'] = data['Components']['GW'] + 1
    data['Components']['ECU1'] = data['Components']['ECU1'] + 1
    try:
        h.request('PUT', '/study/12345678', json.dumps(data))
    except:
        traceback.print_exc()
        close()
        data['Components']['First'] = data['Components']['First'] - 1
        data['Components']['Second'] = data['Components']['Second'] - 1
        return
    close()