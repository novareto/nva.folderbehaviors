import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from nva.folderbehaviors.testing import \
    NVA_FOLDERBEHAVIORS_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = NVA_FOLDERBEHAVIORS_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'nva.folderbehaviors'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')
