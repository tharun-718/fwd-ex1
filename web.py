from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
        <head>
            <title>TCP/IP Protocol Suite</title>
        </head>

        <body style="font-family:Arial; background-color:#f4f6f9;">

        <h1 align="center" style="color:blue;">
            TCP/IP PROTOCOL SUITE
        </h1>

        <table border="1" cellpadding="15"
        cellspacing="0" align="center"
        style="border-collapse:collapse; width:75%;">

        <tr style="background-color:#333366; color:white;">
            <th>Layer</th>
            <th>Protocols</th>
        </tr>

        <tr style="background-color:#ffcccc;">
            <td><b>Application Layer</b></td>
            <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP</td>
        </tr>

        <tr style="background-color:#fff0b3;">
            <td><b>Transport Layer</b></td>
            <td>TCP, UDP</td>
        </tr>

        <tr style="background-color:#ccffcc;">
            <td><b>Internet Layer</b></td>
            <td>IP, ICMP, IGMP</td>
        </tr>

        <tr style="background-color:#cce5ff;">
            <td><b>Network Access Layer</b></td>
            <td>Ethernet, Wi-Fi, PPP, ARP</td>
        </tr>

        </table>

        <h3 align="center" style="color:green;">
            Welcome to Python Web Server
        </h3>

        </body>
        </html>
        """

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',870)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()