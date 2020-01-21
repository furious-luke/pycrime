from pycrime import CrimeClient


jwt = None
client = CrimeClient(jwt=jwt)
response = client.locality_statistics('5000')
print(response)
