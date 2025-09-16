# exporter/app.py
from prometheus_client import start_http_server, Gauge
import psutil
import time
import platform
import argparse

# Metrics
g_cpu = Gauge('seaker_cpu_percent', 'CPU usage percent')
g_mem_used_gb = Gauge('seaker_mem_used_gb', 'Memory used in GB')
g_mem_total_gb = Gauge('seaker_mem_total_gb', 'Memory total in GB')
g_disk_used_gb = Gauge('seaker_disk_used_gb', 'Disk used in GB', ['mount'])
g_disk_total_gb = Gauge('seaker_disk_total_gb', 'Disk total in GB', ['mount'])
g_uptime_hours = Gauge('seaker_uptime_hours', 'Device uptime in hours')
g_temp = Gauge('seaker_temperature_celsius', 'Device temperature in Celsius')

def bytes_to_gb(b):
    return b / (1024**3)

def collect():
    # CPU percent (per core average)
    cpu = psutil.cpu_percent(interval=None)
    g_cpu.set(cpu)

    # Memory
    mem = psutil.virtual_memory()
    g_mem_used_gb.set(bytes_to_gb(mem.used))
    g_mem_total_gb.set(bytes_to_gb(mem.total))

    # Disk - iterate mountpoints (filter pseudo filesystems)
    for part in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(part.mountpoint)
            mount = part.mountpoint.replace('/', '_') if part.mountpoint != '/' else 'root'
            g_disk_used_gb.labels(mount).set(bytes_to_gb(usage.used))
            g_disk_total_gb.labels(mount).set(bytes_to_gb(usage.total))
        except PermissionError:
            # skip unreadable mounts
            continue

    # Uptime
    boot_ts = psutil.boot_time()
    uptime_hours = (time.time() - boot_ts) / 3600.0
    g_uptime_hours.set(uptime_hours)

    # Temperature (attempt; may not be present)
    try:
        temps = psutil.sensors_temperatures()
        # pick a sensible sensor if available
        if temps:
            # flatten and take first reading
            for k, entries in temps.items():
                if entries:
                    g_temp.set(entries[0].current)
                    break
    except AttributeError:
        # not supported on some platforms
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--interval', type=int, default=5, help='collection interval seconds')
    args = parser.parse_args()

    start_http_server(args.port)
    print(f"Exporter HTTP server started on :{args.port}")
    while True:
        collect()
        time.sleep(args.interval)
