import grpc
import location_pb2
import location_pb2_grpc


"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

#get an id that already exists in the db
request = location_pb2.LocationMessageRequest(
    id="29"
)

response = stub.Get(request)
print(response)