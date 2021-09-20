
import grpc
import person_pb2
import person_pb2_grpc

from person_writer import create, with_id, findAll


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def Create(self, request, context):
        
        single_person = {
            "first_name": request.first_name,
            "last_name": request.last_name,
            "company_name": request.company_name
        }
        new_person = create(single_person)
        return person_pb2_grpc.personmessage(
            first_name=new_person["first_name"],
            last_name=new_person["last_name"],
            company_name=new_person["company_name"],
            id=new_person["id"]
        )

    def Retrieve(self, request, context):
        
        person_id = request.id
        single_person = with_id(person_id)
        return person_pb2_grpc.personmessage(
            first_name=single_person.first_name,
            last_name=single_person.last_name,
            company_name=single_person.company_name,
            id=single_person.id
        )

    def RetrieveAll(self, request, context):
    
        all_persons = findAll()
        person_messages = []
        for person in all_persons:
            person_message = person_pb2_grpc.personmessage(
                first_name=person.first_name,
                last_name=person.last_name,
                company_name=person.company_name,
                id=person.id
            )
            person_messages.append(person_message)
        person_list_message = person_pb2_grpc.PersonListMessage()
        person_list_message.persons.extend(person_messages)
        return person_list_message
