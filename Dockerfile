FROM node:8-alpine

RUN apk add --update --no-cache \
    bash \
    python \
    py-pip \
    groff \
    jq \
    zip \
    curl \
    git \
    ca-certificates && \
    pip install atlassian-python-api && \
    apk -v --purge del py-pip
RUN npm install markdown-to-html -g
WORKDIR /data
RUN mkdir /app
COPY add-comment-to-ticket.py /app
COPY create-page.py /app
COPY create-ticket.py /app
COPY run-request-in-confluence.py /app
COPY run-request-in-jira.py /app
COPY search-in-confluence-in-a-space.py /app
COPY search-in-confluence.py /app
