# -*- python -*-

python_sources()

python_tests(
    name="tests",
    dependencies=["//:build_root"],
)

resources(name="resources", sources=["py.typed"])

python_distribution(
    name="dist",
    dependencies=[":underpants", ":resources"],
    repositories=["@pypi"],
    provides=python_artifact(
        name="underpants",
        version="0.2.4",
        description="Leverage the Rules Engine from the Pants Build System as a library.",
        license="MIT",
        project_urls={
            "Documentation": "https://github.com/kaos/underpants/wiki",
            "Source": "https://github.com/kaos/underpants",
            "Tracker": "https://github.com/kaos/underpants/issues",
        },
        long_description_content_type="text/markdown",
        long_description="""
`underpants` - Or, using Pants as an embedded rules engine
==========================================================

For Pantsbuild version: 2.14.0

DISCLAIMER: This is not in any way to show how to use Pants, or recommended patterns of
use. Provided here AS-IS. No gurantees of any kind, as this may break with any future release of
Pants.

This is a toy POC testing out the feasability of using the [Pants Build
System](https://www.pantsbuild.org/) as a rule engine in your Python application.

The relative narrow Python interpreter constraint of 3.9.* is due to the combination of Pants ICs of
>=3.7,<3.10 and the fact that for ARM based Mac (M1s) only >=3.9 works with Pants.

""",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries",
        ],
    ),
)
