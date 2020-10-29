class PhotoList:
    photo_list = {}
    index = 1

    def add(self, value):
        self.photo_list[self.index] = value
        self.index += 1
