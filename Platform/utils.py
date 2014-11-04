import json


def successJson(jsonObj):
    jsonreturnObj = dict({"Status":"Success" , "body":jsonObj})
    return json.dumps(jsonreturnObj)


def errorJson(jsonObj):
    jsonreturnObj = dict({"Status":"Error" , "error":jsonObj})
    return json.dumps(jsonreturnObj)
