import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()



__version__= "0.0.0"

REPO_NAME= "Kidney-disease-classification"
AUTHOR_USER_NAME= "Nisha-tk"
SRC_REPO= "cnnClassifier"
AUTTHOR_EMAIL="nisha.333t@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTTHOR_EMAIL,
    description="A small python package for cnn app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },

    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")


)