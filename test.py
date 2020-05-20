import os
import sys
import json

from pycrime import CrimeClient


try:
    postcode = sys.argv[1]
except IndexError:
    print('Please provide a postcode')
    sys.exit(1)

jwt = os.environ.get('CRIME_API_KEY')
client = CrimeClient(jwt=jwt)
response = client.locality_statistics(postcode)
print(json.dumps(response, indent=2))
