# SDM72D-M
SDM72D-M ModBus RTU client to read EASTRON SDM 3 phase smart power meter registers

It depends on libmodbus (http://libmodbus.org)

To compile
  make clean && make

To install
  make install

To uninstall
  make uninstall

<PRE>
# SDM72D-M
SDM72D-M ModBus RTU client to read EASTRON SDM72D-M 3 phase smart power meter registers

It works with SDM72D-M and SDM220 models

It depends on libmodbus (http://libmodbus.org)

To compile and install
  make clean && make install

<PRE>
Usage: sdm72d-m [-a address] [-d] [-x] [-p] [-v] [-c] [-e] [-i] [-t] [-f] [-g] [-T] [[-m]|[-q]] [-b baud_rate] [-P parity] [-S bit] [-z num_retries] [-j seconds] [-w seconds] [-1 | -2] device
       sdm72d-m [-a address] [-d] [-b baud_rate] [-P parity] [-S bit] [-1 | -2] -s new_address device
       sdm72d-m [-a address] [-d] [-b baud_rate] [-P parity] [-S bit] [-1 | -2] -r baud_rate device 
       sdm72d-m [-a address] [-d] [-b baud_rate] [-P parity] [-S bit] [-1 | -2] -R new_time device

where
    -a address     Meter number (between 1 and 247). Default: 1
    -s new_address Set new meter number (between 1 and 247)
    -p             Get power (W)
    -v             Get voltage (V)
    -c             Get current (A)
    -f             Get frequency (Hz)
    -g             Get power factor
    -e             Get exported energy (Wh)
    -i             Get imported energy (Wh)
    -t             Get total energy (Wh)
    -T             Get Time for rotating display values (0 = no rotation) 
    -d             Debug
    -x             Trace (libmodbus debug on)
    -b baud_rate   Use baud_rate serial port speed (1200, 2400, 4800, 9600)
                   Default: 2400
    -P parity      Use parity (E, N, O)
    -S bit         Use stop bits (1, 2). Default: 1
    -r baud_rate   Set baud_rate meter speed (1200, 2400, 4800, 9600)
    -R new_time    Change rotation time for displaying values (0 - 30s) (0 = no totation)
    -m             Output values in IEC 62056 format ID(VALUE*UNIT)
    -q             Output values in compact mode
    -z num_retries Try to read max num_retries times on bus before exiting
                   with error. Default: 1 (no retry)
    -j 1/10 secs   Response timeout. Default: 2=0.2s
    -D 1/1000 secs Delay before sending commands (wait line set). Default: 30=0.03s
    -w seconds     Time to wait to lock serial port. (1-30s) Default: 0s
    -1             Model: sdm72d-m (default)
    -2             Model: SDM220
    device         Serial device, i.e. /dev/ttyUSB0

Serial device is required. When no parameter is passed, retrives all values</PRE>
