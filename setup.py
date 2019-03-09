from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    author='Lukas Sebastian Müller',
    author_email='lukassebastianmueller@gmail.com',
    name='sp800_22_tests',
    url='https://github.com/luukbox/sp800_22_tests',
    version='0.0.1',
    description='A python implementation of the SP800-22 Rev 1a PRNG test suite.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['sp800_22_tests'],
    platforms=['any'],
)
