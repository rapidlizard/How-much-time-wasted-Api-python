from services.rating_calc import Rating_calc
from models.rating import Rating


def test_user_calculates_rating_when_hours_0_49():
    expected = Rating(title='What even are games?',
                      description='Seriously what are they???')

    rating = Rating_calc().get_rating(30)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_50_299():
    expected = Rating(title='You might aswell just play mobile games',
                      description='Sponsored by RAID: Shadow Legends')

    rating = Rating_calc().get_rating(190)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_300_599():
    expected = Rating(title='You gotta pump those numbers up. Those are rookie numbers',
                      description='I myself have more than 1000 hours')

    rating = Rating_calc().get_rating(400)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_600_999():
    expected = Rating(title='Even my mum has more hours on candy crush',
                      description="She's over level 9000")

    rating = Rating_calc().get_rating(750)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_1000_1999():
    expected = Rating(title='Its all civilisation isnt it?',
                      description="Just one more turn")

    rating = Rating_calc().get_rating(1500)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_2000_3999():
    expected = Rating(title='You have a healthy balance',
                      description="Not too much but not too little")

    rating = Rating_calc().get_rating(2999)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_4000_5999():
    expected = Rating(title='Are you going pro??',
                      description="* insert wannabe esports pro starter pack *")

    rating = Rating_calc().get_rating(5000)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_6000_7999():
    expected = Rating(title='Certified Hardcore Gamer',
                      description="Get your certificate here: www.ImaHardcoreGamer.com")

    rating = Rating_calc().get_rating(6500)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_8000_9999():
    expected = Rating(title='Dude. Are you okay?',
                      description="When was the last time you went outside??")

    rating = Rating_calc().get_rating(8500)

    assert rating.title == expected.title
    assert rating.description == expected.description


def test_user_calculates_rating_when_hours_more_10_000():
    expected = Rating(title='You need to seek medical help',
                      description=" https://www.nhs.uk/")

    rating = Rating_calc().get_rating(15_000)

    assert rating.title == expected.title
    assert rating.description == expected.description
