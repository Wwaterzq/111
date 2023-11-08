import socket

url = "ac.aliyun.com"
port = 80

# 构造 HTTP GET 请求报文
request = f"GET / HTTP/1.1\r\nHost: {url}\r\n\r\n"

host = "aliyun.com"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    # 发送 HTTP 请求
    s.sendall(request.encode())
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data

print(response.decode())
