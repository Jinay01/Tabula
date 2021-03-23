import tabula
# pip3 install tabula-py
df = ("E:/USEFUL/OCR/Geeks For Geeks/Result of 60004190056 for Semester I held in DECEMBER , 2019.PDF")
output = ("E:/USEFUL/OCR/Geeks For Geeks/test1.csv")
tabula.convert_into(df, output, output_format="csv", pages="all", stream=True)
