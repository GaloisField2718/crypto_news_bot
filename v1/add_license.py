import os

LICENSE_HEADER = '''"""
IRC News Bot - A bot that monitors crypto-related news from IRC channels and forwards them to Telegram
Copyright (C) 2024  GaloisField

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

'''

def add_license_to_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Skip if license is already present
    if 'Copyright (C) 2024  GaloisField' in content:
        print(f"License already present in {file_path}")
        return
    
    with open(file_path, 'w') as file:
        file.write(LICENSE_HEADER + content)
    print(f"Added license to {file_path}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_license_to_file(file_path)

if __name__ == "__main__":
    # Add license to all Python files in src directory
    process_directory('src')
    # Add license to main.py if it exists
    if os.path.exists('main.py'):
        add_license_to_file('main.py')
    print("License addition complete!") 