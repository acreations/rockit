import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "rockit",
    version = "0.1",
    packages = find_packages(),
    license = "MIT License",
    author = "Aaron Wong",
    author_email = "aaron.wong@acreations.se",
    description = "Rock it at home with automation",
    url = "https://github.com/acreations/rockit",
    include_package_data = True
)