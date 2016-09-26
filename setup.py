from setuptools import setup, find_packages

setup(
    name='fin',
    version="0.0.1",
    author='Kevin Tandean',
    packages=find_packages(),
    install_requires=['docopt'],
    entry_points={
        'console_scripts': [
            "fin = fin.controller:main"
        ]
    }
)
