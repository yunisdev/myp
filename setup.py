import setuptools
from python_script_manager import PSMReader

with open("README.md","r") as fh:
    long_description = fh.read()

psm = PSMReader('psm.json')

setuptools.setup(
    name=psm.get_name(),
    version=psm.get_version(),
    author=psm.get_author(),
    author_email=psm.get_author_email(),
    description=psm.get_description(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=psm.get_url(),
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