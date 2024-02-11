import ctypes
import winreg

def set_proxy(enable_proxy):
    key_path = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"

    try:
        # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)

        # Set the ProxyEnable value
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, int(enable_proxy))

        if enable_proxy:
            # Set the ProxyServer value
            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, "10.1.1.161:65527")
        else:
            # Clear the ProxyServer value if proxy is disabled
            winreg.DeleteValue(key, "ProxyServer")

        # Notify the system about the changes
        ctypes.windll.Wininet.InternetSetOptionW(0, 39, 0, 0)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the registry key
        winreg.CloseKey(key)

def main():
    wifi_network = input("Enter your Wi-Fi network name: ")  # Replace this with your method of obtaining the network name
    if wifi_network == "MSIL Wireless":
        print(f"Wi-Fi Network: {wifi_network}")
        set_proxy(True)
        print("Proxy enabled for MSIL Wireless network.")
    else:
        print(f"Wi-Fi Network: {wifi_network}")
        set_proxy(False)
        print("Proxy disabled for other networks.")

if __name__ == "__main__":
    main()
