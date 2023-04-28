"""
Setup script for openalex pkg.
"""
from setuptools import setup

setup(
    name="s23p",
    version="0.0.1",
    description="s23p",
    maintainer="Ahmad Ali",
    maintainer_email="asali@andrew.cmu.edu",
    license="MIT",
    packages=["s23p"],
    entry_points={'console_scripts': ['pkgee = s23p.main:main']},
    long_description="""Project for openalex""",
)
