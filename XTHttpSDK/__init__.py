# -*- coding:utf8 -*-

import os
import sys
path = os.path.dirname(__file__)
sys.path.insert(0, path)
from v4.restFuture.HttpAPI import *  # NOQA
from v4.wsSpot.WSAPI import *  # NOQA
from v4.restSpot.HttpAPI import *  # NOQA
