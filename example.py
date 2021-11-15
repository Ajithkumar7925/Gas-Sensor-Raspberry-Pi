from mq import *
import sys, time
try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

# Enter Your API key here
myAPI = 'HKY5YG9F5ZWBHOEQ' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
        sys.stdout.flush()
        time.sleep(0.1)
        conn = urllib2.urlopen(baseURL + '&field1=%f' % (perc))
        conn.close()

except:
    print("\nAbort by user")
