import winreg
import os
import time
def delete_registry_key():
    try:
        reg_path = r"SOFTWARE\WOW6432Node\Microsoft\EdgeUpdate\Clients\{F3017226-FE2A-4295-8BDF-00C3A9A7E4C5}"
        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
            winreg.DeleteKey(hkey, reg_path)
        print("Webview reinstalling, please wait...")
        os.system("curl -o webview.exe https://raw.githubusercontent.com/evilionx3/webview-installer/refs/heads/main/MicrosoftEdgeWebview2Setup.exe")
        time.sleep(1)
        os.system("webview.exe")
    except FileNotFoundError:
        print("Registry key not found, reinstalling webview now...")
        os.system("curl -o webview.exe https://raw.githubusercontent.com/evilionx3/webview-installer/refs/heads/main/MicrosoftEdgeWebview2Setup.exe && webview.exe")
    except PermissionError:
        print("Permission denied. Running as admin...")
        if os.name == 'nt':
            os.system('powershell -Command "Start-Process cmd -ArgumentList \'/c {}\' -Verb runAs"'.format(__file__))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_registry_key()