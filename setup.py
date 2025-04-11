from setuptools import setup

setup(
    name="blackjack-cli",
    version="0.1.0",
    py_modules=["bj"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bj = bj:main",
        ],
    },
    author="Ethan Vo Tran",
    description="A terminal-based Blackjack trainer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
