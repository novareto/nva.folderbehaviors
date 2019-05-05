from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class NvafolderbehaviorsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import nva.folderbehaviors
        xmlconfig.file(
            'configure.zcml',
            nva.folderbehaviors,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nva.folderbehaviors:default')

NVA_FOLDERBEHAVIORS_FIXTURE = NvafolderbehaviorsLayer()
NVA_FOLDERBEHAVIORS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NVA_FOLDERBEHAVIORS_FIXTURE,),
    name="NvafolderbehaviorsLayer:Integration"
)
NVA_FOLDERBEHAVIORS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NVA_FOLDERBEHAVIORS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="NvafolderbehaviorsLayer:Functional"
)
