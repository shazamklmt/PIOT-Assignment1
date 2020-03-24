from sense_hat import SenseHat
import json, os

# Get the file contents
def get_file_contents():
    readFile = open("Task B/config.json", "r")
    contents = readFile.read()

    data = json.loads(contents)

    for key, value in data.items():
        print(key, value)

sense = SenseHat()
sense.clear()

# Get CPU temperature
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n",""))

# Get SenseHat temperature
senseTemp = sense.get_temperature_from_humidity()

# Get actual temperature
realTemp = senseTemp - get_cpu_temp()
print(realTemp)

get_file_contents()