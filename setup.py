from setuptools import setup, find_packages

setup(
    name='ccwc',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ccwc = main:main'
        ]
    },
    install_requires=[
        # Any dependencies your tool needs
    ],
    test_suite='tests'
)