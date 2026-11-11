from setuptools import setup, find_packages

setup(
    name="pyzoren",
    version="1.0.0",
    description="Official Python SDK and native runtime bridge for the Zoren Programming Language",
    long_description=open("docs/PYTHON_TO_ZOREN_GUIDE.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Zoren Language Authors",
    url="https://github.com/zoren-lang/zoren",
    packages=find_packages(include=["pyzoren", "pyzoren.*"]),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
    ],
    entry_points={
        "console_scripts": [
            "pyzoren = pyzoren.cli:main",
        ],
    },
)
