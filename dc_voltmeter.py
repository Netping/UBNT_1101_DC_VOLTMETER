import serial
import serial.rs485
import time
import binascii




avail_channels = [ 'V_IN0', 'V_IN1', 'V_IN2', 'V_IN3', 'V_IN4', 'V_IN5', 'V_IN6', 'V_IN7' ]

class DC_V:
    #deviceAddr = 1
    ser = None

    def __init__(self):
        if not DC_V.ser:
            DC_V.ser = serial.Serial(port='/dev/dkst1101/COM17',
                                    baudrate=9600,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS,
                                    timeout=1)

    def Get(self, channel):
        ret = 0

        try:
            if not channel.upper() in avail_channels:
                raise ValueError('Wrong channel name')

            cmd = '$02A\r'
            cmd = cmd.encode('ascii')

            DC_V.ser.write(cmd)
            time.sleep(0.2)

            answer = DC_V.ser.readline()
            answer = answer.decode('ascii')
            
            values = [ answer[x:x + 4] for x in range (1, len(answer), 4) ]
            
            index = int(channel.upper()[4:])
            
            b = bytes(values[index], 'utf-8')
            ba = binascii.a2b_hex(b)
            num = int.from_bytes(ba, byteorder='big', signed=True)
            

            #If hex_data >= 0 then
            #real_data = hex_data * 10 / 32767
            #else
            #real_data = hex_data * 10 / 32768
            if num >= 0:
                ret = num * 10 / 32767
            else:
                ret = num * 10 / 32768

        except Exception as ex:
            print(ex)

        return ret
