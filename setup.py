import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-scripts",
    version="0.0.1",
    author="YunisDEV",
    author_email="yunisdev.04@gmail.com",
    description="Run scripts easily...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YunisDEV/py-scripts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: LICENSE_NAME",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        py-scripts=py_scripts.__main__:main
    ''',
)