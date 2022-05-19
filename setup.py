import setuptools,find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="kwikeda",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Khushal Naphade",                     # Full name of the author
    author_email="khushal27@gmail.com",                     # Full name of the author
    description="This is package to do quick EDA of any given data set",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    install_requires=['pandas','numpy']                     # Install other dependencies if any
    packages=find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Development status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]                                      # Information to filter the project on PyPi website
)
