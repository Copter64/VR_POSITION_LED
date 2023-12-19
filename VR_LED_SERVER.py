import socket
import openvr
import numpy as np
import time

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen(1)

    print("Waiting for connection...")
    client_socket, client_address = server_socket.accept()
    print("Connection from:", client_address)

    openvr.init(openvr.VRApplication_Scene)
    poses = []
    hmd = openvr.VRSystem()

    while True:
        # Create empty arrays to store pose data
        poses, _ = openvr.VRCompositor().waitGetPoses(poses, None)

        # Get the pose of the HMD
        hmd_pose = poses[openvr.k_unTrackedDeviceIndex_Hmd]

        # Check if the pose is valid
        if hmd_pose.bPoseIsValid:
            # Extract the position information from the HMD pose matrix
            print(hmd_pose.mDeviceToAbsoluteTracking)
            pos = np.array([hmd_pose.mDeviceToAbsoluteTracking[0][3], hmd_pose.mDeviceToAbsoluteTracking[1][3], hmd_pose.mDeviceToAbsoluteTracking[2][3]])

            # Send the positional data to the client
            time.sleep(1/60)
            client_socket.send(str(pos).encode())

    # Clean up and shutdown OpenVR
    openvr.shutdown()

if __name__ == "__main__":
    main()
