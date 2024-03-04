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

def open_serial_connection(port):
    """Open a serial connection to the specified port."""
    try:
        ser = serial.Serial(port)
        return ser
    except serial.SerialException:
        print(f"Failed to open serial connection to {port}")
        return None

# Example usage:
if __name__ == "__main__":
    open_ports = get_open_serial_ports()
    print("Open serial ports:", open_ports)

    # Example: Open connection to COM6
    com6_connection = open_serial_connection("COM6")
    if com6_connection:
        print("Successfully opened connection to COM6")
    else:
        print("Failed to open connection to COM6")
