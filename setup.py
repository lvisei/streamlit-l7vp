import setuptools
from pathlib import Path

parent_dir = Path(__file__).resolve().parent

setuptools.setup(
    name="streamlit-l7vp",
    version="0.0.1",
    author="lvisei",
    author_email="yunji.me@outlook.com",
    description="Streamlit Component for rendering L7VP maps",
    long_description=parent_dir.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/lvisei/streamlit-l7vp",
    license="Apache-2.0",
    packages=setuptools.find_packages(exclude=("tests", "docs", "examples")),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=parent_dir.joinpath("requirements.txt").read_text().splitlines(),
)