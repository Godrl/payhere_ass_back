FROM python:3.10-slim

WORKDIR /build
COPY Pipfile Pipfile.lock ./

EXPOSE 8000

# Install & use pipenv
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --ignore-pipfile

COPY ./app /build/app

CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
