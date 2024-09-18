# Markdown to PDF Converter (Markdown 轉 PDF 工具)

[English](#english) | [繁體中文](#繁體中文)

## English

### Introduction
This tool converts Markdown files to PDF format. It's designed to work on Windows systems and includes support for Chinese characters.

### Features
- Convert Markdown files to PDF
- Support for Chinese characters
- User-friendly interface

### Requirements
- Python 3.6+
- Windows operating system

### Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/markdown-to-pdf.git
   cd markdown-to-pdf
   ```
2. Install required packages:
   ```
   pip install markdown fpdf2
   ```

### Usage
1. Run the script:
   ```
   python md2pdf.py
   ```
2. Choose "1" to convert a Markdown file to PDF.
3. Select your Markdown file when prompted.
4. Choose a location to save the PDF file.

### Building Executable (Optional)
If you want to build a standalone executable:
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Build the executable:
   ```
   pyinstaller --onefile --add-data "msjh.ttc;." md2pdf.py
   ```
3. The executable will be in the `dist` folder.

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### License
[MIT License](LICENSE)

---

## 繁體中文

### 簡介
這個工具可以將 Markdown 文件轉換為 PDF 格式。它專為 Windows 系統設計，並支援中文字符。

### 功能
- 將 Markdown 文件轉換為 PDF
- 支援中文字符
- 用戶友好的界面

### 系統要求
- Python 3.6+
- Windows 操作系統

### 安裝
1. 克隆此儲存庫：
   ```
   git clone https://github.com/yourusername/markdown-to-pdf.git
   cd markdown-to-pdf
   ```
2. 安裝所需套件：
   ```
   pip install markdown fpdf2
   ```

### 使用方法
1. 運行腳本：
   ```
   python md2pdf.py
   ```
2. 選擇 "1" 來轉換 Markdown 文件為 PDF。
3. 在提示時選擇你的 Markdown 文件。
4. 選擇保存 PDF 文件的位置。

### 構建可執行文件（可選）
如果你想構建獨立的可執行文件：
1. 安裝 PyInstaller：
   ```
   pip install pyinstaller
   ```
2. 構建可執行文件：
   ```
   pyinstaller --onefile --add-data "msjh.ttc;." md2pdf.py
   ```
3. 可執行文件將在 `dist` 資料夾中。

### 貢獻
歡迎貢獻！請隨時提交 Pull Request。

### 許可證
[MIT 許可證](LICENSE)
