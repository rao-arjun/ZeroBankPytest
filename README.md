# ZeroBankPytest
Python Selenium automation framework - POM, pytest, unittest
Python Selenium project with pytest and unittest framework

Pre requisite:

System should have the chrome and firefox webdrivers installed and the PATH env variable to be set with the location of installation
Python (> 3.6) should be installed on the system and IDE such as Pycharm or Eclipse should have the interpreter set to installation of Python and the run configurations for Pytest and Python unit test to be present.
Apart from execution from IDE, this can be executed either in the form of Python pytest or Python unittest from command line

After cloning the repository, go to the project path in the command prompt and execute the command 
pipenv install 
The above command installs all the python packages and dependencies.

To execute as pytest, the following commands to be used: 
cd pytestpackage 
pytest -v -s --html=../reports/pytest_reports_ZeroBankApp.html Test_ZeroBank_pytest.py

To execute as python unittest, the following command to be used: 
python -m unittest pythonunittests.ZeroBankUnitTests
