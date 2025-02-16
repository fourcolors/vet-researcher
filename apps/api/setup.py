from setuptools import find_packages, setup

setup(
    name="api",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.109.2",
        "uvicorn>=0.27.1",
        "python-dotenv>=1.0.0",
        "pydantic>=2.6.1",
    ],
) 