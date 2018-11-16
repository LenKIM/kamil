# Goal : 패키지와 배포관리

import io

from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
        return readme


setup(name='kamil',
      version='0.1',
      description='to make labeling tool',
      long_description=long_description(),
      url='http://github.com/LenKIM/kamill',
      author='Lenkim',
      packages=find_packages())
