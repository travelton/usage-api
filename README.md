# Usage API
Simple Python Flask app API endpoint for demo purposes.


## Retrieve Data
Sample Request

```sh
GET /stats/users
```

Example Response

```json
{
    "2021-05-02": 500,
    "2021-05-01": 200
}
```


## Store Data
Sample Request

```sh
POST /stats/users
{
    "date": "2021-05-02",
    "count": 500
}
```

Example Response

```json
{
    "message": "Data received!",
    "data": {
        "date": "2021-05-02",
        "count": 500
    }
}
```