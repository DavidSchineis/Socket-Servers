# Iterative Socket Server, Multi-Threaded Client  

# Import Libraries
import socket
import threading
import time 
import sys

# Global List to Store Turn-Around Times
turn_around_times = []

def client_task(server_address, port, operation):
    try:
        start_time = time.time()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((server_address, port))

            # Send Request
            sock.sendall(operation.encode('utf-8'))

            # Receive Response
            response = ''
            while True:
                data = sock.recv(4096).decode('utf-8')
                if not data:
                    break
                response += data

            end_time = time.time()
            turn_around_time = (end_time - start_time) * 1000
            turn_around_times.append(turn_around_time)

            if operation == "goodbye_world": sys.exit()

            # Output Response and Turn-Around Time
            print(f"\n--- Client Response ---")
            print(f"Turn-around Time: {turn_around_time:.2f} ms")
            print("Response from server:")
            print(response)
            response = ''

    except Exception as e:
        print(f"Client exception: {e}")

def main():
    # Request Network Address and Port
    server_address = input("Enter server IP address: ")
    port = int(input("Enter server port number: "))

    while True:
        # Request Operation
        print("\nSelect operation to request:")
        print("1. Date and Time")
        print("2. Uptime")
        print("3. Memory Use")
        print("4. Netstat")
        print("5. Current Users")
        print("6. Running Processes")
        print("7. Exit Program")
        choice = input("Enter choice (1-7): ")

        operations = {
            '1': "Date and Time",
            '2': "Uptime",
            '3': "Memory Use",
            '4': "Netstat",
            '5': "Current Users",
            '6': "Running Processes",
            '7': "Exit Program",
            'goodbye_world':"goodbye_world"
        }

        operation = operations.get(choice)
        if not operation:
            print("Invalid choice. Please reconnect and reconsider your choice.")
            sys.exit()

        if operation == "Exit Program":
            print("Exiting program.")
            sys.exit()
        
        # Request Number of Client Requests to Generate
        if operation == "goodbye_world":
            num_requests = 1
        else:   
            num_requests = int(input("\nEnter number of client requests to generate (1, 5, 10, 15, 20, 25): "))

        if num_requests not in [1, 5, 10, 15, 20, 25]:
            print("Invalid number of client requests.")
            sys.exit()

        threads = []

        # Start Client Threads
        for _ in range(num_requests):
            thread = threading.Thread(target=client_task, args=(server_address, port, operation))
            threads.append(thread)
            thread.start()
            time.sleep(0.05)

        # Wait for All Threads to Complete
        for thread in threads:
            thread.join()

        # Collect and Display Turn-Around Times
        total_time = sum(turn_around_times)
        average_time = total_time / len(turn_around_times) if turn_around_times else 0
        turn_around_times.clear()

        if operation == "goodbye_world": sys.exit()

        print("\n--- Turn-around Time Summary ---")
        print(f"Total Turn-around Time: {total_time:.2f} ms")
        print(f"Average Turn-around Time: {average_time:.2f} ms")

if __name__ == "__main__":
    main()
    