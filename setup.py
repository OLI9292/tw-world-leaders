from setuptools import setup

setup(
    name='t-w',
    version='0.1.0',
    packages=['app'],
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
    install_requires=['tweepy'],
    entry_points={
        'console_scripts': [
    		'app = app.__main__:main'
        ]
     },
)
