
import bs4

data = """
<html lang="en">
<head>
<meta charset="utf-8">
</head>
<body>
<div class="container">
<a href='this.com'>this</a>
</div>
<div class="container2">
<a href='this2.com'> this2</a>
<p> this is a row </p>
</div>
</body>
</html>
"""
soup = bs4.BeautifulSoup(data, 'html.parser')
# print(soup.head)
# print(soup.div.find_all('a'))
print(soup.find_all('div')[1].find_all('a'))