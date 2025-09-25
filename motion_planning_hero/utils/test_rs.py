import pyrealsense2 as rs

# Configure depth stream
pipeline = rs.pipeline()
config = rs.config()
config.enable_device("TODO")
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Start streaming
pipeline.start(config)

try:
    while True:
        # Wait for a frame set
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            continue

        # Do something simple, like print
        print("Got a depth frame")

except KeyboardInterrupt:
    # Stop streaming on Ctrl+C
    print("Stopping...")
finally:
    pipeline.stop()