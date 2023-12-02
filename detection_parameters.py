import json
from tkinter import filedialog
# Sample dictionary
data = {
    'lower_h': 28,
    'upper_h': 120,
    'lower_s': 30,
    'upper_s': 255,
    'lower_v': 45,
    'upper_v': 255,
    'kernel': 20,
    'blur': 0,
    'radius': 5
}


def write_default_values_file():
    global data
    # Open a JSON file in write mode
    with open('data_default.json', 'w') as json_file:
        json.dump(data, json_file)


def get_default_values():
    # Open the JSON file in read mode
    with open('data.json', 'r') as json_file:
        return json.load(json_file)

def write_custom_values_file(current_values):
    # Open a JSON file in write mode

    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])

    if file_path:
        # Open the selected file in write mode
        with open(file_path, 'w') as json_file:
            json.dump(current_values, json_file)


def get_values_from_file():

    # Ask the user to choose a JSON file
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])

    if file_path:
        # Open the selected file in read mode
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        get_default_values()