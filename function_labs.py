devices = [
    {
        "device_id": "R1",
        "ip": "192.168.1.1",
        "location": "DataCenter",
        "os_version": "IOS 15.1",
        "allowed_versions": ["IOS 15.2", "IOS 15.3"],
        "last_patch_days": 120,
        "open_ports": [22, 80, 443],
        "expected_ports": [22, 443],
        "login_attempts": 3
    },
    {
        "device_id": "FW1",
        "ip": "192.168.1.254",
        "location": "Branch",
        "os_version": "PAN-OS 9.0",
        "allowed_versions": ["PAN-OS 9.1"],
        "last_patch_days": 10,
        "open_ports": [22, 8080],
        "expected_ports": [22],
        "login_attempts": 15
    },
    {
        "device_id": "SW1",
        "ip": "192.168.2.10",
        "location": "HQ",
        "os_version": "NX-OS 7.0",
        "allowed_versions": ["NX-OS 7.0"],
        "last_patch_days": 200,
        "open_ports": [22, 23],
        "expected_ports": [22],
        "login_attempts": 1
    }
]
'''the function is descriptive'''
def os_version_check(data: list[dict])->list[str]:
    outdated_os = []
     
    for dev in data:
        os_version = dev.get("os_version")
        allowed_versions = dev.get("allowed_versions")
        if os_version not in allowed_versions:
            dev["flag"]="outdated_os"
            outdated_os.append(dev.get("device_id"))
    return outdated_os

print(os_version_check(devices))       

def patch_check(data:list[dict],duration:int)->list[str]:
    overdue_devices= []
    for dev in data:
        last_patch_days = dev.get("last_patch_days")
        if last_patch_days > duration:
            dev["flag"]= "patch_overdue"
            overdue_devices.append(dev.get("device_id"))
    return overdue_devices
print(patch_check(data=devices, duration = 80))

def status_category(data:list[dict])->str:
    high_risk_device = []
    for dev in data:
        device_id = dev.get("device_id")
        print(set(os_version_check(data=devices)).isdisjoint(patch_check(data=devices,duration=80)))
        if device_id in os_version_check(data=devices) and device_id in patch_check(data=devices, duration=80):
            dev["status"]="High_risk"
            high_risk_device.append(device_id)
    return high_risk_device
print(status_category(data=devices))  