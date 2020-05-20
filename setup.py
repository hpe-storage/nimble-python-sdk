#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#

import setuptools

__version__ = '1.0.0'

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as requirements:
    install_requires = requirements.readlines()

setuptools.setup(
    name="nimble-sdk",
    version=__version__,
    author="Suneethkumar Byadarahalli",
    author_email="nimble-dcs-storage-automation-eng@hpe.com",
    maintainer="Suneethkumar Byadarahalli, Alok Ranjan, George Costea",
    keywords=["hpe", "nimble", "python", "sdk", "rest", "storage"],
    requires=['requests'],
    description="The Nimble Python SDK (client library) is a utility that can be leveraged to manage HPE Nimble Storage arrays.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="Apache License, Version 2.0",
    url="https://github.com/hpe-storage/nimble-python-sdk",
    project_urls={
        "Documentation": "https://scod.hpedev.io/storage_automation/nimble_python_sdk/index.html",
        "Code": "https://github.com/hpe-storage/nimble-python-sdk",
        "Issue tracker": "https://github.com/hpe-storage/nimble-python-sdk/issues",
    },
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
