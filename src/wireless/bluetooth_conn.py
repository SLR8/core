import bluetooth

print('Scanning for bluetooth devices')

devices = bluetooth.discover_devices(lookup_names=True, lookup_class= True)

number_of_devices = len(devices)
print(f'Devices found {number_of_devices}')

for addr, name, device_class in devices:
    print('\n')
    print('Device')
    print(f'Device name {name}')
    print(f'Device mac address {addr}')
    print(f'Device class {device_class}')