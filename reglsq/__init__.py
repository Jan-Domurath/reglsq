"""reglsq"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("reglsq")
except PackageNotFoundError:
    try:
        from setuptools_scm import get_version
        __version__ = get_version(root='..', relative_to=__file__)
    except (ImportError, LookupError):
        __version__ = "unknown"
