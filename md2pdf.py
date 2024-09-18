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
import logging
from bs4 import BeautifulSoup

# 設置日誌
logging.basicConfig(filename='md2pdf.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def convert_md_to_pdf(md_file_path, pdf_file_path):
    try:
        # 讀取 Markdown 文件
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        logging.debug(f"Markdown content length: {len(md_content)}")
        
        # 將 Markdown 轉換為 HTML，保留更多格式
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        logging.debug(f"HTML content length: {len(html_content)}")
        
        # 註冊中文字體
        font_path = r'C:\Windows\Fonts\msyh.ttc'  # 微軟雅黑
        pdfmetrics.registerFont(TTFont('MSYaHei', font_path))
        
        # 創建樣式
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Chinese', fontName='MSYaHei', fontSize=10))
        
        # 創建 PDF 文檔
        doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
        story = []
        
        # 解析 HTML 並添加到 story
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
                    logging.debug(f"Successfully added: {text[:50]}...")  # 只記錄前50個字符
                except Exception as e:
                    logging.error(f"Error adding text: {text[:50]}...")
                    logging.error(f"Error message: {str(e)}")
        
        # 生成 PDF
        doc.build(story)
        
        print(f"已成功將 {md_file_path} 轉換為 {pdf_file_path}")
        print(f"Successfully converted {md_file_path} to {pdf_file_path}")
        messagebox.showinfo("成功 / Success", f"已成功將 {md_file_path} 轉換為 {pdf_file_path}\nSuccessfully converted {md_file_path} to {pdf_file_path}")
    except Exception as e:
        logging.error(f"Error converting file: {str(e)}", exc_info=True)
        messagebox.showerror("錯誤 / Error", f"轉換過程中發生錯誤：{str(e)}\nAn error occurred during conversion: {str(e)}")

def select_md_file():
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口
    md_file_path = filedialog.askopenfilename(title="選擇 Markdown 文件 / Select Markdown file", filetypes=[("Markdown files", "*.md")])
    if md_file_path:
        pdf_file_path = filedialog.asksaveasfilename(title="保存 PDF 文件 / Save PDF file", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_file_path:
            convert_md_to_pdf(md_file_path, pdf_file_path)

def main():
    print("歡迎使用 Markdown 轉 PDF 工具！")
    print("Welcome to Markdown to PDF Converter!")
    while True:
        choice = input("請選擇 / Please choose: 1. 轉換 Markdown 為 PDF / Convert Markdown to PDF 2. 退出 / Exit\n")
        if choice == '1':
            select_md_file()
        elif choice == '2':
            print("感謝使用，再見！")
            print("Thank you for using. Goodbye!")
            break
        else:
            print("無效的選擇，請重新選擇。")
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
