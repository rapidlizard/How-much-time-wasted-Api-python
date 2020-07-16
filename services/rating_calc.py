from models.rating import Rating


class Rating_calc():

    def get_rating(self, hours: int):
        if hours >= 0 and hours <= 39:
            return Rating(title='What even are games?', description='Seriously what are they???')

        if hours >= 40 and hours <= 299:
            return Rating(title='You might aswell just play mobile games', description='Sponsored by RAID: Shadow Legends')

        if hours >= 300 and hours <= 599:
            return Rating(title='You gotta pump those numbers up. Those are rookie numbers', description='I myself have more than 1000 hours')

        if hours >= 600 and hours <= 999:
            return Rating(title='Even my mum has more hours on candy crush',
                          description="She's over level 9000")

        if hours >= 1000 and hours <= 1999:
            return Rating(title='Its all civilisation isnt it?',
                          description="Just one more turn")

        if hours >= 2000 and hours <= 3999:
            return Rating(title='You have a healthy balance',
                          description="Not too much but not too little")

        if hours >= 4000 and hours <= 5999:
            return Rating(title='Are you going pro??',
                          description="* insert wannabe esports pro starter pack *")

        if hours >= 6000 and hours <= 7999:
            return Rating(title='Certified Hardcore Gamer',
                          description="Get your certificate here: www.ImaHardcoreGamer.com")

        if hours >= 8000 and hours <= 9999:
            return Rating(title='Dude. Are you okay?',
                          description="When was the last time you went outside??")

        if hours >= 1000:
            return Rating(title='You need to seek medical help',
                          description=" https://www.nhs.uk/")
