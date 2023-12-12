# QuickShare WebServer


## Console
![Image 1](https://github.com/Tiegertropfen119-0001/QuickShare-WebServer/blob/main/img/image1.png) 
## Web
![Image 2](https://github.com/Tiegertropfen119-0001/QuickShare-WebServer/blob/main/img/image2.png) 

## What is this?

QuickShare WebServer is a simple Python program that allows you to create a web server for instant file sharing. You can use either the Python script or the precompiled executable version.

## Icon

[Web Icon](https://www.flaticon.com/free-icon/internet_10453141?term=web&page=1&position=19&origin=search&related_id=10453141)

## Project Description

The QuickShare WebServer script creates a web server that enables instant file sharing. It utilizes Python's `http.server` module to handle HTTP requests. The web server provides a directory listing with file details such as size and creation time. Additionally, it includes a basic HTML interface with a home button for easy navigation.

## Usage

1. Run the Python script or the precompiled executable.
2. Access the server using the provided local IP and port.

## Project Structure

- `webserver.py` or `webserver.exe`: Main script or executable file.
- `static`: Directory for static files (e.g., images, stylesheets).
- `README.md`: Project documentation.

## Dependencies

- Python 3.x

## Imports
`import http.server
import socketserver
import os
import socket
import time`

## Notes
The server is accessible within the local network (LAN) only.
