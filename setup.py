from setuptools import setup

setup(
    name="subdomain_scanner",
    version="1.0.0",
    py_modules=["subdomain_scanner","utils"],
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "subdomain-scanner = subdomain_scanner:main"
        ]
    },
    author="Your Name",
    description="Fetch subdomains (Wayback, crt.sh, VT) and check for 200 OK",
    url="https://github.com/YourUser/subdomain-scanner",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
