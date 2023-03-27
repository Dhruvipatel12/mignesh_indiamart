from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mignesh_indiamart/__init__.py
from mignesh_indiamart import __version__ as version

setup(
	name="mignesh_indiamart",
	version=version,
	description="mignesh_indiamart ",
	author="Dhruvi",
	author_email="dhruvikaneriya52@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
