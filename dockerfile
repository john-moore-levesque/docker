FROM python:3.9-buster

// Install firefox
apt-get update
apt-get install firefox

// Install
pip install behave
pip install selenium
pip install geckodriver_autoinstaller
pip install python_dotenv

// Copy stuff
cp -r features/ .

behave -i features/TESTFILE.feature -o TESTFILE.report
