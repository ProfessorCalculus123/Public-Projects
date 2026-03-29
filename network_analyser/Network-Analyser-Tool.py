from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime           
import socket
import threading
SERVICE_MAP = {
        53: "DNS",
        80: "HTTP (WEB)",
        443: "HTTPS (SECURE WEB)",
        22: "SSH(Remote Access)",
        21: "FTP"
    }





def enhanced_scanner(target):
   
    try:
        hostname = socket.gethostbyaddr(target)[0]
    except socket.herror:
        hostname = "Unknown Name"
    print(f"\n---Scanning {target}--{hostname}---")
    
    for port in SERVICE_MAP.keys():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        
    
        if s.connect_ex((target, port)) == 0:
            service = SERVICE_MAP.get(port, "Unknown Service")    
            print(f"[+] {port:<5}) |  {service:<15} | OPEN")
        s.close()
hostname = socket.gethostname()
MY_IP = socket.gethostbyname(hostname)
TARGET_IP = input("Enter IP address or press enter: " )





    
if TARGET_IP == "":
    TARGET_IP = MY_IP


DNS_CACHE = {}
HOST_CACHE = {}
def packet_callback(packet):
    direction = "UNKNOWN"
    resolved_name = "UNKNOWN"
    if packet.haslayer(IP):
        src_ip = packet[IP].src 
        dst_ip = packet[IP].dst
        
        
        if src_ip == TARGET_IP or dst_ip == TARGET_IP:
                portinfo = "NONE" 
                timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                src_port= "N/A"
                dst_port= "N/A"
                proto = "Other"
                if packet.haslayer(TCP): 
                    proto = "TCP    "
                    src_port = packet[TCP].sport
                    dst_port = packet[TCP].dport
                    
                    
                elif packet.haslayer(UDP): 
                    proto = "UDP    "
                    src_port = packet[UDP].sport
                    dst_port = packet[UDP].dport
                else:
                    proto = "OTHER  "
                if dst_ip == MY_IP:
                    direction = "INBOUND"
                elif src_ip == MY_IP:
                    direction = "OUTBOUND"
                service_name = SERVICE_MAP.get(dst_port, SERVICE_MAP.get(src_port, "UNKNOWN"))
                portinfo = (f"{service_name}") if service_name != "UNKNOWN" else ""
                if src_ip == TARGET_IP or dst_ip == TARGET_IP:
                    for ip in [src_ip, dst_ip]:
                        if ip not in HOST_CACHE:
                            try:
                                name = socket.gethostbyaddr(ip)[0]
                                HOST_CACHE[ip] = name 
                            except socket.herror:
                                HOST_CACHE[ip] = ""
                
                
                if src_ip == TARGET_IP:
                   resolved_name = HOST_CACHE.get(dst_ip, dst_ip)
                else: 
                    resolved_name = HOST_CACHE.get(src_ip, src_ip) 
              
                print(f"[{timestamp}] {proto:5} | {src_ip}:{src_port} -> {dst_ip}:{dst_port} | {len(packet)} bytes |  {portinfo} | {direction} | { resolved_name}")
           
        
                

sniff_thread = threading.Thread(
    target=sniff,
    kwargs={
        'filter':f"host {TARGET_IP}",
        "prn": packet_callback,
        "store": 0
    },
    daemon=True
)
sniff_thread.start()


    



print(f"--- Monitoring live traffic for {TARGET_IP}---")
print("____________")
enhanced_scanner(TARGET_IP)
print("____________")

try:
    import time 
    print ("Press Ctrl+C to stop the monitor.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n Session Ending...")
   
        
