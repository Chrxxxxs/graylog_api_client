### This is a low level Graylog API Wrapper heavily based on the guide by [pretzel](https://www.pretzellogix.net/2021/12/08/how-to-write-a-python3-sdk-library-module-for-a-json-rest-api/).
As there are a lot of endpoints not all of them are implemented by now. I started by implementing the GET requests first.
Also the API responses all follow very different schemas and an implementation of that into Python is probably not worth the effort which is why the responses from this API are so low-level.
Due to the amount of Endpoints and the frequent changes, this project does not aim to implement all of them. Instead, only the ones that are needed are added. If some are missing that you need, create an issue or PR. When adding calls to a new Endpoint, follow the schema that is already used (e.g. all authz calls are located in [endpoints.authz.py](/src/graylog_api_client/endpoints/authz.py)).
#### Last tested Graylog Major Version is: 7

### Example Usage

```python
from graylog_api_client import GraylogAPI

# Initialize the GraylogAPI client
api = GraylogAPI(
    host="https://localhost:9000/api",  # Replace with your Graylog server URL
    api_key="your_api_key_here",       # Replace with your API key
    ssl_verify=True                   # /path/to/cert for custom certificate
)

# Example: Fetch users
users = api.users.get_users_paginated({"sort": "username"})

# Print the result
for user in users.data.get("users", []):
    print(f"Username: {user['username']}, Email: {user['email']}, id: {user['id']}")
```

Planned:
1. Tests that run against a Graylog instance to check if the Wrapper works after Graylog Updates


### Test Environment:
1. Install docker and docker-compose
2. Copy the sample docker-compose file by [Graylog](https://github.com/Graylog2/docker-compose) for the open-core (or enterprise if you want to see all API endpoints) and create a .env file with the needed values
3. docker-compose up
4. Log in and create an api-key