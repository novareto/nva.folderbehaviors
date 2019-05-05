# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class INvaFolderBehaviorsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class ISchmuckbilder(Interface):
    schmuckbilder = schema.TextLine(
            title = u"Pfad zu den Schmuckbilder für Nachrichten im Portal",
            default = u"/portalname/ordner/schmuckbilder",
    )
    archivzeit = schema.Int(
        title=u"Zeit bis zur Anzeige der Nachricht im Archiv in Tagen.",
        default=60,
        required=True,
        )

    deletezeit = schema.Int(
        title=u"Zeit bis zur Löschung der Nachricht.",
        default=365,
        required=True,
        )
