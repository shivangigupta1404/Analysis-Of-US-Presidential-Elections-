import HTMLParser,re

def clean(text):
	#1: Escaping HTML characters
	html_parser=HTMLParser.HTMLParser()
	text=html_parser.unescape(text)
	#2: Decoding Data
	text=text.encode('utf-8',errors='ignore')
	#removing urls
	text= re.sub(r"http\S+", "", text)
	#removing user mentions
	text=' '.join(re.sub("(@[A-Za-z0-9_]+)|([^0-9A-Za-z_ \t])|(\w+:\/\/\S+)"," ",text).split())
	return text

def preprocess_str(str):
    str.replace('>','&gt;')
    str.replace('<','&lt;')
    str.replace("'",'&#39;')
    str.replace("&",'&amp;')
    str.replace('"','&quot;')
    return str