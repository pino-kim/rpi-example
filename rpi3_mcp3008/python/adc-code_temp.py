import spidev
import time

#Define Variables
delay = 0.5
ldr_channel = 1

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    # send start code first, ldr_channel code, etc ...
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
    
 
while True:
    ldr_value = readadc(ldr_channel)
    print "---------------------------------------"
    temp = 5.0 * ldr_value * 100 / 1024 
    print("CH1 Value: %d" % ldr_value)
    print("Current Temp : %d"  %  temp)

    time.sleep(delay)
