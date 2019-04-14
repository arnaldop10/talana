FROM python:2.7.16-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /talana
WORKDIR /talana
COPY requirements.txt /talana/
RUN pip install -r requirements.txt
COPY . /talana/