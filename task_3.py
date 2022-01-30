"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable  Unreachable
10.0.0.1   10.0.0.3
10.0.0.2   10.0.0.4
"""
import subprocess
import platform

from tabulate import tabulate

from task_2 import check_vars


def host_range_ping_tab(start_ip, end_ip):
    status, ip, octets = check_vars(start_ip, end_ip)
    ip_draft = '.'.join(octets[:3])
    if status:
        host_list = [f'{ip_draft}.{str(octet)}' for octet in range(end_ip)]
        result = {'Reachable': [], 'Unreachable': []}
        for host in host_list:
            command = ['ping', param, '1', host]
            if subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                result['Reachable'].append(host)
            else:
                result['Unreachable'].append(host)
        print(tabulate(result, headers=list(result.keys())))


if __name__ == '__main__':
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    host_range_ping_tab(start_ip='127.0.0.1', end_ip=5)
