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
        'autoenv',
        'bs4',
        'flask',
        'python-dotenv',
        'tweepy',
    ],
    entry_points='''
        [console_scripts]
        server=app.server:main
        spider=app.spider:main
        stream=app.stream:stream
    ''',
)
