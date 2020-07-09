class User():

    def __init__(self, name: str, img: str, url:str, created: str):
        self.name = name
        self.img = img
        self.url = url
        self.created = created

    def to_json(self):
        return {
            'name': self.name,
            'img': self.img,
            'url': self.url,
            'created': self.created
        }