FROM python:3.9-buster

# Test File
ARG TESTFILE
ENV BEHAVE_TEST = ${TESTFILE}


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

RUN ls -l features/
RUN echo ${BEHAVE_TEST}

RUN cd features && behave -i $BEHAVE_TEST.feature 
