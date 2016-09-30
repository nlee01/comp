from datetime import date
from PIL import Image

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year=year, month=month, day=day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        raise NotImplementedError


# TODO: Define an Article class that extends the Content class
class Article(Content):
    def __init__(self, year, month, day, contributors, headline, content):
        super(Article, self).__init__(year, month, day, contributors)
        self.headline = headline
        self.content = content
    def show(self):
        print 'Contributors'.join(self.contributors)
        print self.title
        print self.month
        print self.content
        print self.year
        print self.type
        print self.day
        
# TODO: Define a Picture class that extends the Content class
class Picture(Content):
    def __init__(self, year, month, day, contributors, title, caption, path):
        super(Picture, self).__init__(year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path
        
    def show(self):
        print 'Contributors'.join(self.contributors)
        print self.title
        print self.month
        Image.open(self.path)
        print self.caption
        print self.year
        print self.type
        print self.day
