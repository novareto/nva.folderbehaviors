from plone.outputfilters.filters.resolveuid_and_caption import IImageCaptioningEnabler
from zope.interface import implements

class CaptioningAlwaysEnabled(object):
    implements(IImageCaptioningEnabler)

    @property
    def available(self):
        return True
