import requests

question_data = []
parameters = {
    "amount": 10,
    "type": "boolean",
}

# data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean") # same as:
data = requests.get("https://opentdb.com/api.php", params=parameters)
print(data)
question_data = data.json()["results"]

#print(question_data)
