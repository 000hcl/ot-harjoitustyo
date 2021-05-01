class Save:
    def __init__(self, file):
        self.__file = file

    def load(self):
        try:
            content = self.__read_file()
        except:
            self.create_new_save_file()
            content = self.__read_file()
        result = content.split(",")
        print(result)

    def __read_file(self):
        with open(self.__file) as file:
            content = file.read()
        return content

    def file_is_valid(self):


    def create_new_save_file(self):
        with open(self.__file, "w") as file:
            file.write("0,0,0,0,0,0,0,0,0,0")


s = Save("test.csv")
s.load()