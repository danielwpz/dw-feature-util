from setuptools import setup


setup(name='feature-util',
      version='0.1',
      description='Stock feature producers',
      author='Daniel Wang',
      author_email='danielwpz@gmail.com',
      license='MIT',
      packages=['feature_util'],
      install_requires=[
          'datasource',
      ],
      zip_safe=False)
