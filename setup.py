from setuptools import setup
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='indexedlines',
    version=get_version('src', 'indexedlines.py'),
    description='A convenience list-like object that allows random access to'
                'lines of a text file.',
    long_description=read('README.rst'),
    url='https://github.com/luismsgomes/indexedlines',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='convenience',
    install_requires=[
        'openfile',
    ],
    package_dir={'': 'src'},
    py_modules=['indexedlines'],
)
