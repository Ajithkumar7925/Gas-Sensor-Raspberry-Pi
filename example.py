from mq import *
import sys, time
try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen
myAPI = '3CUMOGTM5V2JA2CL'
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
        conn = urlopen(baseURL + '&field1=%f' % (mq))
        conn.close()
        sys.stdout.flush()
        time.sleep(0.1)
        

except:
    print("\nAbort by user")
