# search_google

search_google/googleLyrics.ipynb parse each post to Google API. Result returns webpage link, webpage name and webpage content
      
search_google/count_keywords.ipynb: rule-based classifer

search_google/MLClassifer.ipynb: three ML classifiers, their evaluations and evaluation of rule-based classifer

search_google/LabelResults/QuotesDetected_all.csv is the labels for quotes and lyrics (2000 posts) annotated by the rule based classifier. Score is the number of retrieved  documents (webpage names) that contain the keywords. Cosinesim is the cosine similarity between the post and the retrieved webpage content. The labels show whether the post is a quote, suspect or notQuote. see search_google/count_keywords.ipynb for the description of the classifier.


search_google/features.csv: this file shows what the features look like

search_google/searchResults: hashed object for the classifiers. This is the object we used in most of the computation.



Files (Not uploaded to github, files too big):
search_google/all.csv is the query results 

search_google/sample_5000.csv is the posts we need to detect quotes and lyrics
