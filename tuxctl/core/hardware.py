import psutil
import cpuinfo
import platform

cpu_cores = psutil.cpu_count()
print("CPU cores: ", cpu_cores)

cpu_info = cpuinfo.get_cpu_info()

cpu_model = cpu_info["brand_raw"]
cpu_threads = cpu_info["count"]

print("CPU: " , cpu_model)
print("CPU threads: ", cpu_threads)

architect = platform.machine()
print("Architecture:", architect)


