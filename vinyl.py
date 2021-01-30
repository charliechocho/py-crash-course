class Vinyl:
    """A class that models a vinyl record"""

    def __init__(self,artist,album):
        """Initialize what group or artist it is and the name of the album"""

        self.artist = artist
        self.album = album

    def rpm_45(self):
        """Describe at what rpm the record is supposed to be played"""
        print(f"{self.album} is a 45 rpm vinyl!")

    def colored(self):
        print(f"{self.artist} {self.album} is a colored vinyl!")

my_record = Vinyl('beatles', 'abbey road')
my_record_two = Vinyl('ayreon', 'the final experiment')

print(f"I've got a an album with {my_record.artist}. The album is {my_record.album}")
print(f"I've got a an album with {my_record_two.artist}. The album is {my_record_two.album}")

my_record.rpm_45()
my_record.colored()
my_record_two.rpm_45()
my_record_two.colored()