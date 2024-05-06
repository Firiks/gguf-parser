from setuptools import setup, find_packages

setup(
    name="gguf-parser",
    version="0.1.0",
    description="A parser for GGUF files",
    author="Hiromichi Goto",
    author_email="goto@suzuca.ai",
    url="https://github.com/hirox/gguf-parser",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
