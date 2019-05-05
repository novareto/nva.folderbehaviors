# -*- coding: utf-8 -*-
from zope.interface import alsoProvides, implementer
from zope.component import adapter
from zope import schema
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import directives
from plone.supermodel import model
from plone.namedfile import field as namedfile
from plone import api as ploneapi
from plone.uuid.interfaces import IUUID
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.contenttypes.interfaces import IImage
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.vocabularies.catalog import CatalogSource
from nva.folderbehaviors import MessageFactory as _
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from nva.folderbehaviors.interfaces import ISchmuckbilder
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from zope.interface import directlyProvides


def selectSchmuckbilder(context):
    terms = []
    registry = getUtility(IRegistry)
    settings = registry.forInterface(ISchmuckbilder)
    path =  settings.schmuckbilder
    portal = ploneapi.portal.get()
    pcat = portal.portal_catalog
    brains = pcat(portal_type="Image", path=path)
    for i in brains:
        uuid = IUUID(i.getObject(), None)
        terms.append(SimpleVocabulary.createTerm(uuid, uuid, i.Title.decode('utf-8')))
    newlist = sorted(terms, key=lambda x: x.title, reverse=False)
    return SimpleVocabulary(newlist)
directlyProvides(selectSchmuckbilder, IContextSourceBinder)

class ISchmuckbild(model.Schema):
    """
       Marker/Form interface fuer das Schmuckbild
    """

    schmuckbild = schema.Choice(
        title=u"Schmuckbild",
        description=u"Auswahl falls Teaserbild nicht vorhanden.",
        source = selectSchmuckbilder,
        required=False,
        )

alsoProvides(ISchmuckbild,IFormFieldProvider)
