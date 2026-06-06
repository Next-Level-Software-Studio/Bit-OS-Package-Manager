from pathlib import Path
import subprocess, portage

vartree = portage.db[portage.root]["vartree"]
package_match = vartree.dbapi.match("app-misc/fastfetch")[-1]
use_flags = vartree.dbapi.aux_get(package_match, ["USE"])[0]
FLAGS =use_flags.split()

def main(package_name: str):
    gentoodatabase = Path("/var/db/repos/gentoo")
    if gentoodatabase.exists():
        ignore = ["profiles", "metadata", "licenses", "scripts"]
        categories = [p for p in gentoodatabase.iterdir() if p.is_dir() and p.name not in ignore]
        available_portage_packages = []
        for cat in categories:
            for pkg in cat.iterdir():
                if pkg.is_dir():
                    available_portage_packages.append(f"{pkg.parent.name}/{pkg.name}")
    elif not gentoodatabase.exists():
        pass