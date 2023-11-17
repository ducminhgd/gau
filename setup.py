from setuptools import setup, find_packages
from gau.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="gau",
    version=__version__,
    author="Gia Duong Duc Minh",
    author_email="giaduongducminh@gmail.com",
    description="A Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ducminhgd/gau",
    packages=find_packages(),
    package_dir={
        'gau': 'gau',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    tests_require=['pytest'],
)
