"""
DigitalHarbor Confidential
CLD-59193-1597956416
(c) Copyright DH Corp. 2020
The source code for this program is not published. Copyright.

util.py
    A set of methods to use in different sections of the framework.
"""

import requests
from setting import URL

def search_email_from_users(email_to_find, page="2"):
    """
    Method to search an email from users page.

    Args:
        email_to_find  (str):           This value is an email(e.g: name@domain.com)
        page           (str, optional): Page number(e.g: 1 or 2 or 3)

    Returns:
        email_is_found (str): Return found email, otherwise a message.
    """
    email_is_found = "Email '{}' was not found".format(email_to_find)
    users = run_request("get", URL+"?page={}".format(page))
    for item in users["data"][:]:
        if item["email"] == email_to_find:
            email_is_found = email_to_find
            break
    return email_is_found

def run_request(method, endpoint, headers="", body=""):
    """
    Method to execute API requests, for example: POST, GET, PATCH, DELETE

    Args:
        method   (str):           This value is a method type to work with API
                                  (e.g: POST, GET, PATCH, DELETE)
        endpoint (str):           This value is an endpoint (e.g: https://reqres.in/api/users)
        headers  (str, optional): Value of headers.
        body     (str, optional): Value of body to use with POST methods.

    Returns:
        response (json):          Returns a json response from the request.
    """
    method  = method.lower()

    if method == 'get':
        response = requests.get(endpoint, headers=headers)
    if method == 'post':
        response = requests.post(endpoint, headers=headers, data=body)
    if method == 'put':
        response = requests.put(endpoint, json=body, headers=headers)
    if method == 'delete':
        response = requests.delete(endpoint, headers=headers)

    return response.json()
