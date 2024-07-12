import requests

emulator_url = 'http://127.0.0.1:54510/v1/projects/testbed-test:commit'

payload = b'{"mode": "NON_TRANSACTIONAL", "mutations": [{"delete": {"partitionId": {"projectId": "testbed-test", "namespaceId": ""}, "path": [{"kind": "HookTestModel", "name": "NONEXISTENT_KEY_NAME"}]}}]}'

headers = {'Content-Length': '192', 'Content-Type': 'application/json'}

# POST request to the emulator
resp = requests.post(emulator_url, headers=headers, data=payload)

# check response's data
data = resp.json()

# data  must include "version" field based on the reference https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/commit#MutationResult
# Note: Datastore emulator behaves as expected.

print(data)