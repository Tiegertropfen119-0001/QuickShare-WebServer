import http.server
import socketserver
import os
import socket
import time

# Define the port on which the server will run
PORT = 8080

# CustomHandler class to handle HTTP requests
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            # List files in the directory, excluding 'webserver.py' and 'webserver.exe'
            files = os.listdir(path)
            # Send a response indicating a successful request
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Generate an HTML page with the directory listing
            files_list = '\n'.join(
                f'<li><a href="{file}">{file}</a> ({os.path.getsize(os.path.join(path, file))} bytes, {time.ctime(os.path.getctime(os.path.join(path, file)))})</li>'
                for file in files)
            output = f"""
            <!DOCTYPE HTML>
            <html lang="en">
            <head>
            <meta charset="utf-8">
            <title>QuickShare - WebServer</title>
            <!-- Styles for the HTML page -->
            <style>
            /* Styles for the HTML page */
            body {{
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }}
            h1 {{
                color: #333;
            }}
            hr {{
                border: 0;
                border-top: 1px solid #ccc;
                margin: 20px 0;
            }}
            ul {{
                list-style: none;
                padding: 0;
                margin: 0;
            }}
            li {{
                margin: 10px 0;
            }}
            a {{
                text-decoration: none;
                color: #0066cc;
                font-weight: bold;
                transition: color 0.3s;
            }}
            a:hover {{
                color: #004080;
            }}
            p {{
                font-size: 12px;
                text-align: center;
                color: #666;
            }}
            #home-button {{
                left: 10px;
                top: 10px;
                padding: 5px 20px;
                font-size: 16px;
                background-color: #0066cc;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
            }}
            #home-button:hover {{
                background-color: #004080;
            }}
            </style>
            </head>
            <body>
            <!-- HTML body content -->
            <h1>Directory listing for /</h1>
            <hr>
            <ul>
            {files_list}
            </ul>
            <hr>
            <!-- Home button with an onclick event to navigate back to the server's home page -->
            <button id="home-button" onclick="location.href='http://{get_local_ip()}:{PORT}';">Home</button>
            <p>Check my GitHub :)</p>
            <p>https://github.com/Tiegertropfen119-0001/QuickShare-WebServer</p>
            </body>
            </html>
            """
            # Write the HTML output to the response
            self.wfile.write(output.encode())
        except Exception as e:
            print(f"[Error] => {e}")

# Function to get the local IP address of the machine
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable; connect to an external server
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Function to print server information and start serving requests
def server_load():
    print(f"Server online at : \n Public (LAN ONLY) : http://{get_local_ip()}:{PORT}")
    httpd.serve_forever()

# Main function
def main():
    # Load the server
    server_load()

# Create a TCP server instance with the specified IP address and port, using the CustomHandler
httpd = socketserver.TCPServer((str(get_local_ip()), PORT), CustomHandler)

# Entry point for the script
if __name__ == "__main__":
    main()
