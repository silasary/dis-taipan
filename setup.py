from pathlib import Path

from setuptools import find_packages
from setuptools import setup

requirements = [
    'dis-snek>=6.0',
    'sentry-sdk',
]

setup(
    name="dis-taipan",
    description="A handful of dis-snek scales that I want to use in most of my bots.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Silasary",
    url="https://github.com/silasary/dis-taipan",
    version="0.2.2",
    packages=find_packages(),
    package_data={"dis_taipan": ["py.typed", "*.pyi", "**/*.pyi"]},
    
    python_requires=">=3.10",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)