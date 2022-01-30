"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""
import ipaddress
import platform
import subprocess


def host_ping(networks: list):
    for network in networks:
        try:
            ip = ipaddress.ip_address(network)
            command = ['ping', param, '1', str(ip)]
        except ValueError:
            host = network
            command = ['ping', param, '1', host]
        if subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            print('Узел доступен')
        else:
            print('Узел недоступен')


if __name__ == '__main__':
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    host_ping(['ya.ru', '127.0.0.1', '2.2.2.2'])
