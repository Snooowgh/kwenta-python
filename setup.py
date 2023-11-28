from setuptools import setup, find_packages

setup(
    name="kwenta",
    version="1.2.0",
    description="Python SDK for Kwenta",
    long_description="Python SDK for Kwenta",
    author="Kwenta DAO",
    packages=[
        "kwenta",
        "kwenta.alerts",
        "kwenta.cli",
        "kwenta.contracts",
        "kwenta.contracts.json",
        "kwenta.pyth",
        "kwenta.queries",
    ],
    install_requires=["numpy", "pandas", "requests", "web3>=6.0.0", "gql",
                      "web3_multicall@git+https://github.com/Snooowgh/py_web3_multicall.git@master"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    package_data={"kwenta": ["json/*"]},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "kwenta = kwenta.cli.kwenta_cli:kwenta_cli",
        ],
    },
)
