
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
    """
    gjsdhfshdfhksdfk
    sdfjsdfjksdfsd
    sdfnmsdfnsdnf
    """
    blocked_ips = []
    
    def __init__(self, dis_ip = None):
        self.dis_ip = dis_ip

    def block_ip(self, ip):
        if ip in FirewallLog.blocked_ips:
            print("IP is already blocked")
        else:
            FirewallLog.blocked_ips.append(ip)

    def read_logs(self, path):
        with open(path, "r") as f:
            return f.readlins()

    def check_log(self, log):
        if "Failed login" in log:
            return True
        else:
            return False

    def extract_ip(self, log):
        ...


if __name__ == "__main__":

    fire = FirewallLog()
    for log in ("soc_logs.log"):
        if fire.check_log(log):
            ip = fire.extract_ip(log)
            fire.block_ip(ip)
        else:
            continue


    