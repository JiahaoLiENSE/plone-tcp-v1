# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plone.tcp


class PloneTcpLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plone.tcp)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.tcp:default')


PLONE_TCP_FIXTURE = PloneTcpLayer()


PLONE_TCP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_TCP_FIXTURE,),
    name='PloneTcpLayer:IntegrationTesting',
)


PLONE_TCP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_TCP_FIXTURE,),
    name='PloneTcpLayer:FunctionalTesting',
)


PLONE_TCP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_TCP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PloneTcpLayer:AcceptanceTesting',
)
