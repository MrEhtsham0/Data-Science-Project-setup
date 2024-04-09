from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path)->List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



project_name = 'Data-Science-Project-setup',
AUTHOR_NAME="MrEhtsham0"

setup(
    name='Data_Science_setup',
    author=AUTHOR_NAME,
    author_email='mr_ehtsham@yahoo.com',
    version='0.0.1',
    packages=find_packages(),
    url=f"https://github.com/{AUTHOR_NAME}/{project_name}",
    license='APACHE',
    description='Data Science Industial Project setup',
    install_requires=get_requirements('requirements.txt'),
)