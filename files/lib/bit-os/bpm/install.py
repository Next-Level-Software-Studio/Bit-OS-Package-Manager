from pathlib import Path
import subprocess
def main(package: str):
    gentoodatabase = Path("/var/db/repos/gentoo")
    if not gentoodatabase.exists():
        try:
            subprocess.run(["emerge", "--sync"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error syncing Gentoo database: {e}")