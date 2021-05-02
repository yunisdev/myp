from .django import django
from .blank import blank
from .pypi import pypi
from .flaskmng import flaskmng

templates = {
    "flaskmng":flaskmng,
    "django": django,
    "blank":blank,
    "pypi":pypi
}
