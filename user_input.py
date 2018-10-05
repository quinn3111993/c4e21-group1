from mongoengine import Document, StringField, IntField
import mlab

mlab.connect()
class User_input(Document):
  meta = {
    'strict': False
  }
  topic = StringField()
  author = StringField()
  content = StringField()
  priority = IntField(default=0)

# form = User_input(
#   topic="message",
#   author="quinn",
#   content="Today is a new day!",
#   priority=0
# )
# form.save()
