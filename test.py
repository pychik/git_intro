import json
import binascii
import base64
import datetime
import requests
from ctypes import *



class post_reader():
    def post_read(a):
        a=str(a).encode()
        print(a)
        b = binascii.hexlify(a)
        print(str(b)+ '\n')
        a1=a.decode('utf-8')
        #print('1')
        #print(a1)
        #a=a.binascii.hexlify()

        #a=a.decode('utf-8')
        byte_start = a1.find('Content-Transfer-Encoding: binary\r\n\r\n') + len('Content-Transfer-Encoding: binary\r\n\r\n')
        byte_end = a1.find('\r\n--BoreyGA09--')

        byte_string = a[byte_start:byte_end+2]
        #print(byte_string)
        byte_enc = binascii.hexlify(byte_string)
        print(byte_enc.decode('utf-8'))
    def do_POST(q):
        length = int(q.headers.getheader('content-length'))
        field_data = q.rfile.read(length)
        fields = urlparse.parse_qs(field_data)
        print(fields)


def convert(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    #print(fp.contents.value)
    return fp.contents.value

'''
# r = requests.post("http://94.188.34.177:9595/incoming/?", data={'Content-Transfer-Encoding': 'binary \r\n--BoreyGA09--'})
message = '--BoreyGA09\r\nContent-Disposition: form-data; name="CMD"\r\nContent-Type: text/plain\r\n\r\nDevVal\r\n--BoreyGA09\r\nContent-Disposition: form-data; name="DATA"\r\nContent-Type: application/octet-stream\r\nContent-Transfer-Encoding: binary\r\n\r\n\x18\x00\xaeh\x98#S\x07\x05\x07\x05\x13\x00\x8e(G\x01\xfd\x17\x00\x04m\x150e+\x01\xcb\'\x00\xb4L\x11\x01\x00\x00\x00\x00\x85\x10\x7f\x00\x00\x00\x00\x85 \x7f\x00\x00\x00\x00\x850\x7f\x00\x00\x00\x00\x01\xfd\x17\x00\x04m\x150e+q\xfb\x18\x00\xaeh\x98#S\x07\x05\x07\x05\x13\x00\x8e(G\x01\xfd\x17\x00\x04m\x160e+Q\x86\'\x00\xb4L\x11\x01\x00\x00\x00\x00\x85\x10\x7f\x00\x00\x00\x00\x85 \x7f\x00\x00\x00\x00\x850\x7f\x00\x00\x00\x00\x01\xfd\x17\x00\x04m\x160e+!\xb6\r\n--BoreyGA09--'
#message_1 = b'\x18\x00\xef\xbf\xbdh\xef\xbf\xbd#S\x07\x05\x07\x05\x13\x00..G\x01\xef\xbf\xbd\x17\x00\x04m*2e+\xef\xbf\xbd\x19\x18\x00\xef\xbf\xbdh\xef\xbf\xbd#S\x07\x05\x07\x05\x13\x00..G\x01\xef\xbf\xbd\x17\x00\x04m+2e+\xef\xbf\xbd"\x18\x00\xef\xbf\xbdh\xef\xbf\xbd#S\x07\x05\x07\x05\x13\x00..G\x01\xef\xbf\xbd\x17\x00\x04m,2e+-\xef\xbf\xbd\x18\x00\xef\xbf\xbdh\xef\xbf\xbd#S\x07\x05\x07\x05\x13\x00..G\x01\xef\xbf\xbd\x17\x00\x04m-2e+\x1d\xef\xbf\xbd'

#mes_find = post_reader.post_read(message)

# md = post_reader.do_POST(message)
# print(mes_find)


message_raw = b'--BoreyGA09\r\nContent-Disposition: form-data; name="CMD"\r\nContent-Type: text/plain\r\n\r\nDevVal\r\n--BoreyGA09\r\nContent-Disposition: form-data; name="DATA"\r\nContent-Type: application/octet-stream\r\nContent-Transfer-Encoding: binary\r\n\r\n\x18\x00\xaeh\x98#S\x07\x05\x07\x05\x13\x00\x8e(G\x01\xfd\x17\x00\x04m\x150e+\x01\xcb\'\x00\xb4L\x11\x01\x00\x00\x00\x00\x85\x10\x7f\x00\x00\x00\x00\x85 \x7f\x00\x00\x00\x00\x850\x7f\x00\x00\x00\x00\x01\xfd\x17\x00\x04m\x150e+q\xfb\x18\x00\xaeh\x98#S\x07\x05\x07\x05\x13\x00\x8e(G\x01\xfd\x17\x00\x04m\x160e+Q\x86\'\x00\xb4L\x11\x01\x00\x00\x00\x00\x85\x10\x7f\x00\x00\x00\x00\x85 \x7f\x00\x00\x00\x00\x850\x7f\x00\x00\x00\x00\x01\xfd\x17\x00\x04m\x160e+!\xb6\r\n--BoreyGA09--'


#print(len('2d2d426f726579474130390d0a436f6e74656e742d446973706f736974696f6e3a20666f726d2d646174613b206e616d653d22434d44220d0a436f6e74656e742d547970653a20746578742f706c61696e0d0a0d0a44657656616c0d0a2d2d426f726579474130390d0a436f6e74656e742d446973706f736974696f6e3a20666f726d2d646174613b206e616d653d2244415441220d0a436f6e74656e742d547970653a206170706c69636174696f6e2f6f637465742d73747265616d0d0a436f6e74656e742d5472616e736665722d456e636f64696e673a2062696e6172790d0a0d0a'))
raw_e1 = b'Content-Transfer-Encoding: binary\r\n\r\n'

raw_e2 = b'\r\n--BoreyGA09--'
start_hex = raw_e1.hex()
#print(start_hex)
finish_hex = raw_e2.hex()
#print(finish_hex)
messs = message_raw.hex()
#print(messs)
start = messs.find(start_hex) + len(start_hex)
finish = messs.find(finish_hex)
print(messs[start:finish])
print(len('1800ae689823530705070513008e284701fd1700046d1630652b5186'))

time_string = datetime.datetime.now()
time_string = time_string.strftime("%Y-%m-%d %H:%M:%S")
print(time_string)
print(float(int('00c28e28',16)))
convert('472e2e00')
# 008e2847
# 007a2847
# 48A16080
# 8060A148
'''
# raw = '1800b44c01000000000705130000404001fd1700046d2628662b30701800b44c01000000000705130000404001fd1700046d2828662b750e1800b44c01000000000705130000404001fd1700046d2d28662b85d91800b44c01000000000705130000404001fd1700046d3228662b5f681800b44c01000000000705130000404001fd1700046d3728662bafbf1800b44c01000000000705130000404001fd1700046d0029662b01db1800b44c01000000000705130000404001fd1700046d0529662bf10c1800b44c01000000000705130000404001fd1700046d0a29662b84491800b44c01000000000705130000404001fd1700046d0f29662b749e1800b44c01000000000705130000404001fd1700046d1429662b6ec31800b44c01000000000705130000404001fd1700046d1929662b7bf01800b44c01000000000705130000404001fd1700046d1e29662beb511800b44c01000000000705130000404001fd1700046d2329662b6a42'
raw = '1800b44c01000000000705130000404001fd1700046d2628662b30701800b44c01000000000705130000404001fd1700046d2828662b750e1800b44c01000000000705130000404001fd1700046d2d28662b85d91800b44c01000000000705130000404001fd1700046d3228662b5f681800b44c01000000000705130000404001fd1700046d3728662bafbf1800b44c01000000000705130000404001fd1700046d0029662b01db1800b44c01000000000705130000404001fd1700046d0529662bf10c1800b44c01000000000705130000404001fd1700046d0a29662b84491800b44c01000000000705130000404001fd1700046d0f29662b749e1800b44c01000000000705130000404001fd1700046d1429662b6ec31800b44c01000000000705130000404001fd1700046d1929662b7bf01800b44c01000000000705130000404001fd1700046d1e29662beb511800b44c01000000000705130000404001fd1700046d2329662b6a42'
def raw_parser(raw):
    f = len(raw)
    s = 0
    packets_list = []
    while s < f:
        #print(s)
        pack_len_h = raw[s+2:s+4]+ raw[s:s+2]
        pack_len = (int(pack_len_h,16)+4)*2
        print(pack_len)
        packet = raw[s:pack_len+s]
        print(packet)
        if pack_len == 56:
            packet_parser(pack_len,packet)
            packets_list.append(packet)
        else:
            packets_list.append(packet)
        # i = i - pack_len
        s = s + pack_len
        #print(raw)
    print(packets_list)
    return packets_list
packet_time = '0029662b' # '1530652b'# '002B5221' # '002A5126'
def time_parser(packet_time):
    '''
    {
                t->tm_min   = t_data[0] & 0x3F;
                t->tm_hour  = t_data[1] & 0x1F;
                t->tm_mday  = t_data[2] & 0x1F;
                t->tm_mon   = (t_data[3] & 0x0F) - 1; # borey без -1
                t->tm_year  = 100 + (((t_data[2] & 0xE0) >> 5) | # borey 2000 вместо 100
                              ((t_data[3] & 0xF0) >> 1));

            }
    '''
    tm_min = int(packet_time[0:2],16) & 0x3F
    tm_hour = int(packet_time[2:4],16) & 0x1F
    tm_mday = int(packet_time[4:6],16) & 0x1F
    tm_mon = int(packet_time[6:8],16) & 0x0F
    tm_year  = 1900 + 100 * ((int(packet_time[2:4],16) & 0x60)>>5) + ((((int(packet_time[4:6],16) & 0xE0) >> 5) |  ((int(packet_time[6:8],16) & 0xF0) >> 1)))

    # print(tm_min)
    # print(tm_hour)
    # print(tm_mday)
    # print(tm_mon)
    # print(tm_year)
    time_save = datetime.datetime(tm_year,tm_mon,tm_mday,tm_hour,tm_min)
    print(time_save)
    return time_save
def packet_parser(packet_len,packet):
    serial_num = packet[14:16] + packet[12:14] + packet[10:12] + packet[8:10]
    device_type = packet[18:20]
    if device_type == '07':
        device_type = 'счетчик воды'
        device_dim = packet[22:24]
        if device_dim == '13':
            device_dim = 'л'
        else:
            device_dim = 'м3'
    else:
        device_type = 'неизвестный тип прибора: ' + device_type
    device_data_hex = packet[30:32] + packet[28:30] + packet[26:28] + packet[24:26]
    device_data = convert(device_data_hex)
    packet_time_typeF =packet[44:46] + packet[46:48] + packet[48:50] + packet[50:52]
    print(packet_time_typeF)
    packet_time = time_parser(packet_time_typeF)
    print(serial_num + ' , ' + device_type + ' , ' + str(device_data) + ' ' + str(device_dim)+ ' ' + str(packet_time))


packets_list = raw_parser(raw)
# time_parser(packet_time)

i = 1
data_strip = 'Часть пакета №' + str(i)
for el in packets_list:
    if i == 1:
        data_strip = data_strip + " " + el
        i+=1
    else:
        data_strip = data_strip + " \n" + 'Часть пакета №' + str(i) + ' ' + el
        i+=1
print(data_strip)
