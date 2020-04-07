#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#

import setuptools

__version__ = '1.0.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as requirements:
        install_requires = requirements.readlines()

setuptools.setup(
    name="nimble-python-sdk",
    version=__version__,
    author="Suneethkumar Byadarahalli",
    author_email="suneethkumar.byadarahalli@hpe.com",
    maintainer="Suneethkumar Byadarahalli, George Costea",
    keywords=["hpe", "nimble", "python", "sdk", "rest", "storage"],
    requires=['requests'],
    description="A Python SDK or Client library for Nimble OS",
    long_description="A Python SDK to interact with the Nimble OS for storage provisioning and data protection.",
    long_description_content_type="text/markdown",
    license="Apache License, Version 2.0",
    url="https://github.com/hpe-storage/nimble-python-sdk",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
)