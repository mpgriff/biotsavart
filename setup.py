from setuptools import setup, find_packages
__version__='0.0.1'
setup(
    name='biotsavart',
    author='Matt Griffiths',
    author_email='mpg@geo.au.dk',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=['numpy', 'matplotlib'],
    version=__version__,
    license='MIT',
    description='generate magnetic fields in free space using biot savart laws',
    python_requires=">=3.8",
)
