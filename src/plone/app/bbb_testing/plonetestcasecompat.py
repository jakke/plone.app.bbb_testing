import unittest

import plone.app.testing.helpers
from plone.testing import z2
from plone.app.testing import login
from plone.app.testing import logout
from plone.app.testing.interfaces import SITE_OWNER_NAME
from plone.app.testing.interfaces import TEST_USER_NAME

from plone.bbb_testing.zopetestcasecompat import user_name

from Products.PloneTestCase.setup import _createHomeFolder


class PTCCompatTestCase(unittest.TestCase):

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.setUpCompat()
        self.afterSetUp()

    def setUpCompat(self):
        self.portal['portal_workflow'].setDefaultChain(
            'simple_publication_workflow')
        self.login()
        self._setupHomeFolder()

    def logout(self):
        logout()

    def login(self, name=TEST_USER_NAME):
        '''Logs in.'''
        login(self.portal, name)

    def _setupHomeFolder(self):
        '''Creates the default user's home folder.'''
        self.createMemberarea(user_name)
        pm = self.portal.portal_membership
        self.folder = pm.getHomeFolder(user_name)

    def createMemberarea(self, name):
        '''Creates a minimal memberarea.'''
        _createHomeFolder(self.portal, name)

    def afterSetUp(self):
        pass

    def setRoles(self, roles):
        plone.app.testing.helpers.setRoles(self.portal, user_name, roles)

    def loginAsPortalOwner(self):
        z2.login(self.app['acl_users'], SITE_OWNER_NAME)

    def tearDown(self):
        self.beforeTearDown()

    def beforeTearDown(self):
        pass
