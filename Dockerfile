FROM python:3.10.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./app/requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./app/ /code/