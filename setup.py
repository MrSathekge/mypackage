import imp
from setuptools import setup, find_packages     #importing from a library called setuptools, we import 2 libraries: setup & find_packages

#we parse in one method that has a lot of arguments

# These are just the features/attributes/specifications of our package
# # that we are required to include when we make it public
setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Explore Data Science Academy example of python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/MrSathekge/myModule.py',
    author='Caron',
    author_email='caronsathekge28@gmail.com'
)





# Now we go to the readme.MD file

