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

class IDownloads(model.Schema):
    """
       Marker/Form interface for Download-Area
    """

    model.fieldset(
            'downloads',
            label=_(u'Downloads'),
            fields=('downloads',)
        )

    downloads = RelationList(
        title=u"Downloads",
        description=u"Bitte waehlen Sie hier Dateien aus, die im Downloadbereich angezeigt werden sollen.",
        default=[],
        value_type=RelationChoice(title=u"Downloads",
                                  source=CatalogSource(portal_type=['File'])),
        required=False,
        )

alsoProvides(IDownloads, IFormFieldProvider)
