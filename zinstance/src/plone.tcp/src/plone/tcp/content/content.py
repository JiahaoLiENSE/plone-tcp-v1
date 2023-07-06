from plone.dexterity.content import Item
from zope.interface import implementer
from plone.supermodel import model

class IMyTCPContent(model.Schema):
    # Define fields for your content type here
    tcp_data = schema.Text(title="TCP Data")

@implementer(IMyTCPContent)
class MyTCPContent(Item):
    pass
