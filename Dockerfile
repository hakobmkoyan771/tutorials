FROM python:3.9.13

ENV SMEE_URL=None
ENV JENKINS_USERNAME=user
ENV JENKINS_PASSWORD=None
ENV SVC_IP_ADDRESS=None
ENV WEBHOOK_ENDPOINT=None
ENV PROTOCOL=None

RUN apt update
RUN apt -y install npm
RUN npm install --global smee-client

COPY ./webhookfrwd.py /home