from setuptools import setup, find_packages

setup(
    name="avatar_sync_lip",
    version="1.1.0",
    author="ChiChieh Huang",
    author_email="cch.chihchieh@gmail.com",
    description="A package for generating videos using HeyGen API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wsxqaza12/avatar_sync_lip",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
