FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python setup.py install

# Uncomment once we figure out what our entrypoint is
#CMD [ "python", "./your-daemon-or-script.py" ]
