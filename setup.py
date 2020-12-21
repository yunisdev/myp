import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PACKAGE_NAME",
    version="VERSION",
    author="AUTHOR",
    author_email="AUTHOR_EMAIL",
    description="DESCRIPTION",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="GITHUB_URL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: LICENSE_NAME",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)