import json
import logging
import os
import pytest
import shutil

root_dir = os.getcwd()
module_name = "iotedgeFilterModule"
file_list = ["requirements.txt", "module.json", "main.py", ".gitignore",
             "Dockerfile.arm32v7", "Dockerfile.arm32v7.debug",
             "Dockerfile.amd64", "Dockerfile.amd64.debug",
             "Dockerfile.arm64v8", "Dockerfile.arm64v8.debug"]
image_repository = "localhost:5000/" + module_name


@pytest.fixture(scope="module")
def test_install_scaffold(request):
    installmodulecommand = "cookiecutter --no-input \"" + root_dir + "\" module_name=" + \
        module_name + " image_repository=" + image_repository
    print("Cookiecutter execution command: " + installmodulecommand)
    with os.popen(installmodulecommand) as pipe:
        pipe.readlines()
    yield test_install_scaffold
    pipe.close()
    shutil.rmtree(os.path.join(root_dir, module_name))


def test_check_file_exist(test_install_scaffold):
    for file_name in file_list:
        file_path = os.path.join(root_dir, module_name, file_name)
        print("Check file: " + file_path)
        assert os.path.exists(file_path)


def test_check_module_json_content():
    module_file_path = os.path.join(root_dir, module_name, "module.json")
    with open(module_file_path) as module_file:
        module_file_content = json.load(module_file)

    assert image_repository == module_file_content["image"]["repository"]
