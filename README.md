# Socket Servers
>Two types of socket servers implemented in Python to highlight different approaches to handling multiple client connections.

## Features

* Iterative Server handles client requests one at a time.
* Concurrent Server handles multiple clients requests simultaneously using threading.
* Multi-threaded clients to simulate multiple requests concurrently.
* Supports system commands like Date and Time, Uptime, Memory Usage, Netstat, Current Users, and Running Processes.
* Performance benchmarking with turn-around time analysis.

## Iterative Server (Single-Threaded)

* Accepts one client connection at a time.
* Suitable for low-traffic applications where resources are limited.
* Outperforms concurrent server at smaller commands in low-client environments.

## Concurrent Server (Multi-Threaded)

* Uses threading to handle multiple client connections simultaneously.
* Efficient for high-traffic applications requiring parallel processing.
* Outperforms iterative server in unpredictable and high-demand environments.

## How to Run
Clone this repository
```bash
git clone https://github.com/DavidSchineis/Socket-Servers.git
```

Ensure Python 3.8+ is installed and install required libraries:
```bash
pip install -r assets/requirements.txt
```

Run the Iterative Server:
```bash
cd Iterative-Server
python server.py
```

Run the Concurrent Server:
```bash
cd Concurrent-Server
python server.py
```

Run the corresponding client in another terminal:
```bash
python client.py
```
