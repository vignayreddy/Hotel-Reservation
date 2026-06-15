FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
    docker.io \
    python3 \
    python3-pip \
    python3-venv \
    git && \
    apt-get clean

RUN ln -sf /usr/bin/python3 /usr/bin/python

USER root