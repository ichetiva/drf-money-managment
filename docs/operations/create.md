# Create operation for wallet

URL: /api/operations/create/\
Methods: POST

Authorization token required

Request data example:
```json
{
    "wallet": 1,
    "_type": "<Income or Expense>",
    "amount": 100,
    "comment": "<some comment>"
}
```

Response data example:
```json
{
    "id": 1,
    "wallet": 1,
    "_type": "<Income or Expense>",
    "amount": 100,
    "comment": "<some comment>"
}
```
