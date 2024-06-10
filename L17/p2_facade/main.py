# from bluetooth_controller import BLEController
# from wifi_controller import WiFiController
# from pcb_controller import PCBController
#
# ble_controller = BLEController()


from facade import SystemController

system_controller = SystemController()
system_controller.init_system()
# Action
system_controller.turn_off_communication()
# Action
system_controller.shut_down_system()