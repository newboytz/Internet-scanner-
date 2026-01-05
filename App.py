import socket

def port_scanner(target_ip):
    # Orodha ya milango (ports) muhimu
    ports = [21, 22, 80, 443, 3306, 8080]
    
    print(f"\n--- Inaanza kukagua: {target_ip} ---")
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port}: IKO WAZI (OPEN) ✅")
        else:
            print(f"Port {port}: IMEFUNGWA (CLOSED) ❌")
        s.close()

if __name__ == "__main__":
    # Inamruhusu mtumiaji kuandika IP au Tovuti
    target = input("Ingiza URL/IP ya kukagua (mfano: google.com): ")
    if not target:
        target = "google.com"
    port_scanner(target)
    
      
