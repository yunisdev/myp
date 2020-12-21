import setuptools
from python_script_manager import const

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-script-manager",
    version=const.version,
    author="YunisDEV",
    author_email="yunisdev.04@gmail.com",
    description="Run scripts easily...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YunisDEV/python-script-manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        psm=python_script_manager.__main__:main
    ''',
)