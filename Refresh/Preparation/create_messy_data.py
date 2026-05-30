import json

bad_data = [
    {"device_id": "Sensor_A", "timestamp": "2026-05-28 10:00:00", "temperature": "22.5", "status": "OK"},
    {"device_id": "Sensor_B", "timestamp": "2026-05-28 10:01:00", "temperature": "abc", "status": "OK"}, # Error: string instead of float
    {"device_id": "Sensor_A", "timestamp": "2026-05-28 10:00:00", "temperature": "22.5", "status": "OK"}, # Error: Duplicate row
    {"device_id": "Sensor_C", "timestamp": "2026-05-28 10:02:00", "temperature": None, "status": "ERROR"}, # Error: Missing temp
    {"device_id": "Sensor_A", "timestamp": "2026-05-28 10:03:00", "temperature": "24.1", "status": "OK"},
    {"device_id": "Sensor_B", "timestamp": "2026-05-28 10:04:00", "temperature": "999.0", "status": "OK"}, # Error: Outlier/corrupt reading
    {"device_id": "Sensor_C", "timestamp": "2026-05-28 10:05:00", "temperature": "19.8", "status": "OK"}
]

with open("messy_telemetry.json", "w") as f:
    json.dump(bad_data, f, indent=4)

print("Created 'messy_telemetry.json' successfully!")