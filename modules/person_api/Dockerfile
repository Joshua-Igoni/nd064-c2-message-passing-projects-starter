FROM python:3.8

WORKDIR /person_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 4000
COPY . .
RUN  apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
CMD ["flask", "run", "--host", "0.0.0.0"]