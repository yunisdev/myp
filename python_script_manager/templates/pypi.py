def pypi_oninit():
    print("Thanks for using pypi template!!!")


pypi = {
    "body": {
        "scripts": {
            "predeploy": {
                "command": "python setup.py sdist bdist_wheel",
                "description": "Build package"
            },
            "deploy": {
                "command": "python -m twine upload --skip-existing --repository-url https://upload.pypi.org/legacy/ dist/*",
                "description": "Upload to PYPI"
            }
        }
    },
    "oninit": pypi_oninit
}
