import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config import config_by_name
from app.udaconnect.models import Person


config = config_by_name[os.getenv("FLASK_ENV") or "test"]
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)


def create(single_person):
    session = Session(engine)
    new_person = Person()
    new_person.first_name = single_person["first_name"]
    new_person.last_name = single_person["last_name"]
    new_person.company_name = single_person["company_name"]
    session.add(new_person)
    new_person_data = {
        "id": new_person.id,
        "first_name": new_person.first_name,
        "last_name": new_person.last_name,
        "company_name": new_person.company_name
    }

    session.commit()
    session.close()
    return new_person_data


def with_id(person_id):
    session = Session(engine)
    single_person = session.query(Person).get(person_id)
    session.close()
    return single_person


def findAll():
    session = Session(engine)
    all_persons = session.query(Person).all()
    session.close()
    return all_persons
