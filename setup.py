# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
LONG_DESCRIPTION = ''

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache 2.0',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Telepenin Nikolay",
    author_email="telepenin.nikolay@gmail.com",
    maintainer='Telepenin Nikolay',
    maintainer_email="telepenin.nikolay@gmail.com",
    name='django_example',
    version='0.1',
    description='A Django example for PiterPy conference',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/prefer/django_example',
    license='Apache 2.0',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django==1.9.5',
    ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False
)
