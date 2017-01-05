from setuptools import setup

setup(
    name='worldLeaders',
    version='0.1.0',
    author='Oliver Plunkett',
    author_email='otplunkett@gmail.com',
    packages=['app'],
    license='MIT',
    long_description=open('README.txt').read(),
    install_requires=[
        'tweepy',
        'python-dotenv',
        'bs4'
    ],
    entry_points='''
        [console_scripts]
        stream=app.stream:main
        scrape=app.state_leaders_spider:main
    ''',
)
