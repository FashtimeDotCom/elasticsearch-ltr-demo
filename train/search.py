baseQuery = {
      "query": {
        "sltr": {
            "params": {
                "keywords": ""
            },
            "model": "",
      }
   }
}

def ltrQuery(keywords, modelName):
    import json
    baseQuery['query']['sltr']['model'] = model
    baseQuery['query']['sltr']['params']['keywords'] = keywords
    print("%s" % json.dumps(baseQuery))
    return baseQuery


if __name__ == "__main__":
    import configparser
    from sys import argv
    from elasticsearch import Elasticsearch

    config = configparser.ConfigParser()
    config.read('settings.cfg')
    esUrl=config['DEFAULT']['ESHost']

    es = Elasticsearch(esUrl, timeout=1000)
    model = "test_6"
    if len(argv) > 2:
        model = argv[2]
    results = es.search(index='tmdb', doc_type='movie', body=ltrQuery(argv[1], model))
    for result in results['hits']['hits']:
             print("%s " % (result['_source']['title']))

