# Copyright 2017,2018 The DIPP contributors
#
# This file is part of DIPP.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.

"""Library of custom add-ons for Deep Learning frameworks."""

__version__ = '0.1.0.dev0'

__all__ = ('util',)

from . import util

# We don't add any of the Deep-Learning-framework-specific subpackages here
# to keep their namespaces separate. This allows users to only install
# selected frameworks and still be able to import the relevant subpackages
# without getting ImportError due to a missing module.
