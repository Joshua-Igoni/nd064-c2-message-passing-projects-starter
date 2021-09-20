FROM python:3.7-alpine

WORKDIR /person_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 4000
COPY . .
RUN  python -m grpc_tools.protoc -I./modules/person_api/ --python_out=./modules/person_api/ --grpc_python_out=./modules/person_api/ person.proto
CMD ["python", "app.py"]