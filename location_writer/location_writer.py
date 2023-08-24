import csv
import time
import requests
import datetime

base_url = 'http://api.open-notify.org/iss-now.json'


def get_iss_location():
    response = requests.get(base_url)
    data = response.json()
    location = data['iss_position']
    return location['longitude'], location['latitude']


def location_writer_csv():
    with open('statistic/iss_location.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([longitude, latitude])


try:
    while True:
        latitude, longitude = get_iss_location()
        location_writer_csv()
        print(f'Current ISS position is {longitude},{latitude}.')
        time.sleep(5)
except KeyboardInterrupt:
    print('Program stopped.')
