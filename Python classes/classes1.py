class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def display(self):
        if isinstance(self.content, list):
            content_str = ", ".join(self.content)
        else:
            content_str = self.content
        print(f"Title: {self.title}\nContent: {content_str}")

shopping_note = Note("Shopping", ["Groceries", "M sized t-shirt", "Cat food"])
shopping_note.display()

car_note = Note("Buy a car", "BMW 116i 2012")
car_note.display()
