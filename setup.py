"""
Copyright 2015 Jorgen Maas <jorgen.maas@gmail.com>
This file is part of koan.
Koan is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.
Zenossctl is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with zenossctl. If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

setup(
    packages=["koan"],
    scripts=["bin/koan", "bin/cobbler-register"],
)
