from setuptools import setup

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS :: MacOS X",
    "Topic :: Software Development :: Testing",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python :: 3 :: Only",
] + [("Programming Language :: Python :: %s" % x) for x in "3 3.5 3.6 3.7 3.8".split()]

with open("README.rst", "rb") as fd:
    long_description = fd.read().decode("utf-8")

with open("CHANGELOG.rst", "rb") as fd:
    long_description += "\n\n" + fd.read().decode("utf-8")

EXTRAS_REQUIRE = {
    "dev": ["pre-commit", "tox"],
    "testing": ["pytest"],
}


def main():
    setup(
        name="pluggy",
        description="plugin and hook calling mechanisms for python",
        long_description=long_description,
        use_scm_version={"write_to": "src/pluggy/_version.py"},
        setup_requires=["setuptools-scm"],
        license="MIT license",
        platforms=["unix", "linux", "osx", "win32"],
        author="Holger Krekel",
        author_email="holger@merlinux.eu",
        url="https://github.com/pytest-dev/pluggy",
        python_requires=">=3.5",
        install_requires=['importlib-metadata>=0.12;python_version<"3.8"'],
        extras_require=EXTRAS_REQUIRE,
        classifiers=classifiers,
        packages=["pluggy"],
        package_dir={"": "src"},
    )


if __name__ == "__main__":
    main()
