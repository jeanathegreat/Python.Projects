import sys

from bs4 import BeautifulSoup

h = """
<td>
200,90<br/>
196,90                          </td>
"""

soup = BeautifulSoup(h, "html.parser")
prices = soup.find("td").text.strip().split("\n")
print(prices[0], prices[1])
#200,90 196,90

# print(sys.version)
# print(sys.executable)