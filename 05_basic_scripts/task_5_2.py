# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
# ip_network = input()
# network, mask = ip_network.split('/')
# octets = network.split('.')
# bin_mask = '1' * int(mask) + '0' * (32 - int(mask))
# 
# if int(mask) < 32:
#     hostadd = octets
#     hostbin = ' '.join([bin(int(octet))[2:].zfill(8) for octet in hostadd])
#     netbin = hostbin[:int(mask)] + '0' * (32 - int(mask))
#     octets = [int (netbin[i:i+8], 2) for i in range (0, 32, 8)]
# print('Network:\n'
#       f'{octets[0]:<10} {octets[1]:<10} {octets[2]:<10} {octets[3]:<10}\n'
#       f'{int(octets[0]):08b} {int(octets[1]):08b} {int(octets[2]):08b} {int(octets[3]):08b}\n\n'
#       'Mask:\n'
#       f'/{mask}\n'
#       f'{int(bin_mask[0:8], 2):<10} {int(bin_mask[8:16], 2):<10} {int(bin_mask[16:24], 2):<10} {int(bin_mask[24:32], 2):<10}\n'
#       f'{int(bin_mask[0:8], 2):08b}   {int(bin_mask[8:16], 2):08b}   {int(bin_mask[16:24], 2):08b}   {int(bin_mask[24:32], 2):08b}')

# network = input("IP: ")
# 
# ip, mask = network.split("/")
# ip_list = ip.split(".")
# mask = int(mask)
# 
# oct1, oct2, oct3, oct4 = [
#     int(ip_list[0]),
#     int(ip_list[1]),
#     int(ip_list[2]),
#     int(ip_list[3]),
# ]
# 
# bin_mask = "1" * mask + "0" * (32 - mask)
# m1, m2, m3, m4 = [
#     int(bin_mask[0:8], 2),
#     int(bin_mask[8:16], 2),
#     int(bin_mask[16:24], 2),
#     int(bin_mask[24:32], 2),
# ]
# print (bin_mask)
# print(m1, m2, m3, m4)
# 
# ip_output = """
# Network:
# {0:<8}  {1:<8}  {2:<8}  {3:<8}
# {0:08b}  {1:08b}  {2:08b}  {3:08b}"""
# 
# mask_output = """
# Mask:
# /{0}
# {1:<8}  {2:<8}  {3:<8}  {4:<8}
# {1:08b}  {2:08b}  {3:08b}  {4:08b}
# """
# 
# print(ip_output.format(oct1, oct2, oct3, oct4))
# print(mask_output.format(mask, m1, m2, m3, m4))

network = input("Введите адрес сети: ")

ip, mask = network.split("/")
ip_list = ip.split(".")
mask = int(mask)

oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(oct1, oct2, oct3, oct4))
print(mask_output.format(mask, m1, m2, m3, m4))