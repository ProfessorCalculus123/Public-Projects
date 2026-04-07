import objc
from CoreWLAN import CWWiFiClient
import time

def get_wifi_info():
    client = CWWiFiClient.sharedWiFiClient()
    interface = client.interface()
    return interface.ssid(), interface.rssiValue()

print("--- M5 MacBook Signal Tracker ---")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        ssid, rssi = get_wifi_info()
        
        if rssi != 0:
            # Bar logic
            bar_level = max(0, min(20, int((rssi + 100) / 3.5)))
            bar = "█" * bar_level + "-" * (20 - bar_level)
            
            # Label logic
            if rssi >= -30: label = "Perfect"
            elif -50 <= rssi < -30: label = "Amazing"
            elif -60 <= rssi < -50: label = "Excellent"
            elif -70 <= rssi < -60: label = "Good"
            elif -80 <= rssi < -70: label = "Weak"
            elif -90 <= rssi < -80: label = "Dead Zone"
            else: label = "Noise"
            
            # Use .ljust() to clear old characters from the line
            output = f"\rNetwork: {ssid} | Signal: [{bar}] {rssi} dBm ({label})"
            print(output.ljust(80), end="")
        else:
            print("\rSignal not found. Check Location Services.".ljust(80), end="")
        
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n\nScan complete. Ready to log this to a file?")