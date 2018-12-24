from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='tvsleep',
      version='0.4',
      description='put your computer to sleep after a delay',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/tristanmkernan/tvsleep',
      author='tristank',
      author_email='tristanmkernan@gmail.com',
      license='gplv3',
      packages=['tvsleep'],
      scripts=['bin/tvsleep'],
      include_package_data=True,
      zip_safe=False)
