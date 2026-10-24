### Currently Implemented Endpoints:
- ✅ -> fully implemented
- 🟡 -> partly implemented
- ➖ -> no request of that type exists for that endpoint
- ❌ -> not implemented

The API-Browser was reworked in Graylog 7. Instead of listing all possible Endpoints, this table will now show the (partly) implemented Endpoints. The ones that are not here are not yet implemented. 

| Endpoint | Description | Get | Post | Delete | Put | Status | Notes |
|----------|-------------|-----|------|--------|-----|--------|-------|
| `/plugins/SecurityApp/Assets` | SecurityApp Assets | 🟡 | 🟡 | ✅ | ✅ | Partially Implemented | [endpoints.plugins.SecurityApp](/src/graylog_api_client/endpoints/plugins/SecurityApp.py) |
| `/authz` | Authorization | 🟡 | ❌ | ❌ | ❌ | Partly Implemented | [endpoints.authz](/src/graylog_api_client/endpoints/authz.py) |
| `/search` | Search (Simple) | ❌ | 🟡 | ➖ | ➖ | Partly Implemented | [endpoints.search](/src/graylog_api_client/endpoints/search.py) |
| `/users` | Users | ✅ | ❌ | ❌ | ❌ | Partly Implemented | [endpoints.users](/src/graylog_api_client/endpoints/users.py) |
| `/views` | Main Views Endpoints | ✅ | ❌ | ❌ | ❌ | Partly Implemented | [endpoints.views](/src/graylog_api_client/endpoints/views.py) |
