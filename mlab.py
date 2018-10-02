import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds119343.mlab.com:19343/c4e21-group1

host = "ds119343.mlab.com"
port = 19343
db_name = "c4e21-group1"
user_name = "admin"
password = "codethechange1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())