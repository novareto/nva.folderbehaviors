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


terms = [ 
        SimpleTerm(u'card text-white bg-primary mb-3', u'card text-white bg-primary mb-3', u'blauer Hintergrund'),
        SimpleTerm(u'card text-white bg-secondary mb-3', u'card text-white bg-secondary mb-3', u'dunkelgrauer Hintergrund'),
        SimpleTerm(u'card text-white bg-success mb-3', u'card text-white bg-success mb-3', u'grüner Hintergrund'),
        SimpleTerm(u'card text-white bg-danger mb-3', u'card text-white bg-danger mb-3', u'roter Hintergrund'),
        SimpleTerm(u'card text-white bg-warning mb-3', u'card text-white bg-warning mb-3', u'oranger Hintergrund'),
        SimpleTerm(u'card text-white bg-info mb-3', u'card text-white bg-info mb-3', u'türkiser Hintergrund'),
        SimpleTerm(u'card border-primary mb-3', u'card border-primary mb-3', u'blauer Rahmen'),
        ]
cardsVocabulary = SimpleVocabulary(terms)

class ICards(model.Schema):
    """
       Marker/Form interface for Titelbild
    """

    model.fieldset(
            'contentcards',
            label=_(u'Portlets'),
            fields=('cards', 'cardcolor'),
        )

    cards = RelationList(
        title=u"Inhalte als Portlets",
        description=u"Bitte wählen Sie hier die Inhalte, die in Form einer Karte oder Box im Zusammenhang mit dem Inhalt angezeigt werden sollen.",
        default=[],
        value_type=RelationChoice(title=u"Inhalte",
                                  source=CatalogSource()),
        required=False,
        )

    cardcolor = schema.Choice(
        title = u"Farbe der Portlet-Karte",
        description = u"Wenn dieser Artikel als Portlet verwendet wird, kann hier die Farbe der Portlet-Karte konfiguriert werden.",
        vocabulary = cardsVocabulary,
        default = 'card border-primary mb-3'
        )

alsoProvides(ICards,IFormFieldProvider)
