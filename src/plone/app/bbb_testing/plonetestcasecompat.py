import unittest
import plone.app.testing.helpers

from plone.bbb_testing.zopetestcasecompat import user_name


class PTCCompatTestCase(unittest.TestCase):

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.portal['portal_workflow'].setDefaultChain(
            'simple_publication_workflow')
        self.afterSetUp()

    def afterSetUp(self):
        pass

    def setRoles(self, roles):
        plone.app.testing.helpers.setRoles(self.portal, user_name, roles)

    def tearDown(self):
        self.beforeTearDown()

    def beforeTearDown(self):
        pass
