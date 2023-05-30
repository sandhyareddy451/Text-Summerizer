import setuptools
with open("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__ = "0.0.0"

REPO_NAME = "Text-Summerizer"
AUTHOR_USER_NAME = "sandhya"
SRC_REPO="textSummerizer"
AUTHOR_EMAIL = "vemulaa.sandhya51@gmail.com"



setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP app",
    long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        
    "bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
                   
    
    
    
)