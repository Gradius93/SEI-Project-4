from pony.orm import db_session
from app import db
from models.Beer import Beer
from models.Brewery import Brewery
from models.Style import Style
from models.User import User, UserSchema

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():
    schema = UserSchema()
    seanyg = User(
        username='seanyg',
        email='sean.myles.gray@gmail.com',
        password_hash=schema.generate_hash('pass')
    )

    cloudwater = Brewery(name='Cloudwater')
    buxton = Brewery(name='Buxton')
    northern_monks = Brewery(name='Northern Monks')
    brewdog = Brewery(name='Brewdog')
    kernel = Brewery(name='Kernel')
    london_beer_factory = Brewery(name='London Beer Factory')
    siren = Brewery(name='Siren')
    magic_rock = Brewery(name='Magic Rock')
    north_brewing_co = Brewery(name='North Brewing Co.')
    wild_beer_co = Brewery(name='Wild Beer Co.')

    pale = Style(name='Pale')
    ipa = Style(name='IPA')
    dipa = Style(name='DIPA')
    sour = Style(name='Sour')
    stout = Style(name='Stout')
    imperial_stout = Style(name='Imperial Stout')
    lager = Style(name='Lager')
    lambic = Style(name='Lambic')
    table_beer = Style(name='Table Beer')
    neipa = Style(name='NE IPA')
    belgian = Style(name='Belgian')
    porter = Style(name='Porter')
    apa = Style(name='APA')

    Beer(
        name='AW-18 DDH Pale v1',
        brewery=cloudwater,
        style=pale,
        hops='There are some but none specified online',
        region='UK',
        abv=5.5,
        price=6.60,
        tasting_notes="This is a one-off brew to celebrate Indy Man Beer Con 2018. 'DDH' means this Pale has been double dry hopped, using twice the amount of hops as our standard Pale. Expect big citrus and tropical fruit flavours, and a firm, smooth body combined with crushability.",
        user=seanyg
    )
