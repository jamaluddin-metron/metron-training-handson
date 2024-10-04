import requests
import time
import json

url = 'http://127.0.0.1:8081/api'

log_array = [
    # Router Logs
"router1 INFO: Interface eth0 up, IP 192.168.1.1, MTU 1500",
"router1 WARNING: High latency detected on WAN interface, latency: 120ms",
"router1 INFO: DHCP request from 192.168.1.10 granted, lease time 24 hours",
"router1 ERROR: WAN connection lost, retrying...",
"router1 INFO: WAN connection restored, IP assigned: 203.0.113.5",

# Firewall Logs
"firewall1 ALLOW IN 192.168.1.50:5000 -> 203.0.113.15:1194 (UDP) [ALLOW VPN]",
"firewall1 ALERT IN 192.168.1.60:54326 -> 192.0.2.2:80 (TCP) [SUSPICIOUS]",
"firewall1 DENY IN 192.168.1.70:54327 -> 192.0.2.3:1-1024 (TCP) [BLOCKED PORT SCAN]",
"firewall1 ALLOW IN 192.168.1.80:54328 -> 192.168.1.90:8080 (TCP) [ALLOW LOCAL]",
"firewall1 DENY OUT 192.168.1.100:54329 -> 203.0.113.20:5000 (TCP) [SERVICE UNAVAILABLE]"
]


if __name__ == "__main__":
    while True:
        for log in log_array:
            data = {
                    'timestamp': int(time.time()),
                    'message': str(log),
                }
            requests.post(url, json=data)
            time.sleep(1)
        print("Logs Published Successfully!")
        time.sleep(30)