import os
HOME_DIR = os.environ["HOME"]
APP_NAME = "ZeduloPayslips"
APP_HOME_DIR = f"{HOME_DIR}/.{APP_NAME.lower()}"
APP_CONFIG_FILEPATH = f"{APP_HOME_DIR}/config.json"
APP_SQLITE_DB_FILEPATH = f"{APP_HOME_DIR}/database.db"

# DEFAULT APP CONFIGUTRATION
APP_CONFIG = {
    "EMPLOYEE_SPREADSHEET_FILEPATH": f"{HOME_DIR}/Downloads/EMPLOYEES_PAYROLL_TEMPLATE.xlsx",
    "PAYSLIP_TEMPLATE_FILEPATH"    : f"{HOME_DIR}/Downloads/PAYSLIP_TEMPLATE.xlsx",
    "EMPLOYEE_PAYSLIPS_FOLDER"     : f"{HOME_DIR}/{APP_NAME.lower()}",

    # SOURCE XLSX HEADERS
    "EMPLOYEE_NAME_HEADER"          : "Name",
    "EMPLOYEE_STAFF_NUMBER_HEADER"  : "Staff Number",
    "EMPLOYEE_EMAIL_HEADER"         : "Email",   # not included in spreadsheet
    "EMPLOYEE_TIN_HEADER"           : "TIN",   # not included in spreadsheet
    "EMPLOYEE_POSITION_HEADER"      : "Position",
    "EMPLOYEE_DEPARTMENT_HEADER"    : "Department",   # not included in spreadsheet
    "EMPLOYEE_ACCOUNT_NUMBER_HEADER": "Account Number",
    "EMPLOYEE_GROSS_INCOME_HEADER"  : "Basic Salary",
    "EMPLOYEE_UNTAXED_BONUS_HEADER" : "Bonus",

    # TEMPLATE XLSX CELLS
    "TEMPLATE_PAYSLIP_DATE_CELL"       : "A9",
    "TEMPLATE_PAYSLIP_PERIOD_CELL"     : "D11",
    "TEMPLATE_PAYSLIP_NUMBER_CELL"     : "D12",
    "TEMPLATE_NAME_CELL"               : "D13",
    "TEMPLATE_STAFF_NUMBER_CELL"       : "D14",
    "TEMPLATE_EMAIL_CELL"              : "",
    "TEMPLATE_TIN_CELL"                : "D15",
    "TEMPLATE_POSITION_CELL"           : "D16",
    "TEMPLATE_DEPARTMENT_CELL"         : "D17",
    "TEMPLATE_ACCOUNT_NUMBER_CELL"     : "C20",
    "TEMPLATE_GROSS_INCOME_CELL"       : "C23",
    "TEMPLATE_UNTAXED_BONUS_CELL"      : "C33",
    "TEMPLATE_EMPLOYEE_SSF_CELL"       : "D25",
    "TEMPLATE_INCOME_TAX_CELL"         : "D27",
    "TEMPLATE_TIER_2_CELL"             : "E29",
    "TEMPLATE_EMPLOYER_SSF_CELL"       : "E31",
    "TEMPLATE_BONUS_TAX_CELL"          : "D35",
    "TEMPLATE_TOTAL_INCOME_CELL"       : "C37",
    "TEMPLATE_TOTAL_DEDUCTIONS_CELL"   : "D37",
    "TEMPLATE_TOTAL_CONTRIBUTIONS_CELL": "E37",
    "TEMPLATE_YTD_TIER_1_CELL"         : "C40",
    "TEMPLATE_YTD_TIER_2_CELL"         : "D40",
    "TEMPLATE_YTD_GROSS_PAY_CELL"      : "E40",
    "TEMPLATE_NET_INCOME_CELL"         : "C43"
}
