import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="app_pkg", # Replace with your own username
    version="0.0.1",
    author="dlobe",
    author_email="author@example.com",
    description="A small flask package",
    long_description="A small flask package",
    long_description_content_type="text/markdown",
    url="https://github.com/dlobe/density.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
