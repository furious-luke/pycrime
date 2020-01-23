import os

from pycrime import CrimeClient


jwt = os.environ.get('CRIME_API_KEY')
client = CrimeClient(jwt=jwt)
response = client.locality_statistics('3000')
print(response)
