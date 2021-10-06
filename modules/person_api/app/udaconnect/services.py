import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.udaconnect.models import Person
from sqlalchemy.sql import text


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")




class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person_data = Person()
        new_person_data.first_name = person["first_name"]
        new_person_data.last_name = person["last_name"]
        new_person_data.company_name = person["company_name"]

        db.session.add(new_person_data)
        db.session.commit()

        return new_person_data


    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person


    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()