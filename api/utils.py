import json


def parse_response(response):
    result = json.load(response.content)
    return result
