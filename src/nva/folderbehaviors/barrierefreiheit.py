# -*- coding: utf-8 -*-
from zope.interface import alsoProvides, implementer
from zope.component import adapter
from zope import schema
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.app.textfield import RichText
from plone.supermodel import directives
from plone.supermodel import model
from plone.namedfile import field as namedfile
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice, RelationList

from nva.folderbehaviors import MessageFactory as _

class IBarrierefreiheit(model.Schema):
    """
       Interface fuer die Barrierefreiheit
    """

    directives.fieldset(
            'barrierefrei',
            label=_(u'Barrierefreiheit'),
            fields=('leichtesprache',),
        )

    leichtesprache = RichText(
        title=u"Leichte Sprache",
        description=u"Übersetzung des Inhalts in leichte Sprache",
        required=False,
        )

alsoProvides(IBarrierefreiheit, IFormFieldProvider)
