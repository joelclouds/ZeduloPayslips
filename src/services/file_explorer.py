# src/services/file_explorer.py
import os
import subprocess

def open_with_default_app(path):
#    os.system(f"ogdir=$(pwd) && cd {os.environ['HOME']} && gio open {path} && cd $ogdir")
    subprocess.run(["gio", "open", path])
