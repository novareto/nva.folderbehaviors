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

display = SimpleVocabulary(
    [SimpleTerm(value=u'abovetitle', title=_(u'Kopf des Dokuments')),
     SimpleTerm(value=u'header', title=_(u'Unter den Navigationstabs'))]
    )

kind = SimpleVocabulary(
    [SimpleTerm(value=u'categoryimg', title=_(u'Kategorie, mit Titel und Beschreibung')),
     SimpleTerm(value=u'sectionimg', title=_(u'Sektion, nur mit Titel'))]
    )

class ITitelbild(model.Schema):
    """
       Marker/Form interface for Titelbild
    """

    model.fieldset(
            'medien',
            label=_(u'Titelbilder'),
            fields=('titleimages', 'viewlet', 'zufall'),
        )


    titleimages = RelationList(
        title=u"Titelbilder",
        description=u"Bitte waehlen Sie hier Bilder fuer die Anzeige im Titel des Objekts.",
        default=[],
        value_type=RelationChoice(title=u"Titelbilder",
                                  source=CatalogSource()),
        required=False,
        )

    viewlet = schema.Choice(
        title=_(u"Anzeige der Titelbilder"),
        description=u"Bitte waehlen Sie aus, an welcher Stelle der Seite das Banner angezeigt werden soll.",
        vocabulary=display,
        required=False,
        default=u'abovetitle',
        )

    #kind = schema.Choice(
    #    title=_(u"Art der Anzeige des Titelbildes"),
    #    description=u"Bitte waehlen Sie aus, auf welche Art das Titelbild angezeigt werden soll.",
    #    vocabulary=kind,
    #    required=False,
    #    default=u'categoryimg'
    #    )

    zufall = schema.Bool(
        title=u"Zufaellige Reihenfolge der Titelbilder",
        description=u"Auswahl wenn das angezeigte Titelbild nach dem Zufallsprinzip ausgewahlt werden soll.",
        required=False,
        )

#    newsimage = RelationChoice(
#        title=u"Nachrichtenbild",
#        description=u"Bitte waehlen Sie hier ein Bild fuer die Anzeige in der linken Spalte der Ordneransicht.",
#        source=CatalogSource(portal_type=['Folder', 'Image']),
#        required=False,
#        )

#    newstitle = schema.TextLine(
#        title=u"Titel des Nachrichtenbildes",
#        description=u"Ein vorhandener Titel ueberschreibt den Titel des Objekts in den Ordneransichten.",
#        required=False,
#        )

#    newstext = schema.Text(
#        title=u"Text des Nachrichtenbildes",
#        description=u"Ein vorhandener Text ueberschreibt die Kurzfassung des Objekts in den Ordneransichten.",
#        required=False,
#        )

#    videopath = RelationChoice(
#        title=u"Pfad zum Video",
#        description=u"Bitte waehlen Sie aus, mit welchem Videoobjekt das Titelbild verlinkt werden soll.",
#        source=CatalogSource(portal_type=['File']),
#        required=False,
#        )

#    imagepath = RelationChoice(
#        title=u"Pfad zur Bildergalerie",
#        description=u"Bitte waehlen Sie aus, mit welcher Bildergalerie das Titelbild verlinkt werden soll.",
#        source=CatalogSource(portal_type=['Folder']),
#        required=False,
#        )

alsoProvides(ITitelbild,IFormFieldProvider)
