import usb
import dbus


busses = usb.busses()
for bus in busses:
  devices = bus.devices
  for dev in devices:
    print repr(dev)
    print "Device:", dev.filename
    print "  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor)
    print "  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct)
    print "Manufacturer:", dev.iManufacturer
    print "Serial:", dev.iSerialNumber
    print "Product:", dev.iProduct


bus = dbus.SystemBus()
ud_manager_obj = bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
ud_manager = dbus.Interface(ud_manager_obj, 'org.freedesktop.UDisks')

for dev in ud_manager.EnumerateDevices():
    device_obj = bus.get_object("org.freedesktop.UDisks", dev)
    device_props = dbus.Interface(device_obj, dbus.PROPERTIES_IFACE)
    print device_props.Get('org.freedesktop.UDisks.Device', "DriveVendor")
    print device_props.Get('org.freedesktop.UDisks.Device', "DeviceMountPaths")
    print device_props.Get('org.freedesktop.UDisks.Device', "DriveSerial")
    print device_props.Get('org.freedesktop.UDisks.Device', "PartitionSize")
