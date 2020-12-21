## Step 1

Create virtual environment and install dependencies

```bash
python3 -m venv venv
pip install twine setuptools wheel
```

## Step 2

Create build

```bash
python setup.py sdist bdist_wheel
```

## Step 3

Publish to pip

```bash
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

You will need a pypi account to publish your package.
If you have not create one at <a href="https://pypi.org/account/register/">pypi.org</a>
