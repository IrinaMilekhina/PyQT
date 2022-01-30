"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен
только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""
import ipaddress

from task_1 import host_ping


def check_vars(start_ip, end_ip):
    try:
        ip = ipaddress.ip_address(start_ip)
    except ValueError:
        return print('Стартовым значением должен быть ip адрес')
    if not isinstance(end_ip, int):
        return print('Диапазон должен быть числом')
    octets = str(ip).split('.')
    if int(octets[-1]) + end_ip > 254:
        return print(f'Максимальное число для привоерки {254 - int(octets[-1])}')
    return True, ip, octets


def host_range_ping(start_ip, end_ip):
    status, ip, octets = check_vars(start_ip, end_ip)
    ip_draft = '.'.join(octets[:3])
    if status:
        host_list = [f'{ip_draft}.{str(octet)}' for octet in range(end_ip)]
        return host_ping(host_list)


if __name__ == '__main__':
    host_range_ping(start_ip='127.0.0.1', end_ip=24)
