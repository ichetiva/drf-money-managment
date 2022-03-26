# Create user

URL: /api/users/create/\
Methods: POST

Request data example:
```json
{
    "username": "admin",
    "first_name": "James",
    "last_name": "Bond",
    "email": "james@mail.com",
    "password": "admin"
}
```

Response data example:
```json
{
    "id": 1,
    "username": "admin",
    "first_name": "James",
    "last_name": "Bond",
    "email": "james@mail.com",
    "password": "admin"
}
```
