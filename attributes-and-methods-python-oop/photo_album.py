class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):

        return cls(int(photos_count / 4))

    def add_photo(self, label):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return "No more free spots"

    def display(self):
        result = ""
        for p in range(len(self.photos)):
            result += "-----------\n"
            result += (len(self.photos[p]) * '[] ').rstrip() + '\n'
        result += "-----------\n"
        return result

# Test code
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
