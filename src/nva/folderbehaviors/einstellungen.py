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

values = [2, 3, 4]
column_vocabulary = SimpleVocabulary.fromValues(values)

batchvalues = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 100, 150, 200, 250]
batch_vocabulary = SimpleVocabulary.fromValues(batchvalues)

class IEinstellungen(model.Schema):
    """
       Marker/Form interface for Einstellungen
    """

    model.fieldset(
            'settings',
            label=_(u'Einstellungen'),
            fields=('batchvalue', 'excludeFromDisplay', 'alttitle', 'dachzeile', 'columns'),
        )

    alttitle = schema.TextLine(title=u'Alternativer Titel',
                               description=u'Wird verwendet, wenn der Originaltitel für die Darstellungsformate der Ordner zu lang ist.',
                               required = False)

    dachzeile = schema.TextLine(title=u"Dachzeile",
                                description=u"Wenn vorhanden wird die Dachzeile oberhalb des Titels angezeigt.",
                                required = False)

    batchvalue = schema.Choice(
        title=u"Anzahl der Artikel im Stapel",
        description=u"Bestimmt die Anzahl der Artikel auf einer Seite. Bei der Angabe von 0 werden alle Artikel des Ordners angezeigt.",
        required=True,
        vocabulary=batch_vocabulary,
        default=0
        )


    excludeFromDisplay = schema.Bool(
        title=u"Von Anzeige ausschließen",
        description=u"Bestimmt, ob der Artikel in den Darstellungsformaten der Ordner angezeigt wird.",
        required=False,
        )

    columns = schema.Choice(
        title=u"Anzahl von Spalten",
        description=u"Anzahl von Spalten in der Kartenansicht",
        vocabulary=column_vocabulary,
        default=3)

alsoProvides(IEinstellungen,IFormFieldProvider)
