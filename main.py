import pyb


CRITICAL_THRESHOLD = 150
WARNING_THRESHOLD = 100

dac = pyb.DAC(1) # create a DAC object
adc = pyb.ADC('X22') #  setup X22 pin ADC channel
tim = pyb.Timer(6, freq=20000)

critical_pin = pyb.Pin.board.LED_RED
warning_pin = pyb.Pin.board.LED_YELLOW
works_pin = pyb.Pin.board.LED_BLUE


def record():
        buf = bytearray(20000) #  create a 20000 byte array to store samples
        adc.read_timed(buf, tim) #  start the ADC sampling
        return buf


while True:
        # 1 sec
        buf = record()
        delta = max(buf) - min(buf)

        if delta >= CRITICAL_THRESHOLD:
                critical_pin.on()
                warning_pin.off()
                works_pin.off()
        elif WARNING_THRESHOLD <= delta <= CRITICAL_THRESHOLD:
                critical_pin.off()
                warning_pin.on()
                works_pin.off()
        else:
                critical_pin.off()
                warning_pin.off()
                works_pin.on()

        print(delta, delta//10 * '|')
