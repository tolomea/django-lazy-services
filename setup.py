import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-lazy-services",
    version="0.0.1",
    author="Gordon Wrigley",
    author_email="gordon.wrigley@gmail.com",
    description="A helper for switching between test and production versions of a service module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tolomea/django-lazy-services",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
