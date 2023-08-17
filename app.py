import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

CounterFitConnection.init('127.0.0.1', 5000)
light_sensor = GroveLightSensor(0)
led = GroveLed(5)

while True:
    if CounterFitConnection.is_connected:
        luz = light_sensor.light
        if luz > 300:
            led.on()
        else:
            led.off()
    else:
        print("No esta conectado Counterfit...")
        break

    time.sleep(1)