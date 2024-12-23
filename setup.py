from setuptools import setup, find_packages

setup(
    name="djcli_github",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["djcli_github"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "djcli_github=djcli_github:main",
        ],
    },

    description="A Django command-line tool for simplifying manage.py commands.",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/djcli",  # Replace with your repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
