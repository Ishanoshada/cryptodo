from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cryptodo",
    version="3.3",
    author="k.a.ishan oshada",
    author_email="ic31908@gmail.com",
    description="A Python library for text encryption and decryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/cryptodo",
    packages=find_packages(),
    keywords=['text encryption', 'text decryption', 'Caesar cipher', 'substitution cipher', 'rail fence cipher'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
