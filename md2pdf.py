import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
import logging
from bs4 import BeautifulSoup

# Set up logging / 設置日誌
logging.basicConfig(filename='md2pdf.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def convert_md_to_pdf(md_file_path, pdf_file_path):
    try:
        # Read Markdown file / 讀取 Markdown 文件
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        logging.debug(f"Markdown content length: {len(md_content)}")
        
        # Convert Markdown to HTML, preserving more formatting / 將 Markdown 轉換為 HTML，保留更多格式
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        logging.debug(f"HTML content length: {len(html_content)}")
        
        # Register Chinese font / 註冊中文字體
        if getattr(sys, 'frozen', False):
            # If running as a bundled exe / 如果是打包後的 exe 運行
            font_path = os.path.join(sys._MEIPASS, 'msyh.ttc')
        else:
            # If running as a script / 如果是腳本直接運行
            font_path = r'C:\Windows\Fonts\msyh.ttc'
        pdfmetrics.registerFont(TTFont('MSYaHei', font_path))
        
        # Create styles / 創建樣式
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Chinese', fontName='MSYaHei', fontSize=10))
        
        # Create PDF document / 創建 PDF 文檔
        doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
        story = []
        
        # Parse HTML and add to story / 解析 HTML 並添加到 story
        soup = BeautifulSoup(html_content, 'html.parser')
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            if tag.name.startswith('h'):
                size = 18 - int(tag.name[1])  # h1 = 17, h2 = 16, ...
                style = ParagraphStyle(name=f'Heading{tag.name[1]}', parent=styles['Heading1'], fontSize=size, fontName='MSYaHei')
            else:
                style = styles['Chinese']
            
            text = tag.get_text().strip()
            if text:
                try:
                    para = Paragraph(text, style)
                    story.append(para)
                    story.append(Spacer(1, 12))
                    logging.debug(f"Successfully added: {text[:50]}...")  # Only log the first 50 characters / 只記錄前50個字符
                except Exception as e:
                    logging.error(f"Error adding text: {text[:50]}...")
                    logging.error(f"Error message: {str(e)}")
        
        # Generate PDF / 生成 PDF
        doc.build(story)
        
        print(f"Successfully converted {md_file_path} to {pdf_file_path}")
        print(f"已成功將 {md_file_path} 轉換為 {pdf_file_path}")
        messagebox.showinfo("Success / 成功", f"Successfully converted {md_file_path} to {pdf_file_path}\n已成功將 {md_file_path} 轉換為 {pdf_file_path}")
    except Exception as e:
        logging.error(f"Error converting file: {str(e)}", exc_info=True)
        messagebox.showerror("Error / 錯誤", f"An error occurred during conversion: {str(e)}\n轉換過程中發生錯誤：{str(e)}")

def select_md_file():
    md_file_path = filedialog.askopenfilename(title="Select Markdown file / 選擇 Markdown 文件", filetypes=[("Markdown files", "*.md")])
    if md_file_path:
        pdf_file_path = filedialog.asksaveasfilename(title="Save PDF file / 保存 PDF 文件", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_file_path:
            convert_md_to_pdf(md_file_path, pdf_file_path)

def main():
    root = tk.Tk()
    root.title("Markdown to PDF Converter / Markdown 轉 PDF 工具")
    root.geometry("300x100")

    label = tk.Label(root, text="Welcome to Markdown to PDF Converter!\n歡迎使用 Markdown 轉 PDF 工具！")
    label.pack(pady=10)

    convert_button = tk.Button(root, text="Convert Markdown to PDF\n轉換 Markdown 為 PDF", command=select_md_file)
    convert_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
