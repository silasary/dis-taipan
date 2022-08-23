from pathlib import Path

from setuptools import find_packages, setup

requirements = [
    "naff>=1.8.1",
    "sentry-sdk"
]

setup(
    name="dis-taipan",
    description="A handful of naff extensions that I want to use in most of my bots.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Silasary",
    url="https://github.com/silasary/dis-taipan",
    version="0.3.0",
    packages=find_packages(exclude='tests'),
    package_data={"dis_taipan": ["py.typed", "*.pyi", "**/*.pyi"]},
    python_requires=">=3.10",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
