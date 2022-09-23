# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
    with open('README.md', 'r') as f:
        return f.read()


install_requires = [
    'pandas',
    'tzlocal',
    'requests',
    'simplejson',
    'tqdm',
    'tables',
    'protobuf==3.18.3',
]

extra_require = {
    'test': ['pytest'],
    'doc': ['sphinx', 'pydata_sphinx_theme'],
}


def set_entry_points():
    r = {}
    r['console_scripts'] = [
        'pyarchappl-get=archappl.scripts.get:main',
    ]
    return r


setup(
    name='pyarchappl',
    version='0.10.4',
    description='Python interface to Archiver Appliance',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/archman/pyarchappl",
    author='Tong Zhang',
    author_email='zhangt@frib.msu.edu',
    packages=[
        'archappl.admin', 'archappl.data', 'archappl.data.pb',
        'archappl.client', 'archappl.contrib', 'archappl.scripts', 'archappl'
    ],
    package_dir={
        'archappl.admin': 'main/mgmt',
        'archappl.data': 'main/data',
        'archappl.data.pb': 'main/data/pb',
        'archappl.client': 'main/client',
        'archappl.contrib': 'main/contrib',
        'archappl.scripts': 'main/scripts',
        'archappl': 'main'
    },
    entry_points=set_entry_points(),
    install_requires=install_requires,
    extra_require=extra_require,
    license='GPL3+',
    keywords="Archiver EPICS CA PVA",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
