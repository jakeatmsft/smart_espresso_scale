from pylive import live_plotter
import numpy as np
import asyncio
from bleak import BleakScanner

loop = asyncio.get_event_loop()

size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.linspace(0,1,size+1)[0:-1]
line1 = []

def detection_callback(device, advertisement_data):
    global y_vec, y_vec, size, line1
    if(device.address == '50:FB:19:87:D1:51'):
        #print(device.address, "RSSI:", device.rssi, advertisement_data)
        #print(advertisement_data.manufacturer_data[4298])
        hex_str = '0x'+advertisement_data.manufacturer_data[4298][4:6].hex()
        hex_int = int(hex_str, 16)
        #print(hex_int/100)
        y_vec[-1] = hex_int/100
        line1 = live_plotter(x_vec,y_vec,line1)
        y_vec = np.append(y_vec[1:],0.0)

        
async def start():
    scanner = BleakScanner()
    scanner.register_detection_callback(detection_callback)
    await scanner.start()
    await asyncio.sleep(30.0)
    await scanner.stop()

def signal_handler(signal, frame):
    loop.stop()
    sys.exit(0)        

asyncio.ensure_future(start())
loop.run_forever()

#while True:
#    rand_val = np.random.randn(1)
#    y_vec[-1] = rand_val
#    line1 = live_plotter(x_vec,y_vec,line1)
#    y_vec = np.append(y_vec[1:],0.0)