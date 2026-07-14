import random


class Server:
    def __init__(self,name,cpu_usage=0,ram_usage=0,is_online=True):
        self.name = name
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.is_online = is_online

    def update_metrics(self):
        self.cpu_usage=random.randint(0,100)
        self.ram_usage=random.randint(0,100)

    def __str__(self):

        return f"Name:{self.name}, CPU:{self.cpu_usage}, RAM:{self.ram_usage}, ONLINE:{self.is_online}"


class Alarm:
        def __init__(self,server,message=''):
            self.message = message
            self.server = server


class EmailAlert(Alarm):
        def trigger(self):
            print(f"Email sent: server {self.server.name} is reporting {self.message}")


def run_monitor(servers):
        for server in servers:
            if server.is_online:
                server.update_metrics()
            print(server)

            if server.cpu_usage>80:
                alert = EmailAlert(server, "CRITICAL")
                alert.trigger()

servers=[Server("webnode"),Server("database")]



run_monitor(servers)
