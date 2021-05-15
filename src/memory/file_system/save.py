class Save:
    """
    The save file, which in this case is the leaderboard.

    Attributes:
        file: The file to read from.
        result: The contents of the file.
    """
    def __init__(self, file):
        """
        Constructor for the Save object.

        Args:
            file: The file to be read from.
        """
        self.__file = file
        self.__result = self.load()

    def load(self):
        """
        Finds a valid leaderboard. If the current result is not valid,
         rewrite the result as an empty leaderboard.

        Returns:
            A correct result.
        """
        if not self.__file_is_valid():
            self.__create_new_save_file()
        result = self.__read_file()
        return result

    def update(self, number):
        """
        Adds a new number to the leaderboard and updates the file.
        
        Args:
            number: A new result to be added to the leaderboard.
        """
        if not isinstance(number, int):
            return
        if number < 0 or number > 105000:
            return
        self.__result.append(number)
        self.__result.sort(reverse = True)
        new_result = []
        for number in range(10):
            new_result.append(self.__result[number])
        self.__result = new_result
        self.__write_save_file(self.__result)

    def __write_save_file(self, result):
        """
        Converts the current leaderboard into csv and
        rewrites the file.

        Args:
            result: The list to be written.
        """
        result = [str(x) for x in result]
        res_string = ",".join(result)
        with open(self.__file, "w") as file:
            file.write(res_string)


    def __read_file(self):
        """
        Reads the file.

        Returns:
            The contents of the file in list form.
        """
        with open(self.__file) as file:
            content = file.read()
        result = content.split(",")
        result = [int(x) for x in result]
        return result


    def __file_is_valid(self):
        """
        Checks the validity of the file.

        Returns:
            True if it seems valid, otherwise
            False.
        """
        try:
            result = self.__read_file()
            if len(result) != 10:
                return False
            previous = 105001
            for number in result:
                if number > previous:
                    return False
                if number < 0:
                    return False
                previous = number

        except:
            return False
        return True

    def __create_new_save_file(self):
        """
        Creates an empty leaderboard and writes
        it in the file.
        """
        new = [0 for x in range(10)]
        self.__write_save_file(new)

    @property
    def result(self):
        """
        Returns the current loaded leaderboard.
        """
        return self.__result
