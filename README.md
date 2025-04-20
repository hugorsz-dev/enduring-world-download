# Bible Commentary Scraper

A Python utility for downloading and compiling Bible commentaries from Enduring Word (Spanish version).

![Bible Study](https://img.shields.io/badge/Bible-Study-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

This script systematically downloads Bible commentaries from the Spanish version of Enduring Word's website (`es.enduringword.com`), organizing them by book and chapter for easy access. It then compiles all downloaded content into a single comprehensive HTML file.

## Features

- **Complete Bible Coverage**: Downloads commentaries for all 66 books of the Bible
- **Smart Downloading**: Detects page numbering patterns and adapts accordingly
- **Resume Capability**: Can continue interrupted downloads
- **Integrity Verification**: Checks for missing chapters and books
- **Consolidated Output**: Combines all commentaries into a single searchable HTML document

## Requirements

- Python 3.x
- Required packages (install via pip):
  ```
  pip install requests beautifulsoup4
  ```

## Usage

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/bible-commentary-scraper.git
   cd bible-commentary-scraper
   ```

2. Run the script:
   ```
   python scraper.py
   ```

3. The script will:
   - Create a directory called `html` to store individual files
   - Download commentaries for each book and chapter
   - Show progress in the console
   - Compile everything into `output.html` when complete

If you've previously run the script and want to resume a download:
- Answer `Y` when prompted to continue the existing download
- Answer `N` to start fresh

## How It Works

1. **Initialization**: Sets up book names and chapter counts
2. **URL Pattern Detection**: Determines if the website uses leading zeros in chapter numbers
3. **Download Process**: Systematically downloads each chapter's commentary
4. **Exception Handling**: Contains special cases for non-standard URLs
5. **Compilation**: Merges all HTML files into a single document

## Directory Structure

```
bible-commentary-scraper/
├── scraper.py          # Main script
├── html/               # Directory for downloaded files
│   ├── genesis/        # Individual book directories
│   │   ├── 1.html
│   │   ├── 2.html
│   │   └── ...
│   ├── exodo/
│   └── ...
└── output.html         # Final compiled document
```

## Notes

- This script is designed specifically for the Spanish version of Enduring Word
- The script includes handling for special cases where multiple chapters are combined
- Be respectful of the website's resources by not running the script unnecessarily

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is intended for personal study purposes only. Please respect the copyright and terms of service of the website.
