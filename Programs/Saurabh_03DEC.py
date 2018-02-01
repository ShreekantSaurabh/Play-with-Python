import datetime

class Note:
    def __init__(self, memo = '', tag='' ):
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tag = tag
        
    def match(self, search_filter = ''):
        if search_filter in self.memo or search_filter in self.tag:
            print('Match Found')
            return True
        else:
            print('Match Not Found')
            return False
        
"""
#Test the class Note
n1 = Note("abc", "tag1")
n2 = Note("def", "tag2")

n1.match('ab')
n2.match('tag2')
"""
        
class Notebook:
    
    def __init__(self, notes = []):
        self.notes = notes
    
    def New_Note(self, memo = '', tag = ''):
        self.notes.append(Note(memo, tag))      #if Note is in some other file then we have to import the NOte
        #n1 = Note(memo, tag)
        #self.notes.append(n1)
        
"""
#test the class Notebook
nb = Notebook()
nb.New_Note("First Python Class", "page 1")
nb.New_Note("Second Python Class", "page 2")

print(nb.notes[0].memo)
print(nb.notes[1].tag)
"""