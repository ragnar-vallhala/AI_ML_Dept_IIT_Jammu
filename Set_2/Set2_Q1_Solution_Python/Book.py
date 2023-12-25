
class Book:
    
    def __init__(self, title, author, isbn, available_copies, total_copies) -> None:
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available_copies = available_copies
        self._total_copies = total_copies
    
    def __str__(self) -> str:
        info = ''
        info+="Book Info\n"
        info+="Title: "+self._title+"\n"
        info+="Author: "+self._author+"\n"
        info+="ISBN: "+self._isbn+"\n"
        info+="Available Copies: "+str(self._available_copies)+"\n"
        info+="Total Copies: "+str(self._total_copies)+"\n"
        return info
    
    def display_info(self):
        print(str(self))
    
    