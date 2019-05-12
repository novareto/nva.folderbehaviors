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
from plone.app.contenttypes.interfaces import IImage
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.vocabularies.catalog import CatalogSource
from nva.folderbehaviors import MessageFactory as _


class ICards(model.Schema):
    """
       Marker/Form interface for Titelbild
    """

    model.fieldset(
            'contentcards',
            label=_(u'Karten'),
            fields=('cards',),
        )

    cards = RelationList(
        title=u"Inhalte als Karten",
        description=u"Bitte wählen Sie hier die Inhalte, die in Form einer Karte oder Box im Zusammenhang mit dem Inhalt angezeigt werden sollen.",
        default=[],
        value_type=RelationChoice(title=u"Inhalte",
                                  source=CatalogSource()),
        required=False,
        )

alsoProvides(ICards,IFormFieldProvider)
