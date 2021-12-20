from concurrent import futures
from app.udaconnect.models import Location
from app.udaconnect.services import LocationService
import grpc
import location_pb2
import location_pb2_grpc
from kafka import KafkaProducer
import json

kafka_url = "kafka:9092"
kafka_topic = "location"
kafka_producer = KafkaProducer(bootstrap_servers=kafka_url)

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request_value = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude
        }

        kafka_request = json.dumps(request_value).encode()
        kafka_producer.send(kafka_topic, kafka_request)
        kafka_producer.flush()
        
        return location_pb2.LocationMessage(**request_value)

    def Get(self, request, context):
        location: Location = LocationService.retrieve(int(request.id))
        response_value = {
            "person_id": location.id,
            "longitude": location.longitude,
            "latitude": location.latitude
        }

        return location_pb2.LocationMessage(**response_value)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(
    LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
server.wait_for_termination()