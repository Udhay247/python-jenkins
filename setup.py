import setuptools

setuptools.setup(
    name="python-jenkins", # Replace with your own project/artifact name
    version="latest",
    author="Udhay",
    author_email="udhaya.kumar@247.ai",
    description="A small example package (Pyjenkins)",
    long_description_content_type="text/markdown",
    url='https://github.com/Udhay247/python-jenkins.git',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
)

# from setuptools import find_packages, setup
# from pyassemble.package import Package
#
# setup(
#     name='pyjenkins',
#     author="udhaya",
#     version='1.0',
#     description='assemble project with all dependencies for install offline',
#     long_description=open('README.md').read(),
#     classifiers=[
#         'Programming Language :: Python :: 3.6',
#         'Intended Audience :: Developers',
#       ],
#     keywords='assembly pyassemble dist offline install dependencies',
#     url='https://github.home.247-inc.net/python-service-template/PyCICD_template.git',
#     license='Apache License 2.0',
#     packages=find_packages(),
#     include_package_data=True,
#     install_requires=['Flask==1.1.1','pandas','numpy'],     cmdclass={
#         "package": Package
#     }
# )