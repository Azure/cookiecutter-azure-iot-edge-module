import pytest
import os

root_dir = os.getcwd()
module_name = "filterModule"

@pytest.fixture(scope="module",params=["requirements.txt","module.json","main.py","Dockerfile.arm32v7","Dockerfile.amd64.debug","Dockerfile.amd64",".gitignore"])
def test_CheckFileExists(request):
    exists=os.path.exists(os.path.join(root_dir,module_name,request.param))
    return exists

def test_CheckIoTEdgeModuleExits(test_CheckFileExists):
    if test_CheckFileExists :
        pass
    else:
        raise Exception("IoT Edge Module cannot be found.")