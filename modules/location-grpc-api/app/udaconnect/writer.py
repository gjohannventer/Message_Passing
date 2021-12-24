import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")
channel = grpc.insecure_channel("localhost:30003") #port of kubernetes
stub = location_pb2_grpc.LocationServiceStub(channel)

# Send the desired input to location grpc server
location_1 = location_pb2.LocationMessage(
    person_id="1",
    latitude="35",
    longitude='-45',
)

location_2 = location_pb2.LocationMessage(
    person_id="6",
    latitude="45",
    longitude='-5',
)

response_1 = stub.Create(location_1)
response_2 = stub.Create(location_2)
print(response_1)
print(response_2)