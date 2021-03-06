#
#   Copyright 2013 by Arnold Krille <arnold@arnoldarts.de>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup, find_packages

setup(
    name="workout",
    version="0.2.7",
    description="Store and display workout-data from FIT-files in mezzanine.",
    author="Arnold Krille",
    author_email="arnold@arnoldarts.de",
    url="http://github.com/kampfschlaefer/mezzanine-workout",
    license=open('LICENSE', 'r').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['fitparse==0.0.1-dev', 'mezzanine>=3.0,<3.1'],
    dependency_links=['git+https://github.com/kampfschlaefer/python-fitparse.git@ng#egg=fitparse-0.0.1-dev'],
)
