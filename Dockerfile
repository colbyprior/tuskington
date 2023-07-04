FROM python:3.9-alpine

COPY src /app/
WORKDIR /app

RUN apk add git

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0744 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
