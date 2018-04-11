"""Setup file for color-coder."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="color-coder",
    version="0.1",
    description="Represent a vector with a color.",
    license="BSD",
    author="Mikhail Pak <mikhail.pak@tum.de>",
    packages=["colorcoder"],
    install_requires=["numpy"]
    )
