# pyserial_test.py

import serial, pynmea2, time

s = serial.Serial('COM12', 4800, timeout=0.5)
s.flush()
if not s.readline():
    raise Exception('The device at this port returns no data.')

for i in range(3):
    t1 = time.perf_counter()
    data = s.readline()
    while 'GGA' not in data.decode('cp1252'):
        data = s.readline()
        if len(data) > 80:
            # print(data.decode('cp1252'))
            print('yar')
    print(data.decode('cp1252'))
    print(time.perf_counter()-t1)
    # raise Exception
    try:
        msg = pynmea2.parse(data.decode('cp1252'))
        print('Latitude: {}'.format(msg.lat))
        lat = '{:2.0f}\xb0{:2.0f}\'{:02.4f}"'.format(
            msg.latitude, msg.latitude_minutes, msg.latitude_seconds)
        lon = '{:2.0f}\xb0{:2.0f}\'{:02.4f}"'.format(
            msg.longitude, msg.longitude_minutes, msg.longitude_seconds)
        print('Latitude: {}'.format(lat))
        print('Longitude: {}'.format(lon))
    #     # print('Current time (GMT): {}'.format(msg.timestamp))
    #     # print('Altitude ({}) {}'.format(msg.altitude_units.lower(), msg.altitude))
    #     # print('Num Satellites: {}'.format(msg.num_sats))
    #     print('Timestamp: {}'.format(msg.timestamp))
    #     print(time.gmtime(time.time()).tm_sec)
    except pynmea2.nmea.ParseError:
        print('Parse Error')

s.close()