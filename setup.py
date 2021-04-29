import setuptools
from python_script_manager import PSMReader

with open("README.md","r") as fh:
    long_description = fh.read()

psm = PSMReader('psm.json')

setuptools.setup(
    name=psm.get_data("name"),
    version=psm.get_data("version"),
    author=psm.get_data("author"),
    author_email=psm.get_data("author_email"),
    description=psm.get_data("description"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=psm.get_data("url"),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Natural Language :: English"
    ],
    install_requires=psm.get_dependencies("prod"),
    setup_requires=psm.get_dependencies("prod"),
    python_requires='>=3.6'
)