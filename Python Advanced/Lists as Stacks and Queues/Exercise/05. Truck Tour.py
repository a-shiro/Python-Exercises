from collections import deque


def get_gas_station_info(gas_stations_count):

    gas_stations_info = deque()

    for _ in range(gas_stations_count):
        petrol, distance = input().split()
        gas_stations_info.append([int(petrol), int(distance)])

    return gas_stations_info


def get_attempts_count(gas_stations_count, gas_station_info):

    attempt = 0
    fuel_tank = 0
    stops = 0

    # While the number of stops are less than the gas station count it means we haven't done a full circle
    while not stops == gas_stations_count:

        petrol, distance = gas_station_info[stops][0], gas_station_info[stops][1]

        fuel_tank += petrol

        if fuel_tank < distance:
            gas_station_info.append(gas_station_info.popleft())
            fuel_tank = 0
            stops = 0
            attempt += 1
        else:
            fuel_tank -= distance
            stops += 1

    return attempt


gas_stations_count = int(input())

gas_station_info = get_gas_station_info(gas_stations_count)
attempts = get_attempts_count(gas_stations_count, gas_station_info)

print(attempts)