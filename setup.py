from distutils.core import setup


setup(name='microdrop_utility',
      version='0.0.12',
      description='Utility functions and classes for MicroDrop, which might '
      'be potentially useful in other projects.',
      keywords='microdrop dropbot utility',
      author='Christian Fobel and Ryan Fobel',
      author_email='christian@fobel.net and ryan@fobel.net',
      url='http://github.com/cfobel/microdrop_utility.git',
      license='GPL',
      packages=['microdrop_utility', 'microdrop_utility.gui',
                'microdrop_utility.tests'],
      install_requires=['git_helpers'])
