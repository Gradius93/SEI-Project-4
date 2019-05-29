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

    cloudwater = Brewery(name='Cloudwater', founded='2014', area='Manchester', user=seanyg)
    buxton = Brewery(name='Buxton', founded='2017', area='Buxton', user=seanyg)
    northern_monks = Brewery(name='Northern Monks', founded='2013', area='Leeds', user=seanyg)
    brewdog = Brewery(name='Brewdog', founded='2007', area='Ellon', user=seanyg)
    kernel = Brewery(name='Kernel', founded='2010', area='London', user=seanyg)
    london_beer_factory = Brewery(name='London Beer Factory', founded='2014', area='London', user=seanyg)
    siren = Brewery(name='Siren', founded='2013', area='Wokingham', user=seanyg)
    magic_rock = Brewery(name='Magic Rock', founded='2011', area='Huddersfield', user=seanyg)
    north_brewing_co = Brewery(name='North Brewing Co.', founded='2015', area='Leeds', user=seanyg)
    wild_beer_co = Brewery(name='Wild Beer Co.', founded='2012', area='Shepton Mallet', user=seanyg)

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
        tasting_notes='This is a one-off brew to celebrate Indy Man Beer Con 2018. "DDH" means this Pale has been double dry hopped, using twice the amount of hops as our standard Pale. Expect big citrus and tropical fruit flavours, and a firm, smooth body combined with crushability.',
        user=seanyg
    )

    Beer(
        name='Eternal',
        brewery=northern_monks,
        style=ipa,
        hops='There are some but none specified online',
        region='UK',
        abv=4.1,
        price=2.39,
        tasting_notes='A product brewed for almost 7,000 years, a quest for perfection that never ends. Citrusy, light and refreshing. To Eternity.',
        user=seanyg
    )

    Beer(
        name='Jet Black Heart',
        brewery=brewdog,
        style=stout,
        hops='Hallertauer Taurus',
        region='UK',
        abv=4.7,
        price=2.00,
        tasting_notes='This stout is black as pitch and smooth as hell. Jet Black Heart is a milk stout with an ebony core. Loaded with oatmeal and primed for a velvet smooth delivery. Cacao, roasted coffee and berry fruits linger in its deepest darkest depths. Full-bodied, rich and decadent to the core.',
        user=seanyg
    )

    Beer(
        name='India Pale Ale, Vic Secret',
        brewery=kernel,
        style=ipa,
        hops='There are some but none specified online',
        region='UK',
        abv=7.0,
        price=3.00,
        tasting_notes='Hazy golden with white head. Dank fruity hops, light spices, white cheese, soft malts and dough, creamy peach, dank weeds, raw cocoa, gooseberries, toasted nuts. Medium sweet and bitter. Medium bodied. Quite some dank spices here',
        user=seanyg
    )

    Beer(
        name='Hazey Daze',
        brewery=london_beer_factory,
        style=ipa,
        hops='Citra, Mosaic, Vic Secret',
        region='UK',
        abv=4.6,
        price=1.80,
        tasting_notes='A juicy, crushable, session IPA with big tropical notes. Using fully flavoured hazy New England yeast this leaves a citrus hum on the tongue and lashings of pineapple on the nose.',
        user=seanyg
    )

    Beer(
        name='Calypso G901',
        brewery=siren,
        style=sour,
        hops='Cluster, Comet, Simcoe, Mosaic',
        region='UK',
        abv=4.0,
        price=2.00,
        tasting_notes='The newest addition to our core beer range is Calypso, the Goddess known for her sharp tongue. This beer is our homage to this enchantress, a tart, spritzy Berliner-style sour beer. Each batch is dry-hopped differently.',
        user=seanyg
    )

    Beer(
        name='Salty Kiss',
        brewery=magic_rock,
        style=sour,
        hops='Cascade',
        region='UK',
        abv=4.1,
        price=2.15,
        tasting_notes='Originally brewed as a collaboration with Kissmeyer Beer, this is our take on a traditional German style Gose, flavoured with fruit, sea buckthorn and sea salt. Tart, lightly sour, fruity and refreshing with a defined saltiness makes this beer an excellent accompaniment to food.',
        user=seanyg
    )

    Beer(
        name='Full Fathom 5',
        brewery=north_brewing_co,
        style=porter,
        hops='There are some but none specified online',
        region='UK',
        abv=6.5,
        price=3.45,
        tasting_notes='A dark and dreamy porter with rich flavours from single origin Rwandan coffee beans and a delicate toasted coconut aroma. Malty, toothsome and deliciously refreshing.',
        user=seanyg
    )

    Beer(
        name='Bibble',
        brewery=wild_beer_co,
        style=pale,
        hops='Magnum, Summit, Amarillo, Mosaic',
        region='UK',
        abv=4.2,
        price=2.25,
        tasting_notes='This session ale is the perfect fit for a can - fast, easy and delicious. Packed full of hops aromas with a solid malt base it’s a beer for all occasions. The name ‘Bibble’ in Somerset dialect means to drink loudly, often and well',
        user=seanyg
    )

    db.commit()
