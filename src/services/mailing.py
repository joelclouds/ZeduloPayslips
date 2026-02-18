# src/services/mailing.py
"""Email service for payslips via Thunderbird CLI only. No SMTP, no credentials."""

import subprocess
from pathlib import Path


class EmailSender:
    def __init__(self):
        self.thunderbird_cmd = self._find_thunderbird()

    def _find_thunderbird(self):
        for cmd in ["thunderbird", "icedove"]:
            try:
                subprocess.run([cmd, "--version"], check=True, capture_output=True, timeout=5)
                return cmd
            except:
                continue
        return None

    def _escape(self, value):
        return value.replace('"', '\\"').replace(',', '\\,').replace('\n', '\\n')

    def send_payslip(self, recipient_email, employee_name, month, pdf_path):
        if not recipient_email or not Path(pdf_path).exists():
            return False, "Invalid email or PDF not found"
        if not self.thunderbird_cmd:
            return False, "Thunderbird not found"

        subject = f"Payslip for {month} - {employee_name}"
        body = f"""Dear {employee_name},\n\nPlease find attached your payslip for {month}.\n\nBest regards,\nHR Team"""

        try:
            args = f'to={recipient_email},subject={self._escape(subject)},body={self._escape(body)},attachment={pdf_path}'
            subprocess.run([self.thunderbird_cmd, "-compose", args], check=True, capture_output=True, timeout=None)
            return True, f"Compose opened for {recipient_email}"
        except Exception as e:
            return False, str(e)

    def send_bulk(self, payslip_list):
        """
        Send multiple payslips via Thunderbird.
        Opens one compose window per email (user reviews & sends each).
        payslip_list: [{"email": "...", "name": "...", "month": "...", "pdf": "..."}, ...]
        Returns: {"success": int, "failed": int, "errors": [...]}
        """
        results = {"success": 0, "failed": 0, "errors": []}
        for p in payslip_list:
            ok, msg = self.send_payslip(p["email"], p["name"], p["month"], p["pdf"])
            if ok:
                results["success"] += 1
            else:
                results["failed"] += 1
                results["errors"].append({"email": p["email"], "error": msg})
        return results


def send_payslip_email(recipient_email, employee_name, month, pdf_path):
    return EmailSender().send_payslip(recipient_email, employee_name, month, pdf_path)


def send_bulk_payslips(payslip_list):
    return EmailSender().send_bulk(payslip_list)
