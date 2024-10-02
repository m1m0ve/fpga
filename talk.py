from serial import Serial
from pathlib import Path

class SerialCommunicator:
    def __init__(self, devices=["/dev/ttyUSB0", "/dev/ttyUSB1"], active_device=1):
        self.devices = devices
        self.active_device = active_device
        self.ser = None

    def connect(self):
        path = Path(self.devices[self.active_device])
        if path.exists():
            try:
                self.ser = Serial(self.devices[self.active_device])
                print(f"Adapter: {self.ser.name}\n")
                return True
            except Exception as e:
                print(f"Error connecting to {path}: {e}")
                return False
        else:
            print("Failed to find serial port!\n")
            print(f"Ensure {path} is the correct port and is plugged in.\n")
            return False

    def disconnect(self):
        if self.ser:
            self.ser.close()
            print("Disconnected from serial port.")

    def read(self, num_bytes=10):
        if not self.ser:
            print("Not connected to any serial port.")
            return None
        try:
            data = self.ser.read(num_bytes)
            print(f"Read data: {data}")
            return data
        except Exception as e:
            print(f"Error reading from serial port: {e}")
            return None

    def write(self, data):
        if not self.ser:
            print("Not connected to any serial port.")
            return False
        try:
            self.ser.write(data)
            print(f"Wrote data: {data}")
            return True
        except Exception as e:
            print(f"Error writing to serial port: {e}")
            return False

# Example usage:
if __name__ == "__main__":
    comm = SerialCommunicator()
    if comm.connect():
        with open("blinky.bit","rb") as file:
         
          data = file.read()
          comm.write(data)

          comm.disconnect()
