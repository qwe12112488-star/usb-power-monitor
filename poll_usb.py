import wmi
import time

c = wmi.WMI()

def poll_usb_power():
    for usb in c.Win32_USBControllerDevice():
        dep = usb.Dependent
        if any(k in dep.Description for k in ["Mouse", "Keyboard", "Audio", "HID"]):
            print(f"[{dep.DeviceID}] {dep.Description} | Status: {dep.Status} | PowerMgmt: {dep.PowerManagementSupported}")

while True:
    poll_usb_power()
    time.sleep(1)
