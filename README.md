# python sample application

a python calculator made for testing the use of SonarQube's Sonar scanner's ability to scan python projects

The idea is to get test results and code coverage into SonarQube.

According to the documentation of the Sonar Scanner for Python, the last three commands should do it:

```bash
python3 -m pytest
python3 -m coverage erase
python3 -m coverage run Calculator.py --branch
python3 -m coverage xml -i

```