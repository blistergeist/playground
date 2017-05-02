# threading_practice.py

import threading, time, serial, pynmea2, queue, multiprocessing

def poop(q):
    while True:
        time.sleep(1)
        q.put('yar')
    # while True:
    #     time.sleep(1)
    #     print('yar')


# class GPS_thread(threading.Thread):
#     def __init__(self, threadID, name, comPort, baudRate, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.comPort = comPort
#         self.baudRate = baudRate
#         self.q = q
#         self.gps_setup()

#     def run(self):
#         initTime = time.perf_counter()
#         msg = get_gga_sentence(self.gps)
#         self.q.put(msg)


#     def gps_setup(self):
#         # tests device in selected COM port to see if it returns data
#         try:
#             self.gps = serial.Serial(self.comPort, baudrate=self.baudRate, 
#                 timeout=1)
#             self.gps.flush()
#             if not self.gps.readline():
#                 raise GPSError('{} returns no data.'.format(self.comPort))
#         except PermissionError:
#             raise


# def get_gga_sentence(gps):
#     d = gps.readline()
#     while not d.decode('cp1252').startswith('$GPGGA,') or len(d) > 80:
#         if len(d) > 80:
#             print(d.decode('cp1252'))
#         d = gps.readline()
#     msg = pynmea2.parse(d.decode('cp1252'))
#     if int(msg.num_sats) < 1:
#         raise GPSError('No satellites locked.')
#     return msg
    

# if __name__ == '__main__':
#     q = queue.Queue()
#     gps = GPS_thread(0, 'gps thread', 'COM12', 4800, q)
#     garbage = multiprocessing.Process(target=poop)

#     gps.start()
#     garbage.start()

#     gps.join()
#     msg = q.get()

#     print('Latitude: {}'.format(msg.lat))
#     print('Longitude: {}'.format(msg.lon))
#     print('Current time (GMT): {}'.format(msg.timestamp))
#     print('Altitude ({}) {}'.format(msg.altitude_units.lower(), msg.altitude))
#     print('Num Satellites: {}'.format(msg.num_sats))
#     print('Timestamp: {}'.format(msg.timestamp))

#     time.sleep(3)
#     garbage.terminate()
#     garbage.join()


if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=poop, args=(q,))
    p.start()
    for i in range(3):
        print(q.get())
    p.terminate()