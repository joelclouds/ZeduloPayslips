import sqlite3
from pathlib import Path
from src.config import APP_SQLITE_DB_FILEPATH

TABLES = {"payslip_records": "payslip_records"}

def open_db():
    db_path = Path(APP_SQLITE_DB_FILEPATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

with open_db() as db_conn:
    db = db_conn.cursor()
    db.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLES['payslip_records']} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            staff_number INTEGER NOT NULL,
            name TEXT NOT NULL,
            month_no INTEGER NOT NULL,
            tier_1 INTEGER DEFAULT 0,
            tier_2 INTEGER DEFAULT 0,
            gross_pay INTEGER DEFAULT 0,
            UNIQUE(staff_number, month_no)
        )
    """)
    db_conn.commit()


class YTD_Tracker:
    def __init__(self):
        self.table = TABLES["payslip_records"]

    def get_ytd(self, month_no: int, employee: dict) -> dict:
        with open_db() as db_conn:
            db = db_conn.cursor()
            db.execute(f"""
                SELECT staff_number, name, tier_1, tier_2, gross_pay
                FROM {self.table}
                WHERE staff_number = ? AND month_no = ?
            """, (int(employee["staff_number"]), month_no))
            row = db.fetchone()
            if row:
                return {
                    "staff_number": row["staff_number"],
                    "name": row["name"],
                    "ytd_tier_1": row["tier_1"] or 0,
                    "ytd_tier_2": row["tier_2"] or 0,
                    "ytd_gross_pay": row["gross_pay"] or 0,
                }
            return {
                "staff_number": int(employee["staff_number"]),
                "name": employee["name"],
                "ytd_tier_1": 0,
                "ytd_tier_2": 0,
                "ytd_gross_pay": 0,
            }

    def set_month_record(self, month_no: int, employee: dict) -> None:
        """
        """
        necessary_keys = [
            'staff_number',
            'name',
            'employee_ssf',
            'tier_2',
            'gross_income'
        ]
        assert all([key in employee.keys() for key in necessary_keys]), f"employee dict must contain these keys: {necessary_keys}"

        with open_db() as db_conn:
            db = db_conn.cursor()
            db.execute(f"""
                INSERT OR REPLACE INTO {self.table}
                (staff_number, name, month_no, tier_1, tier_2, gross_pay)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                int(employee['staff_number']),
                employee['name'],
                month_no,
                employee['employee_ssf'],
                employee['tier_2'],
                employee['gross_income']
            ))
            db_conn.commit()

    def get_cumulative_ytd(self, up_to_month: int, employee: dict) -> dict:
        with open_db() as db_conn:
            db = db_conn.cursor()
            db.execute(f"""
                SELECT
                    SUM(tier_1) as tier_1,
                    SUM(tier_2) as tier_2,
                    SUM(gross_pay) as gross_pay
                FROM {self.table}
                WHERE staff_number = ? AND month_no <= ?
            """, (int(employee["staff_number"]), up_to_month))
            row = db.fetchone()
            return {
                "staff_number": int(employee["staff_number"]),
                "ytd_tier_1": row["tier_1"] or 0,
                "ytd_tier_2": row["tier_2"] or 0,
                "ytd_gross_pay": row["gross_pay"] or 0,
            }
