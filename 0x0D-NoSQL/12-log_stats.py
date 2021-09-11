#!/usr/bin/env python3
"""Module"""


def main(mongo_collections):
    """[main]
    """
    methods = {'GET': 0, 'POST': 0,
               'PUT': 0, 'PATCH': 0,
               'DELETE': 0}
    nbr = 0
    res = mongo_collections.find({})
    for i in res:
        if i.get("method") in methods:
            methods[i.get("method")] += 1
        if i.get("method") == 'GET' and i.get('path') == '/status':
            nbr += 1

    s = "".join('\tmethod {}: {}\n'.format(k, v) for k, v in methods.items())
    print('{} logs\nMethods:\n{}{} status check'
          .format(sum(methods.values()), s, nbr))


if __name__ == '__main__':
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    logs = client.logs
    mongo_collections = logs.nginx
    if not mongo_collections:
        return
    main(mongo_collections)
