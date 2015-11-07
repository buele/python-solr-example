import http.client
import json
import sys

connection = http.client.HTTPConnection("localhost",8983)

headers = {'Content-type': 'application/json'}


connection.request('GET', '/solr/core/select?wt=json&indent=true&q='+str(sys.argv[1]))

response = connection.getresponse()
print(response.read().decode())
