import subprocess, os, portage
dbapi = portage.db[portage.root]["vartree"].dbapi
try:
    package_match = dbapi.match("sys-apps/bpm")[-1]
    use_flags = dbapi.aux_get(package_match, ["USE"])[0]
    FLAGS = use_flags.split()
except IndexError:
    FLAGS = []

def main(package_name: str):
    def pip(name):
        pass
    def bpm(name)
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
                                        except PermissionError:
                                            print("Please report, this is bug.")
                        except PermissionError:
                            print("Please report, this is bug.")
        except PermissionError:
            print("Please report, this is bug.")
        if (package_name in available_portage_packages) and pip(package_name) and bpm(package_name):
            print("")
        elif package_name in available_portage_packages:
            command = subprocess.run(
                ["emerge", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if command.returncode == 0:
                print(f"Installing {package_name}, was sucessfull.")
            else:
                print("Something has gone wrong.")
        elif pip(package_name):

    elif not os.path.exists(portagedatabase):
        print("Please, create a folder at /var/db/repos")