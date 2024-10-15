from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    HYPHEN_E_DOT = "-e ."
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    author="Uma",
    author_email="umaselvaraj257@gmail.com",
    install_requires=get_requirements("requirements.txt"),
)