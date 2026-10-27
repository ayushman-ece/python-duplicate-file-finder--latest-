# 🔍 Python Duplicate File Finder

A simple Python command-line tool that scans folders and identifies duplicate files by comparing their SHA-256 hashes.

## ✨ Features

- 📂 Scan folders and subfolders
- 🔐 Calculate SHA-256 hashes
- 🔎 Identify files with identical contents
- 📋 Display duplicate groups and file paths
- ⚠️ Handle invalid paths and file-reading errors
- 🛡️ Read-only scanning — files are never deleted
- 🧩 Separate application logic from the user interface

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** `hashlib`, `pathlib`
- **Interface:** Command-line interface (CLI)

## 📁 Project Structure

```text
python-duplicate-file-finder/
├── main.py
├── duplicate_finder.py
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-duplicate-file-finder.git
```

### 2. Open the project folder

```bash
cd python-duplicate-file-finder
```

### 3. Run the application

```bash
python main.py
```

### 4. Enter a folder path

Provide the path to the folder you want to scan.

## 💻 Example Output

```text
===== DUPLICATE FILE FINDER =====
Enter folder path to scan: C:\Users\YourName\Documents

Found 1 duplicate group(s).

Group 1:
  C:\Documents\copy.txt
  C:\Documents\backup\copy.txt
```

*Example output only; results depend on the files in your folder.*

## 🧠 Concepts Learned

- Functions and modular programming
- File and directory traversal
- Binary file reading
- SHA-256 hashing
- Dictionaries and lists
- Exception handling
- Working with file paths
- Algorithmic grouping

## ⚙️ How It Works

1. Scans files recursively in the selected folder.
2. Reads each file in chunks.
3. Calculates its SHA-256 hash.
4. Groups files with matching hashes.
5. Displays groups containing more than one file.

## ⚠️ Limitations

- Large folders can take time to scan.
- Files that cannot be read are skipped with a warning.
- Matching hashes are treated as duplicates; cryptographic hash collisions are theoretically possible.

## 🔮 Future Improvements

- Export duplicate reports to CSV
- Add a progress indicator
- Compare file sizes before hashing
- Add optional duplicate cleanup with confirmation
- Generate a scan summary report

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece

Python learning and portfolio project.

---

*Learning Python one practical project at a time. 🚀*
