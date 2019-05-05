from  nva.folderbehaviors.testing import NVA_FOLDERBEHAVIORS_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=NVA_FOLDERBEHAVIORS_FUNCTIONAL_TESTING)
    ])
    return suite