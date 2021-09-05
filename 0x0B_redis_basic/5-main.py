#!/usr/bin/env python3

get_page = __import__("web").get_page
r = __import__("web").r
url = "http://slowwly.robertomurray.co.uk"
print(get_page(url))
# print(r.get(f"result:{url}"))
print(r.get(f"count:{url}"))
print(get_page(url))
print(r.get(f"count:{url}"))
