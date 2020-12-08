import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="service",
    version="1.0.0",
    url="http://flask.pocoo.org/docs/tutorial/",
    license="BSD",
    maintainer="[24]7.ai",
    maintainer_email="neelesh.sa@247.ai",
    description="The basic skeleton app using Flask",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    #install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)
