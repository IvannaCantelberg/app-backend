FROM python:3.10

RUN useradd --create-home userapi
WORKDIR /backend

RUN pip install -U pipenv
COPY Pipfile .
COPY Pipfile.lock .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system
COPY ./ .

RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app