import serial.tools.list_ports

def get_open_serial_ports():
    """Get a list of all open serial ports."""
    open_ports = []
    ports = serial.tools.list_ports.comports()
    for port in ports:
        try:
            ser = serial.Serial(port.device)
            ser.close()
            open_ports.append(port.device)
        except serial.SerialException:
            pass
    return open_ports

# Example usage:
if __name__ == "__main__":
    open_ports = get_open_serial_ports()
    print("Open serial ports:", open_ports)
