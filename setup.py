import os
import sys
import versioneer
from setuptools import setup
from setuptools.command.test import test as TestCommand


rootpath = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--verbose', '--doctest-modules',
                          '--ignore', 'setup.py']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def read(*parts):
    return open(os.path.join(rootpath, *parts), 'r').read()


email = "ocefpaf@gmail.com"
maintainer = "Filipe Fernandes"
authors = ['Rich Signell', 'Filipe Fernandes']

LICENSE = read('LICENSE.txt')
long_description = '{}\n{}'.format(read('README.rst'), read('CHANGES.txt'))


# Dependencies.
with open('requirements.txt') as f:
    tests_require = f.readlines()
install_requires = [t.strip() for t in tests_require]


setup(name='utilities',
      version=versioneer.get_version(),
      packages=['utilities'],
      package_data={'': ['data/*.csv', 'data/*.css']},
      cmdclass=dict(test=PyTest),
      license=LICENSE,
      long_description=long_description,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Education',
                   'Topic :: Scientific/Engineering'],
      description='Misc utilities functions for IOOS/SECOORA',
      author=authors,
      author_email=email,
      maintainer='Filipe Fernandes',
      maintainer_email=email,
      url='https://github.com/pyoceans/utilities/releases',
      platforms='any',
      keywords=['oceanography', 'data analysis'],
      install_requires=install_requires,
      tests_require='pytest',
      zip_safe=False,
      )
