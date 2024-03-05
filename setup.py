from setuptools import setup, find_packages

setup(
    name='stakepy',
    version='0.1',
    packages=find_packages(),
    description='The intention of the package as of right now is to display the stake quantity of your EVM wallet for all chains.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='byte-my-code',
    author_email='bytemycode.sup@gmail.com',
    url='https://github.com/lachenlama/stakepy',
    license='LICENSE',
    install_requires=[
        'web3>=6.15.1',
    ],
    entry_points={
        'console_scripts': [
            'stakepy=script.py:main',
        ],
    },
)