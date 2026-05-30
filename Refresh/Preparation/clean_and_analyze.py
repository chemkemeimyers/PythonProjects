import csv
import json

def read_json_data(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)
    return data

def read_csv_data(input_file):
    with open(input_file, "r") as f:
        data = list(csv.reader(f))
    return data

def clean_data(input_data):
    unique_fingerPrints = set()

    #remove duplicates
    output_data = []
    for record in input_data:
        fingerprint = (record['device_id'], record['timestamp'])
        if fingerprint not in unique_fingerPrints:
            unique_fingerPrints.add(fingerprint)
            output_data.append(record)
    return output_data

def print_records(records):
    for record in records:
        print(record)

def parse_string_to_float(string_value):
    try:
        return float(string_value)
    except (ValueError, TypeError):
        print(f"Could not convert '{string_value}' to float. Setting to None.")
        return None

def convert_temperature_to_float(data):
    for record in data:
        record['temperature'] = parse_string_to_float(record['temperature'])
    return data

def find_valid_temperatures(data):
    valid_temperature_records = []
    for record in data:
        if record['temperature'] is not None and -50 <= record['temperature'] <= 150:
            valid_temperature_records.append(record)
    return valid_temperature_records

def find_average_temp(valid_records):
    temp_tally = 0
    count = 0

    for record in valid_records:
        temp_tally += record['temperature']
        count +=1

    return temp_tally/count if count >0 else None


if __name__ == "__main__":
    #read data from JSON file
    input_filename = "messy_telemetry.json"
    json_data = read_json_data(input_filename)

    cleaned_data = clean_data(json_data)
    print("Cleaned Data: ")
    print_records(cleaned_data)

    convert_temperature_to_float(cleaned_data)
    print("Data after converting temperature to float: ")
    print_records(cleaned_data)

    print("Records with valid temperature are: ")
    records_with_valid_temps = find_valid_temperatures(cleaned_data)
    print_records(records_with_valid_temps)

    print("The average temperature is: ")
    print(find_average_temp(records_with_valid_temps))

