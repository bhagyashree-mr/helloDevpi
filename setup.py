from setuptools import setup

setup(
    name='helloDevpi',
    version='0.1',
    py_modules=['hello'],
    entry_points={
        'console_scripts': [
            'hello_devpi = hello:main',
        ],
    }
)
