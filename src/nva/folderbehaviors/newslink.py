# -*- coding: utf-8 -*-
from zope.interface import alsoProvides, implementer
from zope.component import adapter
from zope import schema
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import directives
from plone.supermodel import model
from plone.namedfile import field as namedfile
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice, RelationList

from nva.folderbehaviors import MessageFactory as _

class INewslink(model.Schema):
    """
       Marker/Form interface for Navigation
    """

    directives.fieldset(
            'newslink',
            label=_(u'Nachrichtenlink'),
            fields=('newsurl','extnews','extnewstitle'),
        )

    newsurl = RelationChoice(
        title=u"Nachrichtenobjekt",
        description=u"Bitte hier einen Artikel auswählen, zu dem weitergeleitet werden soll.",
        source=CatalogSource(portal_type=['Folder', 'Document', 'News Item']),
        required=False,
        )

    extnews = schema.URI(
        title=u"Alternativ: Externe Nachrichtenquelle",
        description=u"Bitte hier eine alternative externe URL eintragen zu der weitergeleitet werden soll.",
        required=False,
        )

    extnewstitle = schema.TextLine(
        title=u"Titel der externen Nachrichtenquelle",
        required=False,
        )

alsoProvides(INewslink, IFormFieldProvider)
