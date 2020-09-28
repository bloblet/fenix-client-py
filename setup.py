import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fenix-python-bloblet", # Replace with your own username
    version="6.1",
    author="bloblet",
    author_email="blobletdev@gmail.com",
    description="Official Fenix client for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bloblet/fenix-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)