#!./venv/bin/python3

"""
Entry point for Zedulo Payslips Utility.

This file does not contain any business logic.
All UI and generation logic is encapsulated in src/ui/app.py.
"""

from tkinter import Tk
from src.ui.app import App

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
