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

class IEinstellungen(model.Schema):
    """
       Marker/Form interface for Einstellungen
    """

    model.fieldset(
            'settings',
            label=_(u'Einstellungen'),
            fields=('excludeFromDisplay', 'alttitle', 'columns'),
        )

    alttitle = schema.TextLine(title=u'Alternativer Titel',
                               description=u'Wird verwendet, wenn der Originaltitel für die Darstellungsformate der Ordner zu lang ist.',
                               required = False)

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
