import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])


def greet(greeting, name):
    """Return a greeting

    Arguments:
        greeting {string} -- A word
        name {string} -- A persons name

    Returns:
        string -- Greeting with a name
    """
    return f"{greeting} {name}"
