from plone.outputfilters.filters.resolveuid_and_caption import IImageCaptioningEnabler
from zope.interface import implementer

@implementer(IImageCaptioningEnabler)
class CaptioningAlwaysEnabled(object):

    @property
    def available(self):
        return True
