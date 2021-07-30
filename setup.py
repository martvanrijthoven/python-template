from setuptools import setup

package_name = package

setup(
    name=package_name,
    version='0.0.1',
    author='Mart van Rijthoven',
    author_email='mart.vanrijthoven@gmail.com',
    packages=[package_name],
    url=f'http://pypi.python.org/pypi/{package_name}/',
    license='LICENSE.txt',
    long_description='desc',
)
