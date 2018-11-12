# search_google

search_google/googleLyrics.ipynb parse each post to Google API. Result returns webpage link, webpage name and webpage content
      
search_google/count_keywords.ipynb  count the frequency of ‘lyric, quote’ in each search result then return the post with 
At least two search results contain one of those keywords then compare the cosine similarity between posts and retrieved webpage content. 

search_google/LabelResults/QuotesDetected_all.csv is the detected quotes and lyrics from 2000 posts. Score is the number of retrieved  document (webpage names) that contain the keywords. Cosinesim is the cosine similarity between the post and the retrieved webpage content. The labels


Files:
search_google/all.csv is the query results I collected so far (not finished)

search_google/sample_5000.csv is the posts we need to detect quotes and lyrics
