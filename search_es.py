import sys
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError
es_host = "localhost:9200"
index_name = "test_handbill"
messages = [
        'Handbill not printed Lorem ipsum dolor sit amet',
        'Labore Handbill not printed nullam',
        'In sit modo Handbill not printed concludaturque',
        'Alienum definitionem no sea Handbill not printed Facete'
]
message_to_search = "Handbill not printed"

def prepare(es_host, index_name):
    i = 1
    try:
        target_es = Elasticsearch(
            [es_host]
        )
        if target_es.indices.exists(index=index_name):
            target_es.indices.delete(index=index_name)
            target_es.indices.create(index=index_name)
            for message in messages:
                target_es.index(index=index_name, doc_type="articles", body={"content": message}, id=i)
                i +=1
        else:
            target_es.indices.create(index=index_name)
            for message in messages:
                target_es.index(index=index_name, doc_type="articles", body={"content": message}, id=i)
                i +=1

    except ConnectionError as e:
        print ("\n\n[ERROR] %s" %(str(e)))

def count(es_host, index_name, message_to_search):
    try:
        target_es = Elasticsearch(
            [es_host]
        )
        if target_es.indices.exists(index=index_name):
            target_es.indices.refresh(index=index_name)
            search_result = target_es.search(index=index_name, body={"query": {"match": {"content": message_to_search}}})
            search_result_hits = search_result['hits']['total']
            return(search_result_hits)
        else:
            print ("\n[INFO] Index does not exist %s" % index_name)

    except ConnectionError as e:
        print ("\n\n[ERROR] %s" %(str(e)))

def trigger():
    if count(es_host, index_name, message_to_search) < 3:
        print("OK")
        sys.exit(0)
    else:
        print("CRITICAL")
        sys.exit(2)

def main():
    prepare(es_host, index_name)
    count(es_host, index_name, message_to_search)
    trigger()
if __name__ == "__main__":
    main()
