from mongoengine import Document, StringField, IntField

class Quote(Document):
  meta = {
    'strict': False
  }
  topic = StringField()
  author = StringField()
  content = StringField()
  priority = IntField(default=0)