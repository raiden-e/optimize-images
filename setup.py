# encoding: utf-8
import os
import sys

from setuptools import setup, find_packages

used = sys.version_info
required = (3, 7)

if used[:2] < required:
    sys.stderr.write("Unsupported Python version: %s.%s. "
                     "Python 3.6 or later is required." % (sys.version_info.major,
                                                           sys.version_info.minor))
    sys.exit(1)

short_desc = "A command-line interface (CLI) utility written in pure Python " \
             "to help you reduce the file size of images."


def read_readme(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


setup(name='optimize-images',
      version=__import__('optimize_images').__version__,
      description=short_desc,
      author="Victor Domingos",
      packages=find_packages(),
      include_package_data=False,
      long_description=read_readme('README.md'),  # for PyPI
      long_description_content_type="text/markdown",
      license='MIT',
      url='https://github.com/raiden-e/optimize-images',
      project_urls={
          'Documentation': 'https://github.com/raiden-e/optimize-images/docs/docs_EN.md',
          'Source': 'https://github.com/raiden-e/optimize-images',
          'Bug Reports': 'https://github.com/raiden-e/optimize-images/issues',
      },
      python_requires='>=3.7',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Operating System :: iOS',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: Unix',
          'Operating System :: POSIX :: Linux ',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Utilities',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion',
      ],

      keywords='python3 seo web',

      install_requires=[
          'piexif==1.1.3',
      ],

      entry_points={
          'console_scripts': ['optimize-images = optimize_images.optimize_images:main']
      },
      )
