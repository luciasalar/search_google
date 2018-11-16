class mySearchRes:
    def __init__(self,text):
        self.quoteText = text
        self.quoteID = hash(self.quoteText)
        self.link = []
        self.name = []
        self.description = []
        
    def __hash__(self):
        return self.quoteID


def search_google(file):
    for row in file:
        texthash = hash(row)
        if texthash not in objects:
            #print(row)
            objects[texthash] = mySearchRes(row)
        search_results = google.search(row, 1)
            #search_results = [[text, i.link, i.name,i.description] for i in google.search(text, num_page)]
        for i in search_results:
             objects[texthash].link.append(i.link)
#         objects.name.append(search_results.name)
#         objects.description.append(search_results.description)

search_google(posts['text'][1:3])