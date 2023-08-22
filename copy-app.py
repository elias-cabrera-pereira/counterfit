import time
import read_thingspeak
import send_thingspeak
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

CounterFitConnection.init('127.0.0.1', 5000)
light_sensor = GroveLightSensor(0)
led = GroveLed(5)

while True:
    if CounterFitConnection.is_connected:
        luz = light_sensor.light
        send_thingspeak.thingspeak_send(luz)
        valor = read_thingspeak.thingspeak_receive()
        if valor < 300:
            led.on()
        else:
            led.off()

        time.sleep(15)    
    else:
        print("No esta conectado Counterfit...")
        break

