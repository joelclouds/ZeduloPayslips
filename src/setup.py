import os, json, subprocess, shutil
from pathlib import Path
from config import APP_HOME_DIR, APP_CONFIG_FILEPATH, APP_CONFIG, APP_NAME
import sys

def setup():
    # Create app dir and config
    Path(APP_HOME_DIR).mkdir(exist_ok=True)

    with open(APP_CONFIG_FILEPATH, "w") as f:
        json.dump(APP_CONFIG, f, indent=4)

    # Build executable
    project_root = Path(__file__).parent.parent
    subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--name", APP_NAME.lower(),
        "--distpath", str(project_root/"bin"), "--windowed",
        "--icon", str(project_root/"assets/zedulopayslips.png"),
        str(project_root/"main.py")
    ], check=True)

    # Copy binary to APP_HOME_DIR
    binary_src = project_root/"bin"/APP_NAME.lower()
    binary_dest = Path(APP_HOME_DIR)/APP_NAME.lower()
    shutil.copy2(binary_src, binary_dest)
    binary_dest.chmod(0o755)

    # Desktop entry
    desktop = Path.home()/".local/share/applications"/f"{APP_NAME.lower()}.desktop"
    desktop.parent.mkdir(parents=True, exist_ok=True)
    desktop.write_text(f"""[Desktop Entry]
Type=Application
Name={APP_NAME}
Exec={binary_dest}
Icon={APP_HOME_DIR}/icon.png
Categories=Office;
""")
    desktop.chmod(0o755)

    # Copy icon
    shutil.copy2(project_root/"assets/zedulopayslips.png", Path(APP_HOME_DIR)/"icon.png")

    # Update desktop database immediately
    subprocess.run(["update-desktop-database", str(Path.home()/".local/share/applications")],
                  capture_output=True)

    print(f"\n✅ {APP_NAME} successfully installed!")
    print(f"   📁 Location: {APP_HOME_DIR}")
    print(f"   🖥️  Binary: {binary_dest}")
    print(f"\n🎯 You can now find '{APP_NAME}' in your application menu!")

if __name__ == "__main__":
    setup()
