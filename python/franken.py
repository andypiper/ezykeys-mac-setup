import hid

# set constants for the USB ID
VID = 0xFEFD
PID = 0x0003


def prepare_text(message):
    """
    Prepares a message to be sent to the device.
    Convert to a list of int, padded to 20 chars,
    truncate if more than 20 chars
    """
    if len(message) > 20:
        message = message[:20]
    pad = 20 - len(message)
    list_chars = list(message) + [" "] * pad
    list_int = [ord(n) for n in list_chars]
    return list_int


msg = "1 2 3"

h = hid.device()
h.open(VID, PID)

# last value in initial list is row
# 0x00 = top, 0x01 = bottom
h.write([0x00, 0xFD, 0x01, 0x01] + prepare_text(msg))
h.close()
