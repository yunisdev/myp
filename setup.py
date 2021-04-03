import setuptools
from python_script_manager.package import PSMReader

with open("README.md","r") as fh:
    long_description = fh.read()

psm = PSMReader('psm.json')

# def parse_requirements(filename):
#     """ load requirements from a pip requirements file """
#     lineiter = (line.strip() for line in open(filename))
#     return [line for line in lineiter if line and not line.startswith("#")]
# reqs = parse_requirements('requirements.txt')

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
    # install_requires=reqs,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Natural Language :: English"
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        psm=python_script_manager.__main__:main
    ''',
)