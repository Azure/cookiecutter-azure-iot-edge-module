import pytest

class TestIoTEdgeModule():
    def test_RequiredFileExists(self):
        print(self.__class__)
        assert 1 == 1

    def test_RequiredFileExists2(self):
        print(self.__class__)
        assert 1 == 1

if __name__ == '__main__':
    iotEdgeModule=TestIoTEdgeModule()
    iotEdgeModule.test_RequiredFileExists()
    iotEdgeModule.test_RequiredFileExists2()