from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as fh:
    install_requires = fh.read().splitlines()

print(install_requires)

setup(
    name='sp800_22_tests',
    url='https://github.com/luukbox/sp800_22_tests',
    version='0.0.1',
    description='A python implementation of the SP800-22 Rev 1a PRNG test suite.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    packages=['sp800_22_tests'],
    platforms=['any'],
)
