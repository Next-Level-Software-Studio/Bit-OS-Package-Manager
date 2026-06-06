from pathlib import Path
import subprocess, portage, os

vartree = portage.db[portage.root]["vartree"]
package_match = vartree.dbapi.match("sys-apps/bpm")[-1]
use_flags = vartree.dbapi.aux_get(package_match, ["USE"])[0]
FLAGS =use_flags.split()

def main(package_name: str):
    portagedatabase = "/var/db/repos"
    if os.path.exists(portagedatabase):
        available_portage_packages = []
        ignore = {"profiles", "metadata", "licenses", "scripts", "eclass"}
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
                                                    available_portage_packages.append(f"{cat.name}/{pkg.name}")
                                    except PermissionError:
                                        continue
                    except PermissionError:
                        continue
        if package_name in available_portage_packages:
            command = subprocess.run(["emerge", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if command.returncode == 0:
                print(f"Installing {package_name}, was sucessfull.")
            else:
                print(f"Something has gone wrong.")
    elif not portagedatabase.exists():
        pass