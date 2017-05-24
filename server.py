import falcon
import json
import traceback

class ItemsResource:
    items = {
        "Components": {
            "First": 0.1,
            "Second": 0.5
        }
    }

    def on_get(self, req, resp):
        print 'on_get method called'
        resp.body = json.dumps(self.items)

    def on_put(self, req, resp):
        print 'put_put method called'
        body = req.stream.read()
        data = json.loads(body)
        print data

        try:
            self.items['Components']['First'] = data['Components']['First']
            self.items['Components']['Second'] = data['Components']['Second']
        except:
            traceback.print_exc()
    
api = falcon.API()
api.add_route('/study/12345678', ItemsResource())

from wsgiref import simple_server
httpd = simple_server.make_server('127.0.0.1', 8000, api)
httpd.serve_forever()