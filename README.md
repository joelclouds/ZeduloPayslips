# ZeduloPayslips

A desktop application for generating employee payslips from Excel templates. Built with Python, openpyxl, and Tkinter.

## 📋 Features

- Generate payslips for multiple employees from a master spreadsheet
- Customizable Excel templates for payslip formatting
- Automatic calculation of taxes, SSF contributions, and net pay
- Batch processing across multiple months
- Export payslips to PDF for distribution
- Email payslips via Thunderbird (no SMTP credentials required)
- Desktop integration with application menu launcher
- Linux-native installation with venv

## 🏗️ Project Structure

```
ZeduloPayslips/
├── assets/                     # Icons and images
│   └── zedulopayslips.png
├── scripts/                    # Installation scripts
│   ├── install.sh             # Install script
│   ├── uninstall.sh           # Uninstall script
│   └── update.sh              # Update script
├── src/                        # Source code
│   ├── config.py              # Default Application configuration
│   ├── config_manager.py      # Config file management
│   ├── setup.py               # Python setup logic
│   ├── services/              # Business logic
│   │   ├── payslip_generator.py
│   │   ├── file_explorer.py
│   │   └── mailing.py
│   └── ui/                    # User interface
│       ├── app.py
│       └── settings_window.py
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── LICENSE 
```

## 🔧 Prerequisites

- **Python 3.10+**
- **python3-venv**
- **LibreOffice** (for XLSX → PDF conversion)
- **Thunderbird** (for payslip emailing)
- **Linux desktop environment** (GNOME, KDE, XFCE, etc.)

## 🚀 Installation

### Quick Install (For fresh setups)

```bash
git clone https://github.com/joelclouds/ZeduloPayslips.git
cd ZeduloPayslips
./scripts/install.sh
```

### Quick Update (For existing installations)

To update the app to the latest version **without losing your data or settings**:

```bash
cd /path/to/your/ZeduloPayslips   # ← Navigate to your existing clone
git pull
./scripts/update.sh
```

> ⚠️ **Note:** Your configuration and generated payslips are **not affected** by updates.

### What the Installer Does

1. **Checks system dependencies** (Python, LibreOffice)
2. **Creates application directory** at `~/.zedulopayslips/`
3. **Copies project files** to app directory
4. **Creates Python virtual environment**
5. **Installs dependencies** from `requirements.txt`
6. **Creates desktop entry** for application menu integration
7. **Updates desktop database** for immediate access

After installation, find **ZeduloPayslips** in your application menu!

## 📦 Dependencies

- **openpyxl** - Excel file manipulation
- **openpyxl-image-loader** - Image preservation in templates
- **Pillow** - Image processing
- **tkinter** - Desktop UI (included with Python)
- Additional dependencies in `requirements.txt`

## 🎯 Usage

1. Launch **ZeduloPayslips** from your application menu
2. Configure paths in **Settings**:
   - Employee spreadsheet filepath
   - Payslip template filepath
   - Output folder for generated payslips
3. Select month(s) to generate
4. Click **Generate Payslips**
5. XLSX files are generated, then converted to PDF automatically
6. Review PDFs, open folder, or email individual payslips
7. Use **Send All Emails** to batch-open Thunderbird compose windows

> 📖 **Detailed UI Guide**: See [docs/USAGE.md](docs/USAGE.md) for workflow diagrams, config field explanations, and troubleshooting.


## ⚙️ Configuration

Configuration stored in `~/.zedulopayslips/config.json`:

```json
{
    "EMPLOYEE_SPREADSHEET_FILEPATH": "~/Downloads/EMPLOYEES_PAYROLL_TEMPLATE.xlsx",
    "PAYSLIP_TEMPLATE_FILEPATH": "~/Downloads/PAYSLIP_TEMPLATE.xlsx",
    "EMPLOYEE_PAYSLIPS_FOLDER": "~/zedulopayslips",
    "EMPLOYEE_NAME_HEADER": "Employee Name",
    "EMPLOYEE_EMAIL_HEADER": "Email",
    "BASIC_SALARY_CELL": "B5",
    "TAX_CELL": "B10",
    "SSF_CELL": "B11",
    "NET_PAY_CELL": "B12"
}
```

## 🗑️ Uninstallation

```bash
cd ZeduloPayslips
./scripts/uninstall.sh
```

This removes:
- Application directory (`~/.zedulopayslips/`)
- Desktop entry
- Virtual environment

## 🛠️ Development

### Setting up development environment

```bash
# Clone repository
git clone https://github.com/joelclouds/ZeduloPayslips.git
cd ZeduloPayslips

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python3 main.py
```

## 📝 License

MIT License

## 🙏 Acknowledgments

Idea Brainstorming & Tax calculation QA by:
- [Cyril Dzamaklu](https://www.linkedin.com/in/cyril-elorm-dzamaklu)
- [Patience Tsikudo](https://www.linkedin.com/in/patience-tsikudo-7551549b)

Uses **openpyxl** for spreadsheet processing.
Uses **LibreOffice** for XLSX → PDF conversion.
Uses **Thunderbird** for mailing without managing sensitive email credentials.
Inspired by payroll management needs.

## 🐛 Troubleshooting

### Desktop entry not appearing
```bash
update-desktop-database ~/.local/share/applications/
```

### Thunderbird not found (mailing fails)
```bash
sudo apt install thunderbird  # Debian/Ubuntu
```

### LibreOffice not found (PDF generation fails)
```bash
sudo apt install libreoffice  # Debian/Ubuntu
```

### Permission denied on install
```bash
chmod +x scripts/install.sh
./scripts/install.sh
```

## 📞 Support & Contact

For issues, questions, or feature requests:
- 📧 Email: [Joel Opoku](mailto:joelclouds@gmail.com) or [jopoku@zedulo.com](mailto:jopoku@zedulo.com)
- 🐛 GitHub Issues: [Open an issue](https://github.com/joelclouds/ZeduloPayslips/issues)

Feedback and contributions are welcome.
