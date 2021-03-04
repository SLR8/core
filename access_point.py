from PyAccessPoint import pyaccesspoint
import time

access_point = pyaccesspoint.AccessPoint()

def start_ap():
    print("Starting ap ...")
    access_point.start()
    print("AP started succesfully")

def stop_ap():
    if access_point.is_running():
        access_point.stop()

start_ap()

time.sleep(10)

stop_ap()