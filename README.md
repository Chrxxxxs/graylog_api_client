### This is a low level Graylog API Wrapper heavily based on the guide by [pretzel](https://www.pretzellogix.net/2021/12/08/how-to-write-a-python3-sdk-library-module-for-a-json-rest-api/).
As there are a lot of endpoints not all of them are implemented by now. I started by implementing the GET requests first.
Also the API responses all follow very different schemas and an implementation of that into Python is probably not worth the effort which is why the responses from this API are so low-level.
Feel free to add endpoints or schemas in PRs if you need them :)
#### Last tested Graylog Version is: 6.3.4

Planned:
1. Tests that run against a Graylog instance to check if the Wrapper works after Graylog Updates


### Test Environment:
1. Install docker and docker-compose
2. Copy the sample docker-compose file by [Graylog](https://github.com/Graylog2/docker-compose) for the open-core and create a .env file with the needed values
3. docker-compose up
4. Log in and create an api-key