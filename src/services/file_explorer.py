import subprocess

def open_with_default_app(path):
    subprocess.Popen(["gio", "open", path])
