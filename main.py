
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, password):
        if self.password == password:
            print(f"user: {self.username} is authenticated")
        else:
            print("Password is wrong ! ")



class FirewallLog:

    blocked_ips = []
    
    def __init__(self, source_ip, dis_ip, action):
        self.source_ip = source_ip
        self.dis_ip = dis_ip
        self.action = action

    def block_ip(self, ip):
        if ip in FirewallLog.blocked_ips:
            print("IP is already blocked")
        else:
            FirewallLog.blocked_ips.append(ip)


    