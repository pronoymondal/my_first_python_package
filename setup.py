from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='my_first_python_package',
    version=__version__,

    url='https://github.com/pronoymondal/my_first_python_package',
    author='Pronoy Kanti Mondal',
    author_email='pronoykanti@mail.ru',

    packages=find_packages(),
)


