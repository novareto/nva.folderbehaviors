# -*- coding: utf-8 -*-
from zope.interface import alsoProvides, implementer
from zope.component import adapter
from zope import schema
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import directives
from plone.supermodel import model
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.textfield import RichText

from nva.folderbehaviors import MessageFactory as _

class IRichtext(model.Schema):
    """
       Marker/Form interface for Navigation
    """

    directives.fieldset(
            'ordnertexte',
            label=_(u'Ordnertexte'),
            fields=('text','schlusstext',),
        )

    text = RichText(title=u"Haupttext",
            description=u"Hier können Sie den Haupttext des Ordners eingeben. Der Text wird\
                    oberhalb der Auflistung der Ordnerinhalte angezeigt",
            required=False,)

    schlusstext = RichText(title=u"Schlusstext",
            description=u"Hier können Sie Text eingeben der unterhalb der Auflistung der Ordnerinhalte\
                    angezeigt wird.",
            required=False,)


alsoProvides(IRichtext, IFormFieldProvider)
