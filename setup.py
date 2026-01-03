"""
Setup script for RawanAI package.
"""
from setuptools import setup, find_packages


def read_requirements(filename):
    """Read requirements from file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f 
                if line.strip() and not line.startswith('#') and not line.startswith('-r')]


setup(
    name="rawanai",
    version="1.0.0",
    author="Ahmed bin Mohammed bin Jum'an bin Mubarak Al-Dosari",
    description="RawanAI - Your Secretary: AI chatbot with Rawan's personality",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jokr68/RawanAI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements('requirements.txt'),
    extras_require={
        'dev': read_requirements('requirements-dev.txt'),
    },
    entry_points={
        'console_scripts': [
            'rawanai=app:main',
        ],
    },
)
