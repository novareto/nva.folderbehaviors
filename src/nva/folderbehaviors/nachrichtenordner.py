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

class INachrichtenOrdner(model.Schema):
    """
       Marker/Form interface for Nachrichtenordner
    """

    model.fieldset(
            'nachrichtenordner',
            label=_(u'Nachrichtenordner'),
            fields=('newsfolder',),
        )

    newsfolder = RelationList(
        title=u"Weitere Nachrichtenordner",
        description=u"Bitte wählen Sie hier weitere Ordner aus, aus denen Sie Nachrichten anzeigen wollen.",
        default=[],
        value_type=RelationChoice(title=u"Nachrichtenordner",
                                  source=CatalogSource()),
        required=False,
        )

alsoProvides(INachrichtenOrdner,IFormFieldProvider)
