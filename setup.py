from setuptools import setup
import astar

NAME = 'astar'
DESCRIPTION = "Astar: An unified programming language parser & analyse AST tool for Souece Code Analysis.  "

AUTHOR = 'Wakana Hashimoto'
AUTHOR_EMAIL = 'oxwasouxo@gmail.com'
URL = 'https://github.com/xwasoux'

LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/xwasoux/astar.git'
PYTHON_REQUIRES = ">=3.8"

INSTALL_REQUIRES = [
    'anytree',
    'graphviz',
    'pydot',
    'tree_sitter',
]

PACKAGES = [
    'astar'
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
]

setup(
    name=NAME,
    description=DESCRIPTION,
    license=LICENSE,

    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,

    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,

    packages=PACKAGES,
    classifiers=CLASSIFIERS
    )
