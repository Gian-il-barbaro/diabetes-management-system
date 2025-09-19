from setuptools import setup, find_packages

setup(
    name="diabetes_management_system",
    version="1.0.0",
    author="Generated",
    description="Sistema di gestione pazienti diabetici",
    packages=find_packages(where="src/main/python"),
    package_dir={"": "src/main/python"},
    install_requires=[
        "PyQt5>=5.15.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)