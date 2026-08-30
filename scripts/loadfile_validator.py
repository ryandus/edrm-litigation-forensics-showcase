"""
loadfile_validator.py
Production QC utility to verify Concordance (.dat) and Opticon (.opt) load file integrity.
Checks:
  1. Concordance delimiter consistency (þ quote, \x14 field separator).
  2. Header vs. row column count match.
  3. Image cross-reference continuity against .opt files.
"""

import sys
import os

QUOTE_CHAR = 'þ'
DELIM_CHAR = '\x14'

def validate_dat(dat_path):
    print(f"[*] Validating Concordance DAT: {dat_path}")
    if not os.path.exists(dat_path):
        print(f"[!] Error: File not found: {dat_path}")
        return None

    with open(dat_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = [l.strip() for l in f if l.strip()]

    if not lines:
        print("[!] Error: DAT file is empty.")
        return None

    header_raw = lines[0]
    headers = [col.strip(QUOTE_CHAR) for col in header_raw.split(DELIM_CHAR)]
    expected_cols = len(headers)
    print(f"[+] Headers detected ({expected_cols} columns): {', '.join(headers[:5])}...")

    error_count = 0
    bates_list = []

    for idx, row in enumerate(lines[1:], start=2):
        fields = [col.strip(QUOTE_CHAR) for col in row.split(DELIM_CHAR)]
        if len(fields) != expected_cols:
            print(f"[!] Row {idx} Column Mismatch: Expected {expected_cols}, got {len(fields)}")
            error_count += 1
        bates_list.append(fields[0])

    if error_count == 0:
        print(f"[+] DAT validation SUCCESS: {len(bates_list)} records verified with zero column anomalies.")
        return bates_list
    else:
        print(f"[!] DAT validation FAILED: {error_count} row errors found.")
        return None

def validate_opt(opt_path, expected_bates):
    print(f"\n[*] Validating Opticon OPT: {opt_path}")
    if not os.path.exists(opt_path):
        print(f"[!] Error: File not found: {opt_path}")
        return False

    with open(opt_path, 'r', encoding='utf-8', errors='replace') as f:
        opt_lines = [l.strip().split(',') for l in f if l.strip()]

    print(f"[+] Total page image records in OPT: {len(opt_lines)}")
    opt_doc_starts = [row[0] for row in opt_lines if len(row) > 3 and row[3] == 'Y']
    print(f"[+] Document boundary starts ('Y' flags): {len(opt_doc_starts)}")

    if expected_bates and set(expected_bates) == set(opt_doc_starts):
        print("[+] OPT validation SUCCESS: All document boundaries match DAT records perfectly.")
        return True
    elif expected_bates:
        diff = set(expected_bates).symmetric_difference(set(opt_doc_starts))
        print(f"[!] OPT Mismatch: {len(diff)} discrepancies between DAT and OPT document identifiers.")
        return False
    return True

if __name__ == "__main__":
    dat_file = sys.argv[1] if len(sys.argv) > 1 else "../samples/sample_production.dat"
    opt_file = sys.argv[2] if len(sys.argv) > 2 else "../samples/sample_opticon.opt"

    records = validate_dat(dat_file)
    if records:
        validate_opt(opt_file, records)