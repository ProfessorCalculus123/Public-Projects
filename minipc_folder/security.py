import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
def cybersec():
    def Net_Analyser():
        try:
            from scapy.all import sniff, IP, TCP, UDP
        except ImportError:
            print("\n[!] Error: The 'scapy' module is not installed in the current Python environment.")
            print("[!] It looks like you might have multiple Python versions.")
            print("[!] Try running the script using:")
            print("    python3 mini_pc.py")
            print("[!] Or install it explicitly for this environment by running:")
            print("    python3 -m pip install scapy")
            input("\nPress Enter to return to the previous menu...")
            return

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

        global exit_choice, app
        app = 10

        while True:
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
            TARGET_IP = input("Enter IP address or press enter: ")
            if TARGET_IP.lower() == 'q': break 

            if TARGET_IP == "":
                TARGET_IP = MY_IP

            DNS_CACHE = {}
            HOST_CACHE = {}
            
            stop_event = threading.Event()

            def packet_callback(packet):
                if stop_event.is_set():
                    return
                direction = "UNKNOWN"
                resolved_name = "UNKNOWN"
                if packet.haslayer(IP):
                    src_ip = packet[IP].src 
                    dst_ip = packet[IP].dst
            
                    if src_ip == TARGET_IP or dst_ip == TARGET_IP:
                        portinfo = "NONE" 
                        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                        src_port = "N/A"
                        dst_port = "N/A"
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
            
                        print(f"[{timestamp}] {proto:5} | {src_ip}:{src_port} -> {dst_ip}:{dst_port} | {len(packet)} bytes |  {portinfo} | {direction} | {resolved_name}")

            def stop_filter_fn(packet):
                return stop_event.is_set()

            sniff_thread = threading.Thread(
                target=sniff,
                kwargs={
                    'filter': f"host {TARGET_IP}",
                    "prn": packet_callback,
                    "store": 0,
                    "stop_filter": stop_filter_fn
                },
                daemon=True
            )
            sniff_thread.start()

            print(f"--- Monitoring live traffic for {TARGET_IP}---")
            print("____________")
            enhanced_scanner(TARGET_IP)
            print("____________")

            try:
                print("Press Enter to stop the monitor.")
                input("")
            except KeyboardInterrupt:
                pass
                
            stop_event.set()
            print("\n Session Ending...")

            exit_choice = input("Start Again (y/n): ")
            if exit_choice.lower() in ["y", "yes", ""]:
                clear_console()
                continue
            else:
                clear_console()
                break

    while True:
        print("______________________________")
        print("Cyber Security Tools:")
        print("1.Network Analyser")
        print("2.Exit")
        print("______________________________")
        option = input("Choose An Option (1-2): ")
        clear_console()
        print("\n\n")
        try:
            option_int = int(option)
        except ValueError:
            clear_console()
            continue
        
        if option_int == 1:
            clear_console()
            Net_Analyser()
        elif option_int == 2:
            clear_console()
            break
        else:
            clear_console()
def run():
   cybersec()
if __name__ == "__main__":
    run()
