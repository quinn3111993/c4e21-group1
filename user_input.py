from mongoengine import Document, StringField, IntField
import mlab

mlab.connect()
class user_input(Document):
  meta = {
    'strict': False
  }
  topic = StringField()
  author = StringField()
  content = StringField()
  priority = IntField(default=0)


