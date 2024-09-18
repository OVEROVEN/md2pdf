import markdown
from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import re

class MyFPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

def convert_md_to_pdf(md_file_path, pdf_file_path):
    # 讀取 Markdown 文件
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    # 獲取 Markdown 文件所在的目錄
    md_dir = os.path.dirname(md_file_path)
    
    # 將 Markdown 轉換為 HTML
    html_content = markdown.markdown(md_content)
    
    # 創建 PDF 對象
    pdf = MyFPDF()
    pdf.add_page()
    
    # 添加中文字體
    font_path = "C:\\Windows\\Fonts\\msjh.ttc"  # 微軟正黑體路徑
    pdf.add_font('MSJHFont', '', font_path, uni=True)
    pdf.add_font('MSJHFont', 'B', font_path, uni=True)
    pdf.add_font('MSJHFont', 'I', font_path, uni=True)
    pdf.add_font('MSJHFont', 'BI', font_path, uni=True)
    pdf.set_font('MSJHFont', '', 12)
    
    # 處理圖片路徑
    def handle_image(match):
        img_path = match.group(1)
        full_img_path = os.path.join(md_dir, img_path)
        if os.path.exists(full_img_path):
            pdf.image(full_img_path, w=150)
            return ''
        else:
            return f'[圖片未找到: {img_path}]'
    
    # 替換 HTML 中的圖片標籤
    html_content = re.sub(r'<img.*?src="(.*?)".*?>', handle_image, html_content)
    
    # 將 HTML 內容寫入 PDF
    pdf.write_html(html_content)
    
    # 保存 PDF 文件
    pdf.output(pdf_file_path)
    print(f"已成功將 {md_file_path} 轉換為 {pdf_file_path}")
    messagebox.showinfo("成功", f"已成功將 {md_file_path} 轉換為 {pdf_file_path}")

def select_md_file():
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口
    md_file_path = filedialog.askopenfilename(title="選擇 Markdown 文件", filetypes=[("Markdown files", "*.md")])
    if md_file_path:
        pdf_file_path = filedialog.asksaveasfilename(title="保存 PDF 文件", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_file_path:
            convert_md_to_pdf(md_file_path, pdf_file_path)

def main():
    while True:
        choice = input("請選擇: 1. 轉換 Markdown 為 PDF 2. 退出\n")
        if choice == '1':
            select_md_file()
        elif choice == '2':
            break
        else:
            print("無效的選擇，請重新選擇。")

if __name__ == "__main__":
    main()
