FROM python:3.9-buster

# Install firefox
RUN apt-get update
RUN apt-get install firefox-esr -y

# Install
RUN pip install behave
RUN pip install selenium
RUN pip install geckodriver_autoinstaller
RUN pip install python_dotenv

# Copy stuff
COPY . .

RUN behave -i features/TESTFILE.feature -o TESTFILE.report
