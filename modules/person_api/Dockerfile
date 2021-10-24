FROM python:3.9-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN  apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
RUN pip install -r requirements.txt

EXPOSE 4000
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]