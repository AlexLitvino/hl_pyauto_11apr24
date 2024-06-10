from bluetooth_controller import BLEController
from wifi_controller import WiFiController
from pcb_controller import PCBController


class SystemController:

    def __init__(self):
        self._pcb_controller = PCBController()
        self._wifi_controller = WiFiController()
        self._ble_controller = BLEController()

    def turn_on_communication(self):
        self._ble_controller.turn_on_ble()
        self._wifi_controller.turn_on_wifi()
        print()

    def turn_off_communication(self):
        self._ble_controller.turn_off_ble()
        self._wifi_controller.turn_off_wifi()
        print()

    def init_system(self):
        self._pcb_controller.turn_on_pcb()
        self.turn_on_communication()
        print()

    def shut_down_system(self):
        self.turn_off_communication()
        self._pcb_controller.turn_off_pcb()
