FROM python:3.8

WORKDIR /location_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app.py"]