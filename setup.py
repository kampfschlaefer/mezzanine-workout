from distutils.core import setup

setup(
    name="workout",
    version="0.1.0",
    description="Store and display workout-data from FIT-files in mezzanine.",
    author="Arnold Krille",
    author_email="arnold@arnoldarts.de",
    url="http://github.com/kampfschlaefer/mezzanine-workout",
    license=open('LICENSE', 'r').read(),
    packages=['workout'],
    install_requires=['fitparse==0.0.1-dev'],
    dependency_links=['git+https://github.com/kampfschlaefer/python-fitparse.git@ng#egg=fitparse-0.0.1-dev'],
)
