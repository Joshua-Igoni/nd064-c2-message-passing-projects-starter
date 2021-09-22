import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List

import grpc
from app_folder import db
from app_folder.udaconnect.models import Connection, Location, Person
from app_folder.udaconnect.schemas import (ConnectionSchema, LocationSchema,
                                    PersonSchema)
from geoalchemy2.functions import ST_AsText, ST_Point
from kafka import KafkaProducer
from person_api import person_pb2, person_pb2_grpc
from sqlalchemy.sql import text

channel = grpc.insecure_channel("person-service:5005")
person_stub = person_pb2_grpc.PersonServiceStub(channel)

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LocationService")

producer = KafkaProducer(bootstrap_servers=['kafka-service:9092'])


class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5
    ) -> List[Connection]:
        """
        Finds all Person who have been within a given distance of a given Person within a date range.

        This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        smoothly for a better user experience for API consumers?
        """
        locations: List = db.session.query(Location).filter(
            Location.person_id == person_id
        ).filter(Location.creation_time < end_date).filter(
            Location.creation_time >= start_date
        ).all()

        # Cache all users in memory for quick lookup
        person_map: Dict[str, Person] = {person.id: person for person in PersonService.retrieve_all()}

        # Prepare arguments for queries
        data = []
        for location in locations:
            data.append(
                {
                    "person_id": person_id,
                    "longitude": location.longitude,
                    "latitude": location.latitude,
                    "meters": meters,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": (end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
                }
            )

        query = text(
            """
        SELECT  person_id, id, ST_X(coordinate), ST_Y(coordinate), creation_time
        FROM    location
        WHERE   ST_DWithin(coordinate::geography,ST_SetSRID(ST_MakePoint(:latitude,:longitude),4326)::geography, :meters)
        AND     person_id != :person_id
        AND     TO_DATE(:start_date, 'YYYY-MM-DD') <= creation_time
        AND     TO_DATE(:end_date, 'YYYY-MM-DD') > creation_time;
        """
        )
        result: List[Connection] = []
        for line in tuple(data):
            for (
                exposed_person_id,
                location_id,
                exposed_lat,
                exposed_long,
                exposed_time,
            ) in db.engine.execute(query, **line):
                location = Location(
                    id=location_id,
                    person_id=exposed_person_id,
                    creation_time=exposed_time,
                )
                location.set_wkt_with_coords(exposed_lat, exposed_long)

                result.append(
                    Connection(
                        person=person_map[exposed_person_id], location=location,
                    )
                )

        return result


class LocationService:
    @staticmethod

    def send_location(location_data):
        #this sends data to the kafka topic 'location'
        logger.info(location_data)
        producer.send('location', json.dumps(location_data).encode('utf-8'))
        producer.flush()

class PersonService:
    @staticmethod
    def retrieve_with_id(person_id):
        requestMessage = person_pb2.PersonRequestMessage(id=person_id)
        person = person_stub.Retrieve(requestMessage)
        return person


    def retrieve_all():
        requestMessage = person_pb2.PersonRequestMessage()
        persons = person_stub.RetrieveAll(requestMessage)
        return persons


    def create(data):
        person_message = person_pb2.personmessage(
            first_name=data['first_name'],
            last_name=data['last_name'],
            company_name=data['company_name']
        )
        new_person_create= person_stub.Create(person_message)
        return new_person_create