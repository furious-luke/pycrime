from pycrime import CrimeClient


jwt = None
client = CrimeClient(url='https://crime.structrs.com', jwt=jwt)
response = client.locality_statistics('5000')
print(response)
