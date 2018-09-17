import json
import logging
import os
import pytest

root_dir = os.getcwd()
module_name = "iotedgeFilterModule"
file_list = ["requirements.txt", "module.json", "main.py", "Dockerfile.arm32v7",
             "Dockerfile.amd64.debug", "Dockerfile.amd64", ".gitignore"]
image_repository="localhost:5000/"+module_name


@pytest.fixture(scope="module")
def test_install_iotedgemodule(request):
    installmodulecommand = "cookiecutter --no-input "+os.environ["BUILD_REPOSITORY_LOCALPATH"]+" module_name=" + \
        module_name + " image_repository="+image_repository
    print("Cookiecutter execution command: "+installmodulecommand)
    pipe = os.popen(installmodulecommand)
    yield pipe.readlines()
    pipe.close()


def test_check_file_exist(test_install_iotedgemodule):
    for file_name in file_list:
        file_path = os.path.join(root_dir, module_name, file_name)
        print("Check file: "+file_path)
        assert os.path.exists(file_path) == True

def test_check_module_json_context():
    module_file_path=os.path.join(root_dir, module_name, "module.json")
    with open(module_file_path) as module_file:
        module_file_content=json.load(module_file)
    
    assert image_repository in module_file_content["image"]["repository"]