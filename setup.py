from setuptools import find_packages, setup
import os


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='optuna-dashboard',
    packages=find_packages(),
    version='0.0.1',
    author='mayank1903',
    description='Repo to understand and provide demo on Optuna Dashboard for hyperparameter tuning',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT'
)