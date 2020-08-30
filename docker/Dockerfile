FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
WORKDIR /code/dew_save/dew_save
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dew_save.wsgi:application"]