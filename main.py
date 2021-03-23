import tabula
# pip3 install tabula-py
df = ("E:/USEFUL/OCR/Geeks For Geeks/pdf files/Result of 60004190056 for Semester II held in MAY , 2020.PDF")
output = ("E:/USEFUL/OCR/Geeks For Geeks/csv files/test2.csv")
tabula.convert_into(df, output, output_format="csv", pages="all", stream=True)
