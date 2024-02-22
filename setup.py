# hello.py

def main():
    print("Hello, Devpi!")

jenkins@Bhagyashree:/opt/helloDevpi$ cat setup.py
# setup.py

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
