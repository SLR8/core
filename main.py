import sys
from src.mqtt_client import mqtt_client

RUN_LOOP = False

def main():
    
    if len(sys.argv) != 1:
        if sys.argv[1] == 'run':
            print("Starting server")
            start_server(False)
        elif sys.argv[1] == 'loop':
            print('Starting server in loop mode')
            start_server(True)
        else:
            pass
        
    else : 
        print('** Help **')
        print('run - To run the server')
        print('loop - To run the server in loop mode')
def start_server(loop_mode ):
    print('Starting mqtt server')
    
    mqtt_client.connect()
    if loop_mode:
        mqtt_client.loop()


if __name__ == '__main__':
    main()