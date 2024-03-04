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

def open_serial_connection(port, baud_rate):
    """Open a serial connection to the specified port with the given baud rate."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)  # Adjust timeout as needed
        return ser
    except serial.SerialException:
        print(f"Failed to open serial connection to {port}")
        return None

def send_command(ser, command):
    """Send a command over the serial connection."""
    try:
        arg = bytes(str(command), 'utf8') + b'\r'
        ser.write(arg)
        print (ser.readlines())
        print(f"Command '{command}' sent successfully")
    except Exception as e:
        print(f"Failed to send command '{command}': {e}")

def close_serial_connection(ser):
    """Close the serial connection."""
    try:
        ser.close()
        print("Serial connection closed successfully")
    except Exception as e:
        print(f"Failed to close serial connection: {e}")

# Example usage:
if __name__ == "__main__":
    open_ports = get_open_serial_ports()
    print("Open serial ports:", open_ports)

    # Example: Open connection to COM6 with baud rate 9600
    com6_connection = open_serial_connection("COM6", 115200)
    if com6_connection:
        print("Successfully opened connection to COM6")
        send_command(com6_connection, "start 0 ")
        close_serial_connection(com6_connection)
    else:
        print("Failed to open connection to COM6")
