from pathlib import Path
import subprocess, portage

vartree = portage.db[portage.root]["vartree"]
package_match = vartree.dbapi.match("app-misc/fastfetch")[-1]
use_flags = vartree.dbapi.aux_get(package_match, ["USE"])[0]
FLAGS =use_flags.split()

def main(package: str):
    gentoodatabase = Path("/var/db/repos/gentoo")
    package_categories = []
    if gentoodatabase.exists():
        for folder in gentoodatabase.iterdir():
            if folder.is_dir():
                package_categories.append(folder.name)
        for_removal = ["profiles", "metadata", "licenses", "scripts"]
        for i in for_removal:
            if i in package_categories:
                package_categories.remove(i)
    elif not gentoodatabase.exists():
        pass