#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 SoloKeys, Inc. <https://solokeys.com/>
#
# This file is part of Solo.
#
# Solo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Solo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Solo.  If not, see <https://www.gnu.org/licenses/>
#
# This code is available under licenses for commercial use.
# Please contact SoloKeys for more information.
#
import sys
from ecdsa import SigningKey, NIST256p

sk = SigningKey.from_pem(open(sys.argv[1]).read())


print('Private key in various formats:')
print()
print([c for c in sk.to_string()])
print()
print(''.join(['%02x' % c for c in sk.to_string()]))
print()
print('"\\x' + '\\x'.join(['%02x' % c for c in sk.to_string()]) + '"')
print()
