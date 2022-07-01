# -*- python -*-

python_sources()

python_tests(
    name="tests",
    dependencies=["//:build_root"],
)

python_distribution(
    name="dist",
    dependencies=[":underpants"],
    repositories=["@pypi"],
    provides=python_artifact(
        name="underpants",
        version="0.2.0",
        description="Leverage the Rules Engine from the Pants Build System as a library.",
        license="MIT",
        project_urls={
            "Documentation": "https://github.com/kaos/underpants/wiki",
            "Source": "https://github.com/kaos/underpants",
            "Tracker": "https://github.com/kaos/underpants/issues",
        },
        long_description_content_type="text/markdown",
        long_description="""
`underpants` - Or, using Pants as an embedded rule engine
=========================================================

For Pantsbuild version: 2.12.0

DISCLAIMER: This is not in any way to show how to use Pants, or recommended patterns of
use. Provided here AS-IS. No gurantees of any kind, as this may break with any future release of
Pants.

This is a toy POC testing out the feasability of using the [Pants Build
System](https://www.pantsbuild.org/) as a rule engine in your Python application.

""",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries",
        ],
    ),
)
