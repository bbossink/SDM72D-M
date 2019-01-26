#!/usr/bin/python
# Modified sdm120c.py script for use with SDM72D-M Eastron meter

import minimalmodbus

rs485 = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
rs485.serial.baudrate = 9600
rs485.serial.bytesize = 8
rs485.serial.parity = minimalmodbus.serial.PARITY_NONE
rs485.serial.stopbits = 1
rs485.serial.timeout = 1
rs485.debug = False
rs485.mode = minimalmodbus.MODE_RTU

# Uncomment below line to print some rs485 parameters during script execution
# print rs485

Total_System_Power = rs485.read_float(52, functioncode=4, numberOfRegisters=2)
Import_Power = rs485.read_float(1280, functioncode=4, numberOfRegisters=2)
Export_Power = rs485.read_float(1282, functioncode=4, numberOfRegisters=2)
Import_Active_Energy = rs485.read_float(72, functioncode=4, numberOfRegisters=2) 
Export_Active_Energy = rs485.read_float(74, functioncode=4, numberOfRegisters=2)
Total_Active_Energy = rs485.read_float(342, functioncode=4, numberOfRegisters=2)
Settable_Import_Energy = rs485.read_float(388, functioncode=4, numberOfRegisters=2)
Settable_Export_Energy = rs485.read_float(390, functioncode=4, numberOfRegisters=2)
Settable_Total_Energy = rs485.read_float(384, functioncode=4, numberOfRegisters=2)

print 'Total power: {0:.1f} Watts'.format(Total_System_Power)
print 'Import power: {0:.1f} Watts'.format(Import_Power)
print 'Export power: {0:.1f} Watts'.format(Export_Power)
print 'Import active energy: {0:.3f} KWh'.format(Import_Active_Energy)
print 'Export active energy: {0:.3f} KWh'.format(Export_Active_Energy)
print 'Total active energy: {0:.3f} KWh'.format(Total_Active_Energy)
print 'Settable import energy: {0:.3f} KWh'.format(Settable_Import_Energy)
print 'Settable export energy: {0:.3f} KWh'.format(Settable_Export_Energy)
print 'Settable total energy: {0:.3f} KWh'.format(Settable_Total_Energy)
