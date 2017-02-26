# awg70k_pyvisa_send_wfm_1.py
# demonstration of the remote programatic comamnd
# wlist:waveform:data
# for vectors less than 250 million samples

import visa # https://pypi.python.org/pypi/PyVISA
import numpy as np # https://pypi.python.org/pypi/numpy/

# constants
visa_address = 'tcpip::tsc-awg70002a::instr'

# make three sines
l = 60000
s = np.linspace(0, l, num=l, endpoint=False, dtype=np.single)
v1 = np.sin(2 * np.pi / 250 * s)
v2 = np.sin(2 * np.pi / 116 * s)
v3 = np.sin(2 * np.pi / 75 * s)
print(type(v1))

rm = visa.ResourceManager()
awg = rm.open_resource(visa_address)
awg.timeout = 10000

r = awg.query('*idn?')
print(r.strip())

awg.write('*cls')
awg.write('wlist:waveform:delete ALL')

print('sending v1...')
awg.write('wlist:waveform:new "{}",{}'.format('v1', v1.size))
cmd_prefix = 'wlist:waveform:data "{}",'.format('v1')
awg.write_binary_values(cmd_prefix, v1)

print('sending v2...')
awg.write('wlist:waveform:new "{}",{}'.format('v2', v2.size))
cmd_prefix = 'wlist:waveform:data "{}",'.format('v2')
awg.write_binary_values(cmd_prefix, v2)

print('sending v3...')
awg.write('wlist:waveform:new "{}",{}'.format('v3', v3.size))
cmd_prefix = 'wlist:waveform:data "{}",'.format('v3')
awg.write_binary_values(cmd_prefix, v3)

r = int(awg.query('*esr?'))
print('event register: 0b{:08b}'.format(r))
while True:
    r = awg.query('system:error?')
    print(r.strip())
    if r == '0,"No error"\n':
        break

awg.close()
print('done')
