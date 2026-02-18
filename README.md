# ZeduloPayslips

A desktop application for generating employee payslips from Excel templates. Built with Python and integrated with LibreOffice for spreadsheet processing.

## 📋 Features

- Generate individual payslips for multiple employees from a master spreadsheet
- Customizable Excel templates for payslip formatting
- Automatic calculation of taxes, SSF contributions, and net pay
- Employee data management
- Batch processing of payslips
- Desktop integration with application menu launcher

## 🏗️ Project Structure

```
ZeduloPayslips/
├── assets/                 # Icons and desktop entry files
│   ├── zedulopayslips.png
│   └── zedulo-payslips.desktop
├── bin/                    # Compiled executables (created during install)
├── scripts/                # Installation scripts
│   ├── install.sh
│   └── uninstall.sh
├── src/                    # Source code
│   ├── config.py          # Application configuration
│   ├── config_manager.py  # Config file management
│   ├── setup.py           # Installation setup script
│   ├── services/          # Business logic
│   └── ui/                # User interface
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Prerequisites

- **Python 3.8+**
- **LibreOffice** (for Excel file processing)
- **Linux desktop environment** (GNOME, KDE, XFCE, etc.)

## 🚀 Installation

### Quick Install

```bash
git clone https://github.com/joelclouds/ZeduloPayslips.git
cd ZeduloPayslips
./scripts/install.sh
```

### What the Installer Does

1. **Checks internet connectivity**
2. **Installs LibreOffice** (if not present)
3. **Creates Python virtual environment**
4. **Installs dependencies** from `requirements.txt`
5. **Compiles application** into standalone executable using PyInstaller
6. **Creates application directory** at `~/.zedulopayslips/`
7. **Installs desktop entry** for application menu integration
8. **Updates desktop database** for immediate access

After installation, you can find **ZeduloPayslips** in your application menu!

## 📦 Dependencies

- **PyInstaller** - Creates standalone executable
- **openpyxl** - Excel file manipulation
- **CustomTkinter** - Modern GUI framework
- Additional dependencies listed in `requirements.txt`

## 🎯 Usage

1. Launch ZeduloPayslips from your application menu
2. Configure your employee spreadsheet and payslip template paths
3. Load employee data from Excel
4. Generate individual payslips
5. Output PDFs are saved to your specified directory

## ⚙️ Configuration

The application stores configuration in `~/.zedulopayslips/config.json`:

```json
{
    "EMPLOYEE_SPREADSHEET_FILEPATH": "~/Downloads/EMPLOYEES_PAYROLL_TEMPLATE.xlsx",
    "PAYSLIP_TEMPLATE_FILEPATH": "~/Downloads/PAYSLIP_TEMPLATE.xlsx",
    "EMPLOYEE_PAYSLIPS_FOLDER": "~/zedulopayslips",
    // ... additional configuration options
}
```

## 🗑️ Uninstallation

```bash
cd ZeduloPayslips
./scripts/uninstall.sh
```

This removes:
- The application directory (`~/.zedulopayslips/`)
- Desktop entry
- Project files (optional)

## 🛠️ Development

### Setting up development environment

```bash
# Clone repository
git clone https://github.com/yourusername/ZeduloPayslips.git
cd ZeduloPayslips

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python main.py
```

### Building manually

```bash
# Activate virtual environment
source venv/bin/activate

# Build with PyInstaller
pyinstaller --onefile \
    --name zedulopayslips \
    --windowed \
    --icon=assets/zedulopayslips.png \
    main.py
```

## 📝 License

[Your License Here]

## 👥 Authors

[Your Name/Organization]

## 🙏 Acknowledgments

- Built with Python and CustomTkinter
- Uses LibreOffice for spreadsheet processing
- Inspired by payroll management needs

## 🐛 Troubleshooting

### "PyInstaller not found" error
```bash
pip install pyinstaller
```

### Desktop entry not appearing
```bash
update-desktop-database ~/.local/share/applications/
```

### LibreOffice missing
```bash
sudo apt install libreoffice  # Debian/Ubuntu
```

## 📞 Support & Contact

For issues, questions, or feature requests:
- 📧 Email: [Joel Opoku](mailto:joelclouds@gmail.com) or [jopoku@zedulo.com](mailto:jopoku@zedulo.com)
- 🐛 GitHub Issues: [Open an issue](https://github.com/joelclouds/ZeduloPayslips/issues)

We welcome your feedback and contributions!
