import pyrealsense2 as rs

# Create a context object
realsense_ctx = rs.context()

# Get the serial numbers of connected devices
connected_devices = []
for i in range(len(realsense_ctx.devices)):
    serial_number = realsense_ctx.devices[i].get_info(rs.camera_info.serial_number)
    connected_devices.append(serial_number)

# Print the serial numbers
print("Connected RealSense Camera Serial Numbers:", connected_devices)