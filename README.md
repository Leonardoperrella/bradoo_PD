# Bradoo - Python Developer

## Objective
The main objective of this project is to create an API to manage the loan payments control system from a fintech.

## Purpose
The purpose of this challenge is to test your ability to implement a solution given an abstract problem. You may find a problem in the asked task that you need to explain the problem and propose a solution to fix it.

## Problem
A fin-tech needs to create and manage the clients and keep track of the amount of money loaned and the missed/made payments. It also needs a place to retrieve the volume of outstanding debt at some point in time.

## Business Rules

*If a client contracted a loan in the past and paid all without missing any payment, you can decrease by 0.02% his tax rate.
*If a client contracted a loan in the past and paid all but missed until 3 monthly payments, you can increase by 0.04% his tax rate.
*If a client contracted a loan in the past and paid all but missed more than 3 monthly payments or didn’t pay all the loan, you need to deny the new one.


## Limitations
Loans are paid back in monthly installments.

## Endpoints

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

- Example of received data

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

- Example Not Found data.

    {
        "detail": "Not found."
    }


### DELETE /vendors/{id}/

Delete a vendor data and related products.

- Example of Not Found data.

    {
        "detail": "Not found."
    }
