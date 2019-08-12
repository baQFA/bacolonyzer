#!/usr/bin/env python3

from distutils import util
from distutils.core import setup

import setuptools

import recolonyzer

_DESCRIPTION = """\
ReColonyzer is a software to quantify the cell density of bacterial cultures
from timecourse pictures. It uses image analysis tools to determine the fitness
of spotted cultures of bacteria grown on solid agar.
"""


def ensure_scripts(linux_scripts):
    """Creates the proper script names required for each platform
    """

    if util.get_platform()[:3] == "win":
        return linux_scripts + [script + ".bat" for script in linux_scripts]
    return linux_scripts


setup(
    name='recolonyzer',
    version=recolonyzer.__version__,
    description='Analyse timeseries of QFA images',
    author='Judith Bergada',
    author_email='judithbergada@gmail.com',
    url='https://github.com/judithbergada/recolonyzer',
    packages=setuptools.find_packages(),
    long_description=_DESCRIPTION,
    license='MIT',
    scripts=ensure_scripts(['recolonyzer/recolonyzer']),
    python_requires='>3.4, <4',
    install_requires=[
        'numpy>=1.13.0',
        'opencv-python>=4.0.0.21',
        'pandas>=0.21.1',
        'scipy>=1.0.0',
        'tqdm>=4.28.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
)
