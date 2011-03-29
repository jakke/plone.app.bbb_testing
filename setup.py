from setuptools import setup, find_packages
import os

version = '1.0a1'

setup(name='plone.app.bbb_testing',
      version=version,
      description="PloneTestCase  backward-compatible helper classes "
        "for plone.app.testing",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Godefroid Chapelle',
      author_email='gotcha@bubblenet.be',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.app.testing',
      ],
      entry_points="""
      """,
      )
