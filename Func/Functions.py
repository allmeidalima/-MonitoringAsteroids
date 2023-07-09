import requests
import json
import matplotlib.pyplot as plt

#Use this function for get url
def request_url_string(string):
    url = string
    response = requests.get(url)
    file = json.loads(response.text)
    return file

#Use this function for create de table
def create_asteroid_label(dict: dict, name_bar: str, y_index: str, x_index: str, graphic_name: str):
    labels = list(dict.keys())
    values = list(dict.values())

    plt.bar(labels, values)
    plt.xlabel(x_index)
    plt.ylabel(y_index)
    plt.title(name_bar)
    plt.xticks(rotation=45)
    plt.show(block=True)