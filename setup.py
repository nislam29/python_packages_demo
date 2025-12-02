# Think of this as the instruction manual for our package. It contains
# metadata about our package (like its name and version) and lists
# its dependencies. This file is essential for making our package
# installable via pip.

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="my_package",
    version="0.1.0",
    include_package_data=True,
    python_requires=">=3.11",
    pacakges=find_packages(),
    setup_requires=["setuptools-git-versioning"],
    install_requires=requirements,
    author="Nurul ISLAM",
    author_email="nislam@bandsintown.com",
    description="A sample python package to check if it works via github packages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    version_config={"dirty_template": "{tag}"},
)
