import uuid, os, subprocess

print("Rovio Activation Script v1.0.1 by PRO100KatYT")
print("Linux/Wine adaptation\n")

def getMacAddressesInString():
    macAddresses = []

    # Linux method: parse 'ip link show' output
    try:
        output = subprocess.check_output(["ip", "link", "show"], universal_newlines=True)
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("link/ether"):
                parts = line.split()
                if len(parts) >= 2:
                    mac_linux = parts[1].upper().replace(":", "-")
                    if len(mac_linux) == 17 and mac_linux.count("-") == 5:
                        if mac_linux not in macAddresses:
                            macAddresses.append(mac_linux)
    except Exception:
        pass

    # Fallback: uuid.getnode()
    if not macAddresses:
        mac_int = uuid.getnode()
        macAddresses.append("-".join("{:012X}".format(mac_int)[i:i+2] for i in range(0, 12, 2)))

    return ";".join(macAddresses)

def getWineLocalLowPath():
    """
    Tries to find the Wine LocalLow path.
    Checks WINEPREFIX env var first, then falls back to ~/.wine
    """
    wine_prefix = os.environ.get("WINEPREFIX", os.path.join(os.path.expanduser("~"), ".wine"))
    username = os.environ.get("USER") or os.environ.get("USERNAME") or "steamuser"

    # Wine maps AppData/LocalLow under drive_c/users/<username>/AppData/LocalLow
    local_low = os.path.join(wine_prefix, "drive_c", "users", username, "AppData", "LocalLow")

    if not os.path.isdir(local_low):
        # Some Wine setups use a symlink or different username; scan drive_c/users/
        users_dir = os.path.join(wine_prefix, "drive_c", "users")
        if os.path.isdir(users_dir):
            for entry in os.listdir(users_dir):
                candidate = os.path.join(users_dir, entry, "AppData", "LocalLow")
                if os.path.isdir(candidate):
                    local_low = candidate
                    break

    return local_low

def main():
    macAddress = getMacAddressesInString()
    print("Detected MAC address(es): " + macAddress)

    xmlContent = '''<?xml version="1.0" encoding="utf-8"?>
<data>
<Boolean key="BDPGS12FL" value="True" />
<String key="BDPGS12FL_hardwareID" value="{macAddress}" />
</data>'''.format(macAddress=macAddress)

    localLowPath = getWineLocalLowPath()
    targetDir = os.path.join(localLowPath, "Rovio", "Bad Piggies")

    print("Target directory: " + targetDir)
    os.makedirs(targetDir, exist_ok=True)

    filePath = os.path.join(targetDir, "Settings.xml")
    with open(filePath, "w", encoding="utf-8") as f:
        f.write(xmlContent)

    print("\nSettings.xml successfully written to:")
    print(filePath)
    print("\nBad Piggies should now be activated! Launch the game to confirm.")

try:
    main()
except Exception as e:
    print("Unexpected error: {}".format(e))
