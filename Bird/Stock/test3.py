import re
pattern = re.compile(r'#999999')
str = 'F:\\StockData\\SH#999999.txt'
asd = pattern.search(str)
#asd = re.match(pattern, str)
print(asd.group(0))