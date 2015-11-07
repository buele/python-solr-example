import http.client
import json
import sys

connection = http.client.HTTPConnection("localhost",8983)

headers = {'Content-type': 'application/json'}

foo = {'add': {'doc': {'id': sys.argv[1], 'title': sys.argv[2]}, 'boost': 1, 'overwrite': True, 'commitWithin': 1000}}
json_foo = json.dumps(foo)

connection.request('POST', '/solr/core/update?wt=json', json_foo, headers)

response = connection.getresponse()
print(response.read().decode())
