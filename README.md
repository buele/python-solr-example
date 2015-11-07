python-solr-example
=====================================
Silly solr connection with python


# Requirements
 - python 3.x 
 - solr 5.x
 - java 1.8.x
 
# Install solr 
 1. Download: [mirrors](http://www.apache.org/dyn/closer.lua/lucene/solr/5.3.1)
 - Unpack ``` $ tar zxf solr-5.x.x.tgz ```
 
# Run solr 
 - ``` $ cd solr-5.x.x ```
 - Run: ``` $ bin/solr start ```
 
# Create core 
 - Create a core with name *core*: ``` $ bin/solr create -c core ```
 
# Clone the project
```
$ git clone git@github.com:buele/python-solr-example.git
```

# Add Document to core *core*
```
$ cd python-solr-example/
$ python3 add_document.py "new_document_id" "New Document Title!"
```
Output: 
```
{"responseHeader":{"status":0,"QTime":191}}
```

# Search a document in core *core*
```
$ python3 search.py  "Title"
```

Output: 
```
{
  "responseHeader":{
    "status":0,
    "QTime":15,
    "params":{
      "q":"Title",
      "indent":"true",
      "wt":"json"}},
  "response":{"numFound":1,"start":0,"docs":[
      {
        "title":["New Document Title"],
        "id":"new_document_id",
        "_version_":1517198064616472576}]
  }}


```







