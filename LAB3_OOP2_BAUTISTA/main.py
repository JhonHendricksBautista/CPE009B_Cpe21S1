from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter


df = FileReaderWriter()
df.read()
df.write()


c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath="sample2.csv", data=["Hello", "World"])


j = JSONFileReaderWriter()
j.read("sample.json")
j.write(filepath="sample2.json", data=[{'foo': 'bar'},{'koo':'pal'}])

