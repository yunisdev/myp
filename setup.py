"""Setup file for myp"""
import setuptools
from myp import MYPReader

with open("README.md","r") as fh:
    long_description = fh.read()

myp = MYPReader()

requirements = myp.get_dependencies()

setuptools.setup(
    name=myp.get_data("name"),
    version=myp.get_data("version"),
    author=myp.get_data("author"),
    author_email=myp.get_data("author_email"),
    description=myp.get_data("description"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=myp.get_data("url"),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Natural Language :: English"
    ],
    install_requires=requirements,
    setup_requires=requirements,
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        myp=myp.__main__:cli
    ''',
)
