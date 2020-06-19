# Bradoo - Python Developer

## Description
    The main objective of this project is to create an aplicantion for registration of vendor catalogues.

## Requirements and Resources Used.

### Computer

    Hp pavilion I5 4G RAM.

### Operational System

    Ubuntu 18.04 LTS.

### IDLE

    VsCode 1.46.1

### Libraries

    decimal
    django
    djangorestframework
    dj-database-url
    dj-static
    drf-writable-nested
    localflavor
    python-decouple

## How to developer?

    1. Clone the repository
    2. Create a virtualenv
    3. Active o virtualenv
    4. Install the dependencies.
    5. Configure the instance with .env
    6. Run secret_gen.py
    7. On file .venv, replace secret key generated into variable SECRET_KEY=<SECRET_KEY>.
    8. Run migrations
9. Execute tests

```console
    git clone https://github.com/Leonardoperrella/bradoo_PD.git bradoo
    cd bradoo
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    cp contrib/env-sample .env
    cd contrib
    python secret_gen.py
    cd ..
    python manage.py migrate
    python manage.py test
```


### POST /vendors/

#### Summary

Create a vendor in the system.

#### Payload

- name: Vendor's name.
- cnpj: Vendor's Identification Number.
- city: Vendor's city.
- products: Vendor's product(s).
    - name: Product's name.
    - code: Product's code.
    - price: Product's sales price. 

Example of sent data

    {
        "name": "Vendor1",
        "cnpj": "00000000000000",
        "city": "Sao Paulo",
        "products": [{
            "name": "Product1",
            "code": "000001",
            "price": 10.00,
        }]
    }

#### Reply

Example of received data

    {
        "name": "Vendor1",
        "cnpj": "00000000000000",
        "city": "Sao Paulo",
        "products": [{
            "name": "Product1",
            "code": "000001",
            "price": 10.00,
        }]
    }


### GET /vendors/

#### Summary

Get a json of all vendors.

### GET /vendors/?id={id}&cnpj={cnpj}&name={name}

Get a json of a filtered vendor by id, cnpj or name or 
a combination of those fields.

### PUT /vendors/{id}/

Alter some of vendors's data.

- name: Vendor's name.
- cnpj: Vendor's Identification Number.
- city: Vendor's city.
- products: Vendor's product(s).
    - name: Product's name.
    - code: Product's code.
    - price: Product's sales price. 

Example of sent data

    {
        "name": "Vendor1",
        "cnpj": "00000000000000",
        "city": "Sao Paulo",
        "products": [{
            "name": "Product1",
            "code": "000001",
            "price": 20.00,
        }]
    }

#### Reply

Example of received data

    {
        "name": "Vendor1",
        "cnpj": "00000000000000",
        "city": "Sao Paulo",
        "products": [{
            "name": "Product1",
            "code": "000001",
            "price": 20.00,
        }]
    }


### DELETE /vendors/{id}/

Delete a vendor data and related products.
