from setuptools import find_packages ,setup

from typing import List


def get_requirements()->list[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
    
setup(
 name ="sensor",
 version= "0.0.01",
 author="sudhir kumar",
 author_email ="sudhirkmr40@gmail.com",
 packages = find_packages(),
 install_require =get_requirements(),
)