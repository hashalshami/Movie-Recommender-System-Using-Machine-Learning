from setuptools import setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

AUTHOR_NAME = "Hashem Ameen"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version="0.1.0",
    author=AUTHOR_NAME,
    author_email='hashemalshami20@gmail.com',
    description="A simple Python package for a simple web app",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[SRC_REPO],
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)
