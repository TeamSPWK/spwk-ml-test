from setuptools import setup, find_packages

setup_requires = [
    "numpy"
]

install_requires = [
    "shapely==1.7.1",
    "matplotlib==3.2.1"
]
setup(
    name = "spwkml",
    version = "0.0.0",
    author= "iglee",
    author_email = "iglee@spacewalk.tech",
    description = "Tests for spacewalk ML team applicants",
    packages = find_packages(),
    url="https://github.com/TeamSPWK/spwk-ml-test",
    install_requires = install_requires
)
