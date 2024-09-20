FROM python:3.9-slim
# google for: python docker images 
RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

# Install numpy explicitly as a workaround for pipenv issues
RUN pip install numpy scipy

COPY ["model_C=1.0.bin", "predict.py", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]

