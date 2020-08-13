from influxdb import InfluxDBClient as influx
import requests as rq
import json
from time import sleep as t
cliente = influx(database='covid')
while 1:
    h=rq.get("https://api.thingspeak.com/channels/1113372/feeds.json?results=2")
    j=json.loads(h.content)
    temp=j['feeds'][0]['field1']
    data = []
    data.append("paciente,tag=0 val={}".format(temp))
    cliente.write_points(data, database='', time_precision='s', protocol='line')
    print(temp,hum)
    t(2)