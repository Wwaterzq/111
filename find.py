import ssl
import socket

target_domain = "aliyun.com"
target_port = 443

context = ssl.create_default_context()
with socket.create_connection((target_domain, target_port)) as sock:
    with context.wrap_socket(sock, server_hostname=target_domain) as ssock:
        cert = ssock.getpeercert()

san_list = cert.get("subjectAltName", [])

related_domains = set()
for entry in san_list:
    entry_type, entry_value = entry
    if entry_type == "DNS":
        related_domains.add(entry_value)
related_domains.discard(target_domain)


print(related_domains)
