import distro
import platform

os_name = distro.name()
os_id = distro.id()

print("OS name:", os_name)
print("OS ID:", os_id)

kernal = platform.release()
print("Kernal: ", kernal)

