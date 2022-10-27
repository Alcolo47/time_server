#!/usr/bin/env python
import os
import re
from pathlib import Path

from setuptools import find_packages, setup

os.chdir(Path(__file__).parent)

setup(name='time_server',
      version='1.0',
      description='Time server',
      author='Stéphane Bastidon',
      author_email='stephane.bastidon@mfi.fr',
      url='https://',
      packages=find_packages(),
      python_requires='>=3.6',
      install_requires=[re.sub(r'(==.*)$', lambda m: f'({m.group(1)})', l) for l in open('requirements.txt').read().splitlines()],
      entry_points={
            "console_scripts": ["time-server = time_server.main:main"],
      }
      )
