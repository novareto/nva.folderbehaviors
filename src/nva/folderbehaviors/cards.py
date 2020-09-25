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
from nva.folderbehaviors.einstellungen import column_vocabulary
from nva.folderbehaviors import MessageFactory as _

terms = [ 
        SimpleTerm(u'card text-white bg-primary mb-3', u'card text-white bg-primary mb-3', u'blauer Hintergrund'),
        SimpleTerm(u'card text-white bg-secondary mb-3', u'card text-white bg-secondary mb-3', u'dunkelgrauer Hintergrund'),
        SimpleTerm(u'card text-white bg-success mb-3', u'card text-white bg-success mb-3', u'grüner Hintergrund'),
        SimpleTerm(u'card text-white bg-danger mb-3', u'card text-white bg-danger mb-3', u'roter Hintergrund'),
        SimpleTerm(u'card text-white bg-warning mb-3', u'card text-white bg-warning mb-3', u'oranger Hintergrund'),
        SimpleTerm(u'card text-white bg-info mb-3', u'card text-white bg-info mb-3', u'türkiser Hintergrund'),
        SimpleTerm(u'card border-primary mb-3', u'card border-primary mb-3', u'blauer Rahmen'),
        SimpleTerm(u'card card-shadow mb-3', u'card card-shadow mb-3', u'grauer Hintergrund, Schattierung'),
        ]
cardsVocabulary = SimpleVocabulary(terms)

class ICards(model.Schema):
    """
       Marker/Form interface for Titelbild
    """

    model.fieldset(
            'contentcards',
            label=_(u'Portlets und Karten'),
            fields=('cards', 'contentcards', 'cardcolumns', 'cardcolor'),
        )

    cards = RelationList(
        title=u"Auswahl Portlets",
        description=u"Bitte wählen Sie hier die Artikel, die als Karten in der rechten Spalte des Portals angezeigt werden sollen.",
        default=[],
        value_type=RelationChoice(title=u"Inhalte",
                                  source=CatalogSource(portal_type=['Folder', 'Document','Image','Collection', 'Portlet'])),
        required=False,
        )

    contentcards = RelationList(
        title=u"Auswahl Content-Karten",
        description=u"Bitte wählen Sie hier die Artikel, die als Karten nach dem Haupttext (vor dem Schlusstext) angezeigt werden sollen.",
        default=[],
        value_type=RelationChoice(title=u"Inhalte",
                                  source=CatalogSource()),
        required=False,
        )


    cardcolumns = schema.Choice(
        title=u"Anzahl der Content-Karten",
        description=u"Anzahl der Content-Karten, die nebeneinander angezeigt werden dürfen.",
        vocabulary=column_vocabulary,
        default=3)


    cardcolor = schema.Choice(
        title = u"Farbe der Karte",
        description = u"Wenn dieser Artikel als Portlet oder Content-Karte verwendet wird, kann hier die Farbe der Karte eingestellt werden.",
        vocabulary = cardsVocabulary,
        default = 'card card-shadow mb-3'
        )

alsoProvides(ICards,IFormFieldProvider)
