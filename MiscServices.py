import urllib, json, socket, os, datetime, time

class MiscServices:

    def getExternalIp(self):
        return json.loads(urllib.urlopen("http://ip.jsontest.com/").read())['ip']
        
    def getHostName(self):
        return socket.getfqdn()

    def getTemperature(self):
        f = os.popen('cat /sys/class/thermal/thermal_zone0/temp')
        fs = f.read()
        celcius = int(fs)/1000
        return "%d'C" % celcius

    def getCurrentDateTime(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    def getTimezone(self):
        return time.tzname[0]
        
if __name__ == "__main__":
    misc_svc = MiscServices()
    print misc_svc.getExternalIp()
    print misc_svc.getHostName()
    print misc_svc.getTemperature()
    print misc_svc.getCurrentDateTime()
    print misc_svc.getTimezone()
