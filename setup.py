from setuptools import setup, find_packages

setup(
    name="nfcreaders",
    version="0.1",
    author="yukiha-Fuyuno",
    packages=find_packages(),
    install_requires=["nfcpy"],
    include_package_data=True,
)