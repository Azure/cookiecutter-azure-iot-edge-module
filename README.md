# Cookiecutter Template for Azure IoT Edge Python Module

`cookiecutter-azure-iot-edge-module` creates a base template to start a new Azure IoT Edge Python module

## Prerequisites
Install [Cookiecutter](https://github.com/audreyr/cookiecutter):
```
$ pip install -U cookiecutter
```

## Usage
```
$ cookiecutter https://github.com/Azure/cookiecutter-azure-iot-edge-module --checkout master
```
and follow the interactive prompts.

If you prefer one-liner:
```
$ cookiecutter --no-input https://github.com/Azure/cookiecutter-azure-iot-edge-module module_name=<module_name> image_repository=<image_repository> --checkout master
```

For example:
```
$ cookiecutter --no-input https://github.com/Azure/cookiecutter-azure-iot-edge-module module_name=filterModule image_repository=localhost:5000/filtermodule --checkout master
```

## Documentation
* [Develop and deploy a Python IoT Edge module to your simulated device](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-python-module)
* [Azure IoT Edge](https://docs.microsoft.com/en-us/azure/iot-edge/)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
