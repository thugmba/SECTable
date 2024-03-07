from bs4 import BeautifulSoup

# Assuming you have HTML content stored in a variable called html_content
# You should replace this with your HTML content or load it from a file/url
html_content = """
<html>
<head><title>Example</title></head>
<body>
<p>This is some text before the table.</p>
<table>
  <tr><td>Row 1, Column 1</td><td>Row 1, Column 2</td></tr>
  <tr><td>Row 2, Column 1</td><td>Row 2, Column 2</td></tr>
</table>
<p>This is some text after the table.</p>
<table>
  <tr><td>Second Table Row 1, Column 1</td><td>Second Table Row 1, Column 2</td></tr>
  <tr><td>Second Table Row 2, Column 1</td><td>Second Table Row 2, Column 2</td></tr>
</table>
</body>
</html>
"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first occurrence of the text you're looking for
target_text = "This is some text before the table."
target_element = soup.find(string=target_text)

# Find the first table tag after the target text
table_after_text = target_element.find_next('table')

# Now you have the first table tag after the specified text
print(table_after_text)