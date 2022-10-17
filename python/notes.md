```text
python
Python 3.10.8 (main, Oct 13 2022, 09:48:40) [Clang 14.0.0 (clang-1400.0.29.102)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import usb.core
>>> import usb.util
>>> dev = usb.core.find(idVendor=0xfefd, idProduct=0x0003)
>>> print(dev)
DEVICE ID fefd:0003 on Bus 001 Address 004 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x110 USB 1.1
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0xfefd
 idProduct              : 0x0003
 bcdDevice              :    0x2 Device 0.02
 iManufacturer          :    0x3 vial:f64c2b3c
 iProduct               :    0x2 0005
 iSerialNumber          :    0x3 vial:f64c2b3c
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 500 mA ==================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x5b (91 bytes)
   bNumInterfaces       :    0x3
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0
   bmAttributes         :   0xa0 Bus Powered, Remote Wakeup
   bMaxPower            :   0xfa (500 mA)
    INTERFACE 0: Human Interface Device ====================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x1
     bInterfaceClass    :    0x3 Human Interface Device
     bInterfaceSubClass :    0x1
     bInterfaceProtocol :    0x1
     iInterface         :    0x0
      ENDPOINT 0x81: Interrupt IN ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :    0x9 (9 bytes)
       bInterval        :    0xa
    INTERFACE 1: Human Interface Device ====================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x1
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :    0x3 Human Interface Device
     bInterfaceSubClass :    0x0
     bInterfaceProtocol :    0x0
     iInterface         :    0x0
      ENDPOINT 0x82: Interrupt IN ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x82 IN
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :   0x20 (32 bytes)
       bInterval        :    0x1
      ENDPOINT 0x3: Interrupt OUT ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x3 OUT
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :   0x20 (32 bytes)
       bInterval        :    0x1
    INTERFACE 2: Human Interface Device ====================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x2
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x1
     bInterfaceClass    :    0x3 Human Interface Device
     bInterfaceSubClass :    0x0
     bInterfaceProtocol :    0x0
     iInterface         :    0x0
      ENDPOINT 0x84: Interrupt IN ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x84 IN
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :   0x20 (32 bytes)
       bInterval        :    0xa
>>>
```

Using hid

```python
>>> import hid
>>> h = hid.device()
>>> h.open(0xFEFD, 0x0003)
>>> h.write([0x00,0xfd,0x01,0x01 + encode(b"there", 'hex') + [0x20] * 15)
```

(seems inconsistent / sometimes fails to open device)
