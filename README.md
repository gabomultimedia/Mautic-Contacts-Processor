# Mautic Contacts Processor

This Python script processes multiple CSV files, extracts relevant contact information, and consolidates it into a single CSV file for easy import into Mautic.

## Features
- Supports multiple encoding formats (`utf-8`, `utf-16`, `latin-1`).
- Detects name and email columns automatically.
- Removes duplicate email entries.
- Outputs a single consolidated CSV file.

## Usage
1. Update the `base_path` variable with the folder path containing your CSV files.
2. Add the names of the CSV files to the `file_names` list.
3. Run the script:
   ```bash
   python process_mautic_contacts.py

Requirements
Python 3.x
pandas library (pip install pandas)
