# Imports.
import requests
import os
from bs4 import BeautifulSoup
from functools import partial

# Constants.
_ABC_NEWS_JUSTIN_PAGE= "http://www.abc.net.au/news/justin"
_NEWS_FILENAME = 'newsfile.html'

# General tag adder.
def _tagged(tag,textin):
	return("<" + tag + ">" + textin + "</" + tag + ">")

# Page linker.
def _linked(linktext,linkto):
	return('<a href="' + linkto + '">' + linktext + "</a>")
	
def _updated_heading(original_heading):
	"""
	Look for special last word and separate it from rest of sentence.
	"""
	word_list = original_heading.split()
	last_word = word_list[-1]
	pre_last_word = ' '.join(word_list[0:-1])
	if last_word in ("Explainer", "Analysis", "Opinion"):
		new_heading = pre_last_word + " (" + last_word + ")"
	else:
		new_heading = original_heading
	return new_heading

if __name__ == "__main__":

	# Scrape news page.
	page = requests.get(_ABC_NEWS_JUSTIN_PAGE)
	soup = BeautifulSoup(page.content, 'html.parser')
	articles = soup.find_all(class_="article-index")
	article_entries = articles[0].find_all('li')

	# Open HTML file.
	htmlfile=open(_NEWS_FILENAME,'w')

	# Add header.
	htmlfile.write("<head>")
	htmlfile.write('<link rel="stylesheet" type="text/css" href="default.css">')
	htmlfile.write("</head>")
	htmlfile.write("<body>")

	# Write non-sport articles to file.
	for article in article_entries:
		heading = _updated_heading(article.find('h3').get_text())
		p_lines = article.find_all('p')
		summary = p_lines[1].get_text()
		linkpage = _ABC_NEWS_JUSTIN_PAGE + article.find('a')['href']
		if len(p_lines) > 2:
			topics = p_lines[2].get_text()
			if "sport" not in topics:
				htmlfile.write(_tagged("p", _tagged("h1",heading)))
				htmlfile.write(_tagged("p", _tagged("h2","- " + summary)))
				htmlfile.write(_tagged("p", _tagged("h3",_linked('LINK',linkpage))))
				htmlfile.write(_tagged("p", _tagged("h4",topics)))

	# Close HTML file.
	htmlfile.write("</body>")
	htmlfile.close()

	# Display file.
	os.startfile(_NEWS_FILENAME)