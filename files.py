ips = ["192.168.1.5", "185.22.33.44", "10.0.0.1"]


with open("data/ips.txt", "a", encoding="utf-8") as file:
    for ip in ips:
        file.write(f"{ip}\n")