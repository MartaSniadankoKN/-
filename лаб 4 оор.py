# Патерн Composite
class FileSystemComponent:
    def show(self, indent=0):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"File: {self.name}")

class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.show(indent + 2)

# Патерн Facade
class FileSystemFacade:
    def __init__(self):
        self.root = Folder("Root")

    def create_sample_structure(self):
        doc_folder = Folder("Documents")
        doc_folder.add(File("resume.docx"))
        doc_folder.add(File("report.pdf"))

        img_folder = Folder("Images")
        img_folder.add(File("photo1.jpg"))
        img_folder.add(File("photo2.png"))

        self.root.add(doc_folder)
        self.root.add(img_folder)
        self.root.add(File("readme.txt"))

    def show_structure(self):
        self.root.show()

# Використання фасаду
facade = FileSystemFacade()
facade.create_sample_structure()
facade.show_structure()
