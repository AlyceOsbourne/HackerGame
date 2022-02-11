from dataclasses import dataclass, field
from io import StringIO, BytesIO


@dataclass(slots=True)
class File:
    file_name: str
    file_extension: str
    file_data: StringIO or BytesIO

    def __str__(self):
        return self.file_name+"."+self.file_extension
    # todo needs enter and exit dunders


@dataclass
class Folder:
    def __init__(self, name, parent: object = None, children: dict = None):
        self.name = name
        self.parent = parent if isinstance(parent, self.__class__) else None
        self.depth = parent.depth+1 if parent and isinstance(parent, self.__class__) else 1
        self.children = children if children else {}

    # todo needs enter and exit dunders

    def new_folder(self, folder_name: str, children=None):
        print(f"attempting to create folder: {folder_name}, with children: {children}")
        folder = self._create_(name=folder_name, parent=self, children=children if children else {})
        self.children.update({folder_name: folder})
        print(f"file {'creation failed' if folder_name not in self.children.keys() else 'created successfully'}")
        return folder

    def new_file(self, filename: str, create_directories=True, file_data = None):
        if create_directories:
            split_text = filename.split("/", 1)
            if len(split_text) > 1:
                foldername = split_text[0].replace("/", "")
                if foldername not in self.children.keys():
                    self.new_folder(foldername).new_file(split_text[1], create_directories, file_data)
                else:
                    self.children[foldername].new_file(split_text[1], create_directories, file_data)
            else:
                print(f"attempting to create file{split_text[0]}")
                split_text = split_text[0].split(".")
                filename = split_text[0]
                fileextension = split_text[1] if len(split_text) > 1 else ""
                print(f"name: {filename}, extension: {fileextension}")
                self.children.update({filename: File(filename, fileextension, file_data)})

    @classmethod
    def _create_(cls, name, parent, children):
        return cls(name, parent, children)

    def __str__(self):
        out = self.name
        for c in self.children.values():
            out+="\n"
            for i in range(self.depth):
                out+="\t"
            out+=str(c)
        return out


@dataclass
class FileSystem:
    root = Folder("Root:")
    def __str__(self):
        return self.root.__str__()

fs = FileSystem()
fs.root.new_folder("user")
fs.root.new_file("user/docs/file.txt")
fs.root.new_file("system/settings.ini")
print(fs)