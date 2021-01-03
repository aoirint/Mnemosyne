FROM python:3

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
  wait-for-it

ADD ./requirements.txt /
RUN pip3 install -r /requirements.txt

ADD ./django /code


ADD ./docker-entrypoint.sh /
ENTRYPOINT [ "/docker-entrypoint.sh" ]

# CMD [ "python3", "/code/manage.py", "runserver", "0.0.0.0:8000" ]

# TODO: nginx integration to distribute static files
CMD [ "gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "--chdir", "/code", "Mnemosyne.wsgi:application" ]
