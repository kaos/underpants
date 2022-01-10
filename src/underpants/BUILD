# -*- python -*-

python_sources()

python_tests(
    name="tests",
    dependencies=["//:build_root"],
)

python_distribution(
    name="dist",
    provides=python_artifact(
        name="underpants",
        version="0.1.0",
        description="Leverage the Rules Engine from the Pants Build System as a library.",
        license="MIT",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Topic :: Software Development :: Libraries",
        ],
        project_urls={
            "Documentation": "https://github.com/kaos/underpants/wiki",
            "Source": "https://github.com/kaos/underpants",
            "Tracker": "https://github.com/kaos/underpants/issues",
        },
    ),
    repositories=["@pypi"],
)
