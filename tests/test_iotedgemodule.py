import os
import pytest

root_dir = os.getcwd()
module_name = "iotedgeFilterModule"
file_list = ["requirements.txt", "module.json", "main.py", "Dockerfile.arm32v7",
             "Dockerfile.amd64.debug", "Dockerfile.amd64", ".gitignore"]


@pytest.fixture(scope="module")
def test_install_iotedgemodule(request):
    installmodulecommand = "cookiecutter --no-input https://github.com/Azure/cookiecutter-azure-iot-edge-module module_name=" + \
        module_name + " image_repository=localhost:5000/"+module_name+" --checkout master"
    pipe = os.popen(installmodulecommand)
    yield pipe.readlines()
    pipe.close()


@pytest.fixture(scope="module", params=file_list)
def test_check_file_exist(request):
    exists = os.path.exists(os.path.join(root_dir, module_name, request.param))
    return exists


def test_check_iotedgemodule_exist(test_install_iotedgemodule, test_check_file_exist):
    if not test_check_file_exist:
        raise Exception("IoT Edge Module cannot be found.")
