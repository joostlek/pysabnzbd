from setuptools import setup

setup(
    name='pysabnzbd',
    packages=['pysabnzbd'],
    version='1.1.1',
    description='Python wrapper for SABnzbd API',
    author='Jerad Meisner',
    author_email='jerad.meisner@gmail.com',
    url='https://github.com/jeradM/pysabnzbd',
    download_url='https://github.com/jeradM/pysabnzbd/archive/1.1.0.tar.gz',
    keywords=['SABnzbd'],
    install_requires=["aiohttp>=3.6.1,<4.0"],
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
)
