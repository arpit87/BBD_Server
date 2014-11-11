import json

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def successJson(jsonObj):
    jsonreturnObj = dict({"Status":"Success" , "body":jsonObj})
    return json.dumps(jsonreturnObj,default=date_handler)


def errorJson(jsonObj):
    jsonreturnObj = dict({"Status":"Error" , "error":jsonObj})
    return json.dumps(jsonreturnObj,default=date_handler)
