import fitz
import os
import sys

def expand_pdf_for_annotations(pdf_path, extra_width=200):
    doc = fitz.open(pdf_path)
    expanded_pdf = fitz.open()
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        
        rect = page.rect
        new_rect = fitz.Rect(0, 0, rect.width + extra_width, rect.height)
        new_page = expanded_pdf.new_page(width=new_rect.width, height=new_rect.height)
        
        original_position = fitz.Rect(0, 0, rect.width, rect.height)
        new_page.show_pdf_page(original_position, doc, page_num)
    
    new_pdf_path = f"{os.path.splitext(pdf_path)[0]}_expanded.pdf"
    expanded_pdf.save(new_pdf_path)
    expanded_pdf.close()
    doc.close()
    
    print(f"Expanded PDF saved at: {new_pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        expand_pdf_for_annotations(pdf_path)
    else:
        print("Please provide a PDF file path.")
