# -*- coding: utf-8 -*-
"""Installer for the plone.tcp package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='plone.tcp',
    version='1.0a1',
    description="A TCP Add-on",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='AndyLi',
    author_email='andyofl1024@gmail.com',
    url='https://github.com/collective/plone.tcp',
    project_urls={
        'PyPI': 'https://pypi.org/project/plone.tcp/',
        'Source': 'https://github.com/collective/plone.tcp',
        'Tracker': 'https://github.com/collective/plone.tcp/issues',
        # 'Documentation': 'https://plone.tcp.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['plone'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
	'plone.dexterity',
	'plone.supermodel',
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = plone.tcp.locales.update:update_locale
    """,
)
