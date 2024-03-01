import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pdf2image import convert_from_path

def pdf_to_png(pdf_path, output_folder):
    # 使用pdf2image将PDF转换为图像
    images = convert_from_path(pdf_path)

    # 创建PdfPages对象，用于保存图像为PDF文件
    with PdfPages(output_folder + '/output.pdf') as pdf:
        # 将每个图像保存到PdfPages
        for i, img in enumerate(images):
           
            # 或者，保存图像为PNG文件
            img.save(output_folder + f'/page_{i + 1}.png', 'PNG')

# 使用示例
pdf_path = "C:/Users/wazi/Desktop/vtk/marine-model2.pdf"
output_folder = "C:/Users/wazi/Desktop"
pdf_to_png(pdf_path, output_folder)
