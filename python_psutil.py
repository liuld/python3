#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

# psutil: psutil是一个跨平台库(http://pythonhosted.org/psutil/)能够轻松实现获取系统运行的进程和系统利用率
#         (包括CPU、内存、磁盘、网络等)信息。它主要用来做系统监控，性能分析，进程管理。它实现了同等命令
#         行工具提供的功能，如ps/top/lsof/netstat/ifconfig/who/df/kill/free/nice/ionice/iostat/iotop/uptime
#         /pidof/tty/taskset/pmap等


import psutil

# 逻辑cpu个数
cpu_total = int(psutil.cpu_count(logical=True))
# 各个cpu的使用率
cpu_percent_list = psutil.cpu_percent(percpu=True,interval=True)
# 各个cpu使用详细
cpu_percent_detail = psutil.cpu_times(percpu=True)

print("\033[1;35m系统cpu使用情况: 物理cpu个数: %s 逻辑cpu个数: %d\033[0m" % (psutil.cpu_count(), cpu_total))
for i in range(len(cpu_percent_list)):
    print("\033[1;32mcpu%d 使用率: %s%% \033[0m \ndetail: %s" % (i, cpu_percent_list[i], cpu_percent_detail[i]))

# memory
memory_info = psutil.virtual_memory()
# total 单位:G
mem_total = round(memory_info.total / (1024.0 * 1024.0 * 1024.0), 2)
# freeMen = free + cached + buffers
mem_free = round((memory_info.free + memory_info.cached + memory_info.buffers) / (1024.0 * 1024.0 * 1024.0), 2)
# swap
swap_info = psutil.swap_memory()
#swap_total
swap_total = round(swap_info.total / (1024.0 * 1024.0 * 1024.0), 2)
swap_free = round(swap_info.free / (1024.0 * 1024.0 * 1024.0), 2)

print("\033[1;35m系统内存使用情况 总数total: %0.2fG 空闲free: %0.2fG 使用率: %0.2f%%\033[0m" % (mem_total, mem_free, memory_info.percent))
print("\033[1;35m系统swap使用情况 总数total: %0.2fG 空闲free: %0.2fG 使用率: %0.2f%%\033[0m" % (swap_total, swap_free, swap_info.percent))

# disk
partitions = psutil.disk_partitions()

print("\033[1;35m系统分区使用情况\033[0m")
for i in range(len(partitions)):
    disk_device = partitions[i][0]
    disk_mountpoint = partitions[i][1]
    disk_total_size = round(psutil.disk_usage(disk_mountpoint)[0] / (1024.0 * 1024.0 * 1024.0), 2)
    disk_free_size = round(psutil.disk_usage(disk_mountpoint)[2] / (1024.0 * 1024.0 * 1024.0), 2)
    disk_percent = psutil.disk_usage(disk_mountpoint)[3]
    print("\033[1;32m分区: %s 挂载点: %s 总量: %0.2fG 可用: %0.2fG 使用率: %0.2f%%\033[0m" % (disk_device, disk_mountpoint, disk_total_size, disk_free_size, disk_percent))

disk_io_info = psutil.disk_io_counters(perdisk=True)
print("\033[1;35mio使用情况\033[0m")
print("\033[1;35mdevice\tread_count\twrite_count\tread_bytes\twrite_bytes\tread_time\twrite_time\033[0m")
for device in disk_io_info.keys():
    print("%s\t%-10.0d\t%-10.0d\t%-10.0f KB\t%-10.0f KB\t%-10d\t%-10d" % (device, disk_io_info[device][0], disk_io_info[device][1], disk_io_info[device][2]/1024, disk_io_info[device][3]/1024, disk_io_info[device][4], disk_io_info[device][5]))

# net
net_info = psutil.net_io_counters(pernic=True)
print("\033[1;35m网卡流量情况\033[0m")
print("\033[1;35m%-15s\t%-15s\t%-15s\t%-15s\t%-15s\033[0m" % ("device_name", "bytes_sent(M)", "bytes_recv(M)", "packets_sent", "packets_recv"))
for nic in net_info.keys():
    print("%-15s\t%-15.2f\t%-15.2f\t%-15d\t%-15d" % (nic, net_info[nic][0]/1024.0/1024.0, net_info[nic][1]/1024.0/1024.0, net_info[nic][2], net_info[nic][3]))
