FROM jenkins/jenkins:lts

USER root

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    docker.io \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl && \
    apt-get clean

# Make python default
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Install Google Cloud CLI (correct location: /opt/gcloud)
RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz && \
    tar -xf google-cloud-cli-linux-x86_64.tar.gz && \
    mv google-cloud-sdk /opt/gcloud && \
    /opt/gcloud/install.sh --quiet && \
    rm google-cloud-cli-linux-x86_64.tar.gz

# Add gcloud to PATH
ENV PATH=$PATH:/opt/gcloud/bin

USER jenkins