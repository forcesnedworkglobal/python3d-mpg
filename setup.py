import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python3d-mpg",  # Replace with your own username
    version="0.0.1",
    author="Dennis Satia",
    author_email="acloudbank@gmail.com",
    description="Python MPG(Mastercard Payment Gateway) package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/forcesnedworkglobal/python3d-mpg",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Mastercard Visa Payment Gateway",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
