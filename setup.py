"""Barebones setup.py retained for supporting editable_ installs::

    pip install -e .

.. _editable: https://github.com/pypa/packaging-problems/issues/256#issuecomment-504790004

"""
from setuptools import setup
import subprocess

subprocess.run("hg version -v --config extensions.hggit=".split())

setup()
