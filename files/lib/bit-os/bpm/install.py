import subprocess, os, portage, socket
dbapi = portage.db[portage.root]["vartree"].dbapi
try:
    package_match = dbapi.match("sys-apps/bpm")[-1]
    use_flags = dbapi.aux_get(package_match, ["USE"])[0]
    FLAGS = use_flags.split()
except IndexError:
    FLAGS = []

def main(package_name: str):
    def internet(timeout=2):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except OSError:
            return False
    def bpm(name):
        pass
    def portage(name):
        portagedatabase = "/var/db/repos"
        available_portage_packages = set()
        ignore = {"profiles", "metadata", "licenses", "scripts", "eclass"}
        if os.path.exists(portagedatabase):
            try:
                with os.scandir(portagedatabase) as overlays:
                    for overlay in overlays:
                        if overlay.is_dir():
                            try:
                                with os.scandir(overlay.path) as categories:
                                    for cat in categories:
                                        if cat.is_dir() and cat.name not in ignore:
                                            try:
                                                with os.scandir(cat.path) as pkgs:
                                                    for pkg in pkgs:
                                                        if pkg.is_dir():
                                                            available_portage_packages.add(f"{cat.name}/{pkg.name}")
                                                return available_portage_packages
                                            except PermissionError:
                                                return False
                            except PermissionError:
                                return False
            except PermissionError:
                return False

        if package_name in available_portage_packages:
            existsinportage = True
        elif package_name not in available_portage_packages:
            existsinportage = False

        if 
        
        if existsinportage is True and bpm(package_name):
            print("A package is duplicated.")
        elif existsinportage is True and not bpm(package_name):
            command = subprocess.run(["emerge", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if command.returncode == 0:
                print(f"Installing {package_name}, was sucessfull.")
            else:
                print("Something has gone wrong.")
        elif existsinportage is False and bpm(package_name):
            pass
        elif existsinportage is False and not bpm(package_name):
            print("O pacote não está disponível.")
    elif not os.path.exists(portagedatabase):
        print("Please, create a folder at /var/db/repos")