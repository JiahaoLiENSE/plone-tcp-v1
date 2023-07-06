# -*- coding: utf-8 -*-
"""Init and utils."""
from plone.tcp.content import MyTCPContent
from zope.i18nmessageid import MessageFactory

def initialize(context):
    # Register your content type with Plone
    from plone.dexterity import ftidata
    ftidata.register()
    context.registerClass(
        MyTCPContent,
        constructors=(MyTCPContent,),
        permission='plone.tcp: Add My TCP Content',
        )

_ = MessageFactory('plone.tcp')
