import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="combinations-wmacevoy", # Replace with your own username
    version="1.0.0",
    author="Warren MacEvoy",
    author_email="wmacevoy@gmail.com",
    descripftion="Generate and index combinations"
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wmacevoy/combinations",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
