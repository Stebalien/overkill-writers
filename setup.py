from setuptools import setup, find_packages
setup(
    name = "overkill-extra-writers",
    version = "0.1",
    install_requires=["overkill"],
    packages = find_packages(),
    namespace_packages = ["overkill", "overkill.extra"],
    author = "Steven Allen",
    author_email = "steven@stebalien.com",
    description = "Common data writers for overkill.",
    license = "GPL3",
    url = "http://stebalien.com"
)
