# PCODE-API

![example workflow](https://github.com/RamSailopal/PCODE-API/actions/workflows/deploy.yml/badge.svg)

An API that takes a UK post code and returns the longitute and latitude

Utilises YottaDB as the database and Python flask to present the API endpoint.

# To run

    docker-run -p 5000:5000 -it docker.io/ramb0/api-pcode

The endpoint will then be available at the address http://dockerserveraddress:5000/pcode

To get the co-ordinates for example of zip **B71 4LF**:

    curl http://dockerserveraddress:5000/pcode?pcode=B71 4LF
    
    
Output:

    [
      {
        "lat": "52.509003",
        "long": "1664982",
        "pcode": "B71 4LF"
      }
    ]
