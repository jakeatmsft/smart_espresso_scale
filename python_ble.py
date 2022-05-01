import asyncio
from bleak import BleakScanner

def detection_callback(device, advertisement_data):
    if(device.address == '50:FB:19:87:D1:51'):
        #print(device.address, "RSSI:", device.rssi, advertisement_data)
        #print(advertisement_data.manufacturer_data[4298])
        hex_str = '0x'+advertisement_data.manufacturer_data[4298][4:6].hex()
        hex_int = int(hex_str, 16)
        print(hex_int/100)
        
scanner = BleakScanner()
scanner.register_detection_callback(detection_callback)
await scanner.start()
await asyncio.sleep(5.0)
await scanner.stop()