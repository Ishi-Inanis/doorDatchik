import numpy as np
import pandas as pd
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import docx
from pymystem3 import Mystem
from nltk.corpus import stopwords
from string import punctuation
alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

mystem = Mystem() 
russian_stopwords = stopwords.words("russian")

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
df = pd.read_csv('trein_data.csv')
group_df = df.groupby(by=['word'], as_index = False)['np'].mean()
sort_group_df = group_df.sort_values(by=['np'])
data = sort_group_df[ sort_group_df['np'] > 0.005]['word']

doc = docx.Document(filename)
print ("start")
for paragraph in doc.paragraphs:
	if(paragraph.text != ""):
		text = ""
		for run in paragraph.runs:
			text += run.text.lower() + " "
			tokens = mystem.lemmatize(text)
			tokens = [token for token in tokens if token not in russian_stopwords\
				and token != " " \
				and token.strip() not in punctuation\
				and len(token) > 2\
				and alphabet.isdisjoint(token) == 0]
			if ( tokens != []):
				for i_word in tokens:
					if ( i_word in data):
						print ( i_word + "присутствует в тексте")


