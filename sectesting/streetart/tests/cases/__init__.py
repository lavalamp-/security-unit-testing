# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .auth import (
    AuthenticationEnforcementTestCase,
)

from .csrf import (
    CsrfEnforcementTestCase,
)

from .dos import (
    AdminViewRequestIsSuccessfulTestCase,
    RegularViewRequestIsSuccessfulTestCase,
)

from .headers import (
    HeaderKeyExistsTestCase,
    HeaderKeyNotExistsTestCase,
    HeaderValueAccurateTestCase,
)

from .hidden import (
    AdminUnknownMethodsTestCase,
    AdminVerbNotSupportedTestCase,
    RegularUnknownMethodsTestCase,
    RegularVerbNotSupportedTestCase,
)

from .requestor import (
    ViewHasRequestorTestCase,
)
