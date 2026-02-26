import os, json, subprocess, shutil, venv
from pathlib import Path
from config import APP_HOME_DIR, APP_CONFIG_FILEPATH, APP_CONFIG, APP_NAME
import sys

def setup(fresh):
    Path(APP_HOME_DIR).mkdir(exist_ok=True)

    # Copy project
    app_dest = Path(APP_HOME_DIR) / "runtime_files"
    if app_dest.exists():
        shutil.rmtree(app_dest)
    shutil.copytree(
        Path(__file__).parent.parent,
        app_dest,
        ignore=shutil.ignore_patterns('__pycache__', '*.pyc', 'bin', 'build', 'dist', '.git', 'venv')
    )

    # Create venv with pip
    venv_path = app_dest / "venv"
    venv.create(str(venv_path), with_pip=True)

    # Install dependencies
    requirements = app_dest / "requirements.txt"
    if requirements.exists():
        subprocess.run([str(venv_path / "bin" / "pip"), "install", "-r", str(requirements)], check=True)

    # Create config
    Path(APP_CONFIG_FILEPATH).parent.mkdir(exist_ok=True)
    old_cfg = {}

    if not fresh:
        with open(APP_CONFIG_FILEPATH, "r") as f:
            old_cfg = json.load(f)

    with open(APP_CONFIG_FILEPATH, "w") as f:
        cfg = APP_CONFIG.copy()

        if not fresh:
            cfg.update(old_cfg)

        json.dump(cfg, f, indent=4)

    # Desktop entry
    desktop = Path.home() / ".local" / "share" / "applications" / f"{APP_NAME.lower()}.desktop"
    desktop.parent.mkdir(parents=True, exist_ok=True)
    desktop.write_text(f"""[Desktop Entry]
Type=Application
Name={APP_NAME}
Exec={venv_path / "bin" / "python"} {app_dest / "main.py"}
Icon={APP_HOME_DIR}/icon.png
Categories=Office
Terminal=False;
""")
    desktop.chmod(0o755)

    # Copy icon
    icon_src = Path(__file__).parent.parent / "assets" / "zedulopayslips.png"
    if icon_src.exists():
        shutil.copy2(icon_src, Path(APP_HOME_DIR) / "icon.png")

    subprocess.run(["update-desktop-database", str(Path.home() / ".local" / "share" / "applications")], capture_output=True)
    print(f"\n✅ {APP_NAME} installed!")

if __name__ == "__main__":
    isfresh = ("--fresh" in sys.argv)

    setup(isfresh)
