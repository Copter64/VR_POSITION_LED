import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.1.187', 5555)  # Replace with your server IP address

    try:
        client_socket.connect(server_address)
        print("Connected to server.")

        while True:
            data = client_socket.recv(1024).decode()

            # Check if the server closed the connection
            if not data:
                print("Server closed the connection.")
                break

            print("Received data:", data)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket when done
        client_socket.close()

if __name__ == "__main__":
    main()
