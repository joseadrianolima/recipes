FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

WORKDIR /App

COPY . .

RUN pip3 install -U Django
RUN pip3 install -U python-dotenv
RUN pip3 install -U django-tinymce
RUN pip3 install -U Pillow
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]