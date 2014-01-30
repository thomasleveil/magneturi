from setuptools import setup

setup(
    name='magneturi',
    version='1.0',
    packages=['magneturi'],
    entry_points={
        'console_scripts': [
            'magneturi = magneturi.__main__:main',
        ]},
    url='https://github.com/thomasleveil/magneturi',
    license='WTFPL',
    author='Thomas LÉVEIL',
    author_email='thomasleveil@gmail.com',
    description='generate bittorrent magnet URI from torrent files',
)
