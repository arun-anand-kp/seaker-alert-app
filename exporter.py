# from prometheus_client import start_http_server, Gauge
# import psutil
# import time

# # Define Prometheus metrics
# cpu_usage = Gauge("cpu_usage_percent", "CPU usage in percent")
# ram_used = Gauge("ram_used_gb", "Used RAM in GB")
# ram_total = Gauge("ram_total_gb", "Total RAM in GB")
# disk_used = Gauge("disk_used_gb", "Used disk space in GB")
# disk_total = Gauge("disk_total_gb", "Total disk space in GB")
# uptime = Gauge("uptime_hours", "Device uptime in hours")

# def collect_metrics():
#     cpu_usage.set(psutil.cpu_percent(interval=1))
#     memory = psutil.virtual_memory()
#     ram_used.set(round(memory.used / (1024**3), 2))
#     ram_total.set(round(memory.total / (1024**3), 2))
#     disk = psutil.disk_usage('C:/')  # Use C drive on Windows
#     disk_used.set(round(disk.used / (1024**3), 2))
#     disk_total.set(round(disk.total / (1024**3), 2))
#     boot_time = psutil.boot_time()
#     uptime.set(round((time.time() - boot_time) / 3600, 2))

# if __name__ == "__main__":
#     start_http_server(8000)
#     while True:
#         collect_metrics()
#         time.sleep(5)


