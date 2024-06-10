from sensor import Sensor
from subscribers import MobileClient, WebClient

sensor = Sensor()

mobile_client = MobileClient()
web_client = WebClient()

sensor.subscribe(mobile_client)
sensor.subscribe(web_client)

sensor.notify_all()
sensor.notify(mobile_client)