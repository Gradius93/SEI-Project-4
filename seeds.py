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

    cloudwater = Brewery(
        name='Cloudwater',
        logo='https://static1.squarespace.com/static/5b82b075697a98a304da1872/t/5b9653f203ce64eefd2710d6/1558803635027/?format=1500w', image='https://static1.squarespace.com/static/55a8de09e4b0090a7a1ac6de/t/55e5f7fae4b05237dd5ae303/1441134592265/Cloudwater_brew_Co_002_brewery_photography',
        founded='2014',
        area='Manchester',
        info='Our work at Cloudwater starts with the intention of helping you relax and unwind with the finest quality modern beers we can make. We employ all the passion, skills, dreams, and experience of our team, and harness up-to-the-minute brewing science and techniques, out of respect for the ingredients our suppliers work hard to grow and process, and out of our gratitude for your support and trust. Outside our range of evolving and one-off seasonal beers, we collaborate with some of the world’s best breweries, and we also produce modern takes on classic styles. Though modern beer is our focus, we honour those that trail-blaze around us, and that pioneered before us by a constant focus on quality and innovation.',
        user=seanyg)

    buxton = Brewery(
        name='Buxton',
        logo='https://i0.wp.com/www.thedrinkers.co.uk/wp-content/uploads/2017/12/buxton.png?fit=1055%2C1200&ssl=1',
        image='https://static1.squarespace.com/static/59a862328fd4d227956d1f66/t/5a5e736ce2c4834114a25f23/1516140513892/DSC06411-01.jpeg',
        founded='2017',
        area='Buxton',
        info='Buxton is a craft micro-brewery, launched in 2008 and located in Buxton, UK. They brew tasty, aromatic, full flavoured, characterful beers. Using hops from all over the world, and the finest specialty malts that they can get their hands on.',
        user=seanyg
)

    northern_monks = Brewery(
        name='Northern Monks',
        logo='https://static1.squarespace.com/static/56e53b52859fd07e03b6c49f/t/5ac46e2d758d46be7f08e0d3/1522822711814/Screen+Shot+2018-04-04+at+06.47.23.png',
        image='https://www.leeds-art.ac.uk/media/563129/northern-monk-header.jpg',
        founded='2013',
        area='Leeds',
        info='Inspired by our northern surroundings and the history of monastic brewing practiced across the region for thousands of years, we commit ourselves to creating the highest quality beers, combining the best of traditional monastic brewing values with a progressive approach to ingredients and techniques. Community and collaboration are at the core of our business. We focus on working with anyone who shares our passion, and our values. We regularly collaborate with national and international breweries, businesses and charities to help strengthen the north for positive change, and to continually diversify our own offering. One of the ways we do this is through our patrons projects.',
        user=seanyg
    )

    magic_rock = Brewery(
        name='Magic Rock',
        logo='https://www.magicrockbrewing.com/cms/wp-content/themes/magicrock/images/logo@2x.png',
        image='https://www.magicrockbrewing.com/cms/wp-content/uploads/2015/10/brewery-hire-web.jpg',
        founded='2011',
        area='Huddersfield',
        info='Inspired by local brewing traditions and the vibrant US craft beer scene, Magic Rock Brewing is the culmination of a lifelong passion for beer. Richard Burhouse (aided by head brewer Stuart Ross) started the brewery in 2011 in an old out-building of the family business (an importer of crystals and natural gifts) in Huddersfield, West Yorkshire. // Alongside a distinctive core range we produce an ever changing line up of idiosyncratic beers with an innovative quality driven approach. Our Same but Different beers are packed with intense yet approachable flavours which will challenge and inspire, but above all remain balanced and drinkable.',
        user=seanyg
    )

    siren = Brewery(
        name='Siren',
        logo='https://www.eebriatrade.com/media/products/10831/20180530184231635/450x450.jpg',
        image='https://www.eebria.com/media/company/33/tallheader.jpg',
        founded='2013',
        area='Wokingham',
        info='Siren Craft Brew was born in 2013 with a simple idea in mind: to introduce exciting, full-ﬂavoured and forward-thinking beers to as many people as possible. // There are now six Sirens of Siren Craft Brew. These Sirens characterise our flagship beers. They\'re adventurous but drinkable, designed to be accessible to those lured into craft beer, yet flavourful enough for those seasoned beer fans to return to time and time again. // In addition, we have a prolific brewing schedule, with over 100 releases planned in 2019 alone. We are lucky enough to have been named the "Best Brewer in England" by Ratebeer users in 2015, and added to that with a Supreme Champion Beer of Britain award by CAMRA this year in 2018.',
        user=seanyg
    )

    kernel = Brewery(
        name='Kernel',
        logo='https://www.beyondbeer.de/media/image/39/58/d3/the_kernel-logo-beyond-beer1.png',
        image='https://static1.squarespace.com/static/5055e59ce4b02b42cb30023c/t/5a48f4a50d92977993059408/1514730674825/56.jpg?format=1500w',
        founded='2010',
        area='London',
        info='The brewery springs from the need to have more good beer. Beer deserving of a certain attention. Beer that forces you to confront and consider what you are drinking. Upfront hops, lingering bitternesses, warming alcohols, bodies of malt. Lengths and depths of flavour. We make Pale Ales, India Pale Ales and old school London Porters and Stouts towards these ends. Bottled alive, to give them time to grow.',
        user=seanyg
    )

    wild_beer_co = Brewery(
        name='Wild Beer Co.',
        logo='https://pbs.twimg.com/profile_images/1088804900677533697/_BR7ZxYZ.jpg',
        image='https://www.insidermedia.com/uploads/news/Wild_Beer_Co_cgi_1.jpg',
        founded='2012',
        area='Shepton Mallet',
        info='Unconstrained by stylistic guidelines and led by flavour, we celebrate traditional techniques whilst embracing a sense of modernity in our brewing. We want to give you a truly memorable drinking experience, altering your perceptions of beer and thrilling your taste buds. Whether it\'s hoppy freshness, stout sweetness or sour and refined barrel-aged flavours that you\'re after, rest assured you\'ll find them here.',
        user=seanyg)

    london_beer_factory = Brewery(
        name='London Beer Factory',
        logo='https://static.designmynight.com/uploads/2017/05/londonbeerfactory-1-optimised.jpg',
        image='https://imbibe.com/media/31294/beer-factory-crowdfunding.jpg',
        founded='2014',
        area='London',
        info='The London Beer Factory is a craft brewery founded in early 2014 by brothers Ed and Sim Cotton. // From day one we have been committed to producing beer with character; beer with unique flavours and engaging aromas; beer brimming with personality and distinctive qualities.// Distilling these principles into every single brew, we have developed a broad range of unfiltered, unpasteurised beer, incorporating a wide array of hops and malts from around the world. //Our Core Range includes five beers, all of which are available in keg, can and bottle format.',
        user=seanyg
    )

    north_brewing_co = Brewery(
        name='North Brewing Co.',
        logo='https://www.northbrewing.com/wp-content/uploads/2016/12/North-Brewing-Co-Logo-bk-2.png',
        image='https://cdn-b.william-reed.com/var/wrbm_gb_hospitality/storage/images/7/7/7/5/2595777-1-eng-GB/North-Brewing-Co-growing-across-the-globe_wrbm_large.jpg',
        founded='2015',
        area='Leeds',
        info='North Brewing Co was founded in 2015 by John Gyngell and Christian Townsley, the pioneers behind legendary Leeds beer venue North Bar, which opened in 1997. Known as “the first craft beer bar in Britain”, North Bar influenced a new wave of modern beer bars and breweries across the country, including their own. // In 2015 they turned their 10-year dream of making their own beer into a reality by opening a 15bbl brewery, featuring a 200-person capacity tap room, just half a mile from their original flagship North Bar in Leeds.',
        user=seanyg
    )


    brewdog = Brewery(
        name='Brewdog',
        logo='https://www.craftbeerjoe.com/wp-content/uploads/2018/01/brewdog-logo-crest.jpg',
        image='https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/04/10/13/brewdog1.gif',
        founded='2007',
        area='Ellon',
        info='BrewDog was born with the aim to revolutionize the beer industry and completely redefine beer-drinking culture. We’re determined to make a stand for independence, a stand for quality and stand for craft. And a big part of this is shamelessly spreading our passion for great craft beer. // That’s why every BrewDog bar offers a free Beer School, where our cicerone-trained crew will lead folks through a beer-tasting and walk them through the brewing process.',
        user=seanyg
    )

    white_hag = Brewery(
        name='White Hag',
        logo='https://static1.squarespace.com/static/58543435440243bd141ac1f3/t/5a5fbfd88165f51098cd0076/1516224473745/white-hag.png',
        image='https://www.belgiansmaak.com/wp-content/uploads/ngg_featured/IMG_6806.jpg',
        founded='2012',
        area='Sligo, Ireland',
        info='White Hag are one of the most exciting brewers to emerge from the recent explosion of craft breweries in Ireland. Brewing on Ireland\'s west coast, they use traditional and modern brewing techniques to explore native Irish styles as well putting their own spin on well known styles like IPA and imperial stout. White Hag refers to elements within Irish mythology which tell of a witch and a goddess, concerned with creation, the harvest and weather, and is Mother Nature herself.',
        user=seanyg
    )

    partizan = Brewery(
        name='Partizan',
        logo='https://2.bp.blogspot.com/-F_6zQqYSopE/V5XktHbYfEI/AAAAAAAAHZM/We5IIqcmRCsuW20CK-_Y72zo2yfRdyISQCLcB/s1600/Partizan_Brewing_Logotype.jpg',
        image='https://cdn-images-1.medium.com/max/2600/1*vdHqUvuVZTSEd7mmYYAlNw.jpeg',
        founded='2012',
        area='Bermondsey',
        info='Partizan Brewing was started by Andy Smith in 2012. Brewing in London in South Bermondsey, Partizan is producing interesting and creative bottle conditioned beers. Their label artwork is produced by illustrator Alec Doherty, sticking a signature style to all of their beers. HonestBrew has got to know Partizan as fellow LBA (London Brewers Alliance) members. We enjoy their beautifully crafted Saisons at home beside the barbecue.',
        user=seanyg
    )



    pale = Style(
        name='Pale',
        info='Pale ale is an ale made with predominantly pale malt. The highest proportion of pale malts results in a lighter colour. The term \'pale ale\' first appeared around 1703 for beers made from malts dried with high-carbon coke, which resulted in a lighter colour than other beers popular at that time. Different brewing practices and hop levels have resulted in a range of different tastes and strengths within the pale ale family.'
    )

    ipa = Style(
        name='IPA',
        info='India pale ale (IPA) is a hoppy beer style within the broader category of pale ale. The term \'pale ale\' originally denoted an ale brewed from pale malt. Among the first brewers known to export beer to India was Englishman George Hodgson\'s Bow Brewery on the Middlesex-Essex border. Bow Brewery beers became popular among East India Company traders in the late 18th century because of the brewery\'s location near the East India Docks in Blackwall. The export style of pale ale, which had become known as \'India pale ale\', developed in England around 1840, and it later became a popular product there.On the other hand, IPAs have a long history in Canada and the United States, and many breweries there produce a version of the style.'
    )

    dipa = Style(
        name='DIPA',
        info='Double IPAs Also called “Imperial” IPAs, this uniquely American style takes the craving for hops and runs with it. These usually use double or even triple the typical amount of hops, but also add more malts to balance. The resulting beer has huge hoppy highs and deep malty depths with an high ABV to match.'
    )

    sour = Style(
        name='Sour',
        info='Sour beer is beer which has an intentionally acidic, tart or sour taste. The most common sour beer styles are Belgian lambics, gueuze and Flanders red ale. Unlike modern brewing, which is done in a sterile environment to guard against the intrusion of wild yeast, historically the starter used from one batch to another usually contained some wild yeast and bacteria. Sour beers are made by intentionally allowing wild yeast strains or bacteria into the brew, traditionally through the barrels or during the cooling of the wort in a coolship open to the outside air. The most common agents used to intentionally sour beer are Lactobacillus, Brettanomyces, and Pediococcus. Another method for achieving a tart flavor is adding fruit during the aging process to spur a secondary fermentation. Because of the uncertainty involved in using wild yeast, the sour beer brewing process is extremely unpredictable. The beer takes months to ferment and can take years to mature.'
    )

    stout = Style(
        name='Stout',
        info='Stout is a dark beer. There are a number of variations, including Baltic porter, milk stout, and imperial stout; but the most common variation is dry stout, as exemplified by Guinness Draught, the world\'s best-selling stout. Stout is a top-fermented beer. The first known use of the word stout for beer was in a document dated 1677 found in the Egerton Manuscripts, the sense being that a "stout beer" was a strong beer, not a dark beer. The name porter was first used in 1721 to describe a dark brown beer that had been made with roasted malts. Because of the huge popularity of porters, brewers made them in a variety of strengths. The stronger beers, typically 7% or 8% alcohol by volume (ABV), were called "stout porters", so the history and development of stout and porter are intertwined, and the term stout has become firmly associated with dark beer, rather than just strong beer.'
    )

    imperial_stout = Style(
        name='Imperial Stout',
        info='Imperial stout, also known as Russian imperial stout or imperial Russian stout, is a strong dark beer or stout in the style that was brewed in the 18th century by Thrale\'s brewery in London for export to the court of Catherine II of Russia. In 1781 the brewery changed hands and the beer became known as Barclay Perkins Imperial Brown Stout. When the brewery was taken over by Courage the beer was renamed Courage Imperial Russian Stout (IRS). It has a high alcohol content, usually over 9% abv. It is among the darkest available beer styles.'
    )

    lager = Style(
        name='Lager',
        info='Lager is a type of beer conditioned at low temperatures. Lagers can be pale, amber, or dark. Pale lager is the most widely consumed and commercially available style of beer. As well as maturation in cold storage, most lagers are also distinguished by the use of Saccharomyces pastorianusyeast, a "bottom-fermenting" yeast that also ferments at relatively cold temperatures. It is possible to use lager yeast in a warm fermentation process, such as with American steam beer; while German Altbier and Kölsch are brewed with Saccharomyces cerevisiae top-fermenting yeast at a warm temperature, but with a cold-storage finishing stage, and classified as obergäriges lagerbier (top-fermented lager beer). Until the 19th century, the German word lagerbier (de) referred to all types of bottom-fermented, cool-conditioned beer in normal strengths. In Germany today, it mainly refers to beers in southern Germany, "Helles" (pale) and "Dunkel" (dark). Pilsner, a more heavily hopped pale lager, is most often known as "Pilsner", "Pilsener", or "Pils". Other lagers are Bock, Märzen, and Schwarzbier. In the United Kingdom, the term commonly refers to pale lagers derived from the Pilsner style.'
    )

    neipa = Style(
        name='NE IPA',
        info='New England India pale ales are a style of IPA invented in Vermont in the early 2010s. They are characterized by juicy, citrus, and floral flavours, with a more subtle and less piney hop taste than typical IPAs. They also have a smooth consistency or mouthfeel, and a hazy appearance. These characteristics are achieved using a combination of brewing techniques, including the use of particular strains of yeast, the timing of adding the hops, and adjusting the chemistry of the water. The style has become popular among New England brewers. New England IPAs need not be brewed in New England. It was officially recognized as a separate beer style, the Juicy or Hazy India Pale Ale, by the Brewers Association in 2018.'
    )

    porter = Style(
        name='Porter',
        info='Porter is a dark style of beer developed in London from well-hopped beers made from brown malt. The name was first recorded in the 18th century, and is thought to come from its popularity with street and river porters, who carried objects for others. The history and development of stout and porter beer types are intertwined. The name "stout", used for a dark beer, is believed to have come about because strong porters were marketed under such names as "extra porter", "double porter", and "stout porter". The term stout porter would later be shortened to just stout. For example, Guinness Extra Stout was originally called "Extra Superior Porter" and was only given the name "Extra Stout" in 1840.'
    )

    apa = Style(
        name='APA',
        info='American pale ale (APA) is a style of pale ale developed in the United States around 1980. American pale ales are generally around 5% abv with significant quantities of American hops, typically Cascade. Although American brewed beers tend to use a cleaner yeast, and American two row malt, it is particularly the American hops that distinguish an APA from British or European pale ales. The style is close to the American India Pale Ale(IPA), and boundaries blur, though IPAs are stronger and more assertively hopped. The style is also close to amber ale, though ambers are darker and maltier due to use of crystal malts.'
    )

    Beer(
        name='India Pale Ale, Vic Secret',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/02/CMVS.jpg',
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
        name='Calypso G901',
        image='https://honestbrew.co.uk/wp-content/uploads/2015/11/Siren-Calypsov2.jpg',
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
        image='https://honestbrew.co.uk/wp-content/uploads/2018/02/Magic-Rock-Salty-Kiss-Can-330ml.jpg',
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
        image='https://honestbrew.co.uk/wp-content/uploads/2018/04/North-Brewing-Co.-Full-Fathom-5-Coffee-Coconut-Porter-6.5_-Can-330ml.jpg',
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
        name='Tremendous Ideas',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/05/Cloudwater-Other-Half-Tremendous-Ideas-DIPA-8_-Can-440ml.jpg',
        brewery=cloudwater,
        style=dipa,
        hops='Pacific Jade, Ella',
        region='UK',
        abv=8.8,
        price=7.99,
        tasting_notes='Tremendous Ideas was the first collaboration brewed in Manchester with Other Half back in 2017, and they\'ve revived it just in time for the second edition of Other Half\'s Green City festival. Combining a huge, pillowy body with vibrant citrus and tropical fruit flavours from a selection of punchy, modern hop varietals, this is a smooth and decadent DIPA.',
        user=seanyg
    )

    Beer(
        name='Undercurrent',
        image='https://honestbrew.co.uk/wp-content/uploads/2015/11/Siren-Undercurrentv2.jpg',
        brewery=siren,
        style=pale,
        hops='Cascade, Simcoe, Columbus, Bravo',
        region='UK',
        abv=4.5,
        price=1.89,
        tasting_notes='If you’re after brews of a somewhat spicy, nutty nature, Undercurrent will take your senses for a spin with aromas of both leading into citrus floral hops. This dark golden pale goes down real smooth with flavours matching the aromas while adding a bit of lychee and passionfruit.',
        user=seanyg
    )

    Beer(
        name='Heathen',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/01/Northern-Monk-Heathen-IPA-Can-440ml.jpg',
        brewery=northern_monks,
        style=ipa,
        region='UK',
        abv=7.2,
        price=3.99,
        tasting_notes='A simple malt base of Pale malt to take the beer up to 7.2%, then small kettle additions of US and UK hops for a soft fruity bitterness. Come dry hopping time Northern Monk go for it. 16kg of Citra spread over three additions are layered into the beer for the ultimate juicy, resinous taste experience and an aroma of tropical fruit you can smell across the room.',
        user=seanyg
    )

    Beer(
        name='Atlantean',
        image='https://honestbrew.co.uk/wp-content/uploads/2017/09/Whitehag-New-England.jpg',
        brewery=white_hag,
        style=neipa,
        region='UK',
        abv=5.4,
        price=3.19,
        tasting_notes='New England-style IPA. Atlantean is inspired by mythological sea journeys which took curious voyagers beyond the ninth wave in search of the magical otherworlds and the secret treasures they held. For this IPA white Hag’s inspiration has travelled back across the cloudy foam of the Atlantic from New England.',
        user=seanyg
    )

    Beer(
        name='Partizan - Porter',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/04/NEW-LABEL-Partizan-Porter-Bottle-330ml.jpg',
        brewery=partizan,
        style=porter,
        region='UK',
        abv=5.4,
        price=2.89,
        tasting_notes='A traditional Porter that boasts caramel tones as opposed to typically roasty stout flavours. Ruby red in colour and full-bodied with a moderate bitterness, Partizan are strong supporters of traditional with a fresh and contemporary twist.',
        user=seanyg
    )

    Beer(
        name='CannonBall',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/01/Magic-Rock-Cannonball-Can-330ml.jpg',
        brewery=magic_rock,
        style=ipa,
        region='UK',
        abv=7.2,
        price=2.89,
        tasting_notes='One punchy punchbowl full of fruity goodness, Cannonball exudes a bounty of tropical and resinous hops finishing with a puckering bitter bite that’ll leave you wondering where your mouth’s gone.',
        user=seanyg
    )


    Beer(
        name='Inhaler',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/02/Magic-Rock-Inhaler-Can-330ml.jpg',
        brewery=magic_rock,
        style=pale,
        region='UK',
        abv=4.5,
        price=1.99,
        tasting_notes='Things move quickly in the beer world and Magic Rock’s latest pale ale/IPA hybrid is designed to showcase some of the newer hop varieties which work so well in modern hop forward beers. Pale malt, a little wheat, a little crystal malt, low bitterness and then six different hops! Super fruity, super ripe, super juicy and super drinkable. Breathe it in!',
        user=seanyg
    )

    Beer(
        name='Shelterstone',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/07/Buxton-Shelterstone-IPA-5.6_-Can-330ml.jpg',
        brewery=buxton,
        style=ipa,
        region='UK',
        abv=5.6,
        price=2.89,
        tasting_notes='Kick back and take sanctuary under the protection of the Shelterstone. A refreshing, unfined, vegan nectar from Buxton, best drunk cold in the great outdoors.',
        user=seanyg
    )

    Beer(
        name='Kellerbier',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/01/Buxton-Kellerbier-4.5_-Can-440ml.jpg',
        brewery=buxton,
        style=lager,
        region='UK',
        abv=4.5,
        price=3.89,
        tasting_notes='Kellerbier is Buxton’s edition of the timeless German style of beer. The term literally translates as ‘cellar beer’, referring to its cool lagering temperatures. Its recipe likely dates to the Middle Ages, and Buxton’s version was aptly brewed to celebrate the opening of their Taphouse Cellar Bar.',
        user=seanyg
    )

    Beer(
        name='Axe Edge',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/04/Buxton-Axe-Edge-IPA-6.8_-Can-440ml.jpg',
        brewery=buxton,
        style=ipa,
        region='UK',
        abv=6.8,
        price=4.69,
        tasting_notes='A full-flavoured IPA. Light amber with flavours of mandarin orange, tropical fruits and a warming, dry finish. Buxton have dedicated themselves to creating some of the best beers in Europe and this is one of the beers that is definitely helping them achieve their goal.',
        user=seanyg
    )

    Beer(
        name='High Wire Grapefruit',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/02/Magic-Rock-High-Wire-Grapefruit-Can-330ml.jpg',
        brewery=magic_rock,
        style=pale,
        region='UK',
        abv=5.5,
        price=2.49,
        tasting_notes='An explosion of mango, lychee and lip-smacking grapefruit flavours, Magic Rock’s punchy grapefruit version of their tribute to the American West Coast will knock your socks off. Walk a tightrope of taste with this dynamic brew from the Huddersfield based brewery.',
        user=seanyg
    )

    Beer(
        name='The Puca Berries, Hibiscus & Ginger',
        image='https://honestbrew.co.uk/wp-content/uploads/2016/11/Whitehag-The-Puca.jpg',
        brewery=white_hag,
        style=sour,
        region='UK',
        abv=3.5,
        price=2.89,
        tasting_notes='Sour, juicy, spicy, floral – The Puca is looking especially pretty in pink cans, it’s tasting excellent too. Wrap your taste buds around White Hag’s dry-hopped Berliner Weisse.',
        user=seanyg
    )

    Beer(
        name='Pinata Mango & Guava',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/04/North-Brewing-Co.-Pinata-Session-IPA-4.5_-Can-330ml.jpg',
        brewery=north_brewing_co,
        style=pale,
        region='UK',
        abv=4.5,
        price=2.89,
        tasting_notes='A brew packed with sweet fruity treats, North Brewing Co bring you Pinata tropical pale ale. You’ll find four tropical fruits paired with plenty of new world hops. Mandarin and grapefruit peel are combined in the kettle, alongside additions of guava and mango. A party and drink all night long 4.5% ABV.',
        user=seanyg
    )

    Beer(
        name='Sputnik',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/07/North-Brewing-Co-Sputnik-American-Pale-Ale-5_-Can-330ml.jpg',
        brewery=north_brewing_co,
        style=apa,
        region='UK',
        abv=5,
        price=3.19,
        tasting_notes='Sputnik is an out of this world dry hopped Pale Ale. Sessionable at 5%, it presents a light body and colour. The blend of American hops give this beer a citrus and pine aroma, while tropical and stone fruit also put in a hoppy appearance.',
        user=seanyg
    )

    Beer(
        name='Special Pale Ale',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/02/Buxton-Spa-Special-Pale-Ale-4.1_-Bottle-330ml.jpg',
        brewery=buxton,
        style=pale,
        region='UK',
        abv=4.1,
        price=3.19,
        tasting_notes='In 78 AD the Roman Empire reached and settled Buxton. They enjoyed the warm Spa waters that rise in the town. This beer celebrates the Spa of Buxton. A light, refreshing, hoppy pale ale. It has a lovely citrus aroma, with juicy fruit flavours in the mouth. Medium bitterness.',
        user=seanyg
    )

    Beer(
        name='AXE^X',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/05/Buxton-Axe-X-NEIPA-6.5_-can-440ml.jpg',
        brewery=buxton,
        style=ipa,
        region='UK',
        abv=6.8,
        price=5.49,
        tasting_notes='Do your beer maths. This is AXE raised to the power of X, where X is dry hopping and increased by 200%. For enhanced mouthfeel and character, 20% of oats are added to the grist, while IBU’s are significantly reduced. The sums say, drink this NEIPA.',
        user=seanyg
    )

    Beer(
        name='Millionaire',
        image='https://honestbrew.co.uk/wp-content/uploads/Wild-Millionare.jpg',
        brewery=wild_beer_co,
        style=stout,
        region='UK',
        hops='Magnum',
        abv=4.7,
        price=2.25,
        tasting_notes='Sometimes a drink can make you feel so decadent it’s like you’re a millionaire; this beer wraps you in a velvety cocoon, dresses you in a smart suit and takes you out for a special night on the tiles... Sweet and salty collide in this rich, balanced and smooth dessert stout.',
        user=seanyg
    )

    Beer(
        name='Existential Thanks DDH',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/05/Cloudwater-Existential-Thanks-DDH-IPA-6_-Can-440ml.jpg',
        brewery=cloudwater,
        style=ipa,
        region='UK',
        abv=6,
        price=6.79,
        tasting_notes='This DDH IPA is a single-hop showcase of the latest crop of famous US hop varietal Simcoe, which has a flavour profile that is likely to confound expectations. Instead of the punchy resinous notes and pine usually associated with Simcoe, this batch packs soft and juicy fruit flavours, making it an ideal fit for a modern, smooth and full-bodied DDH IPA.',
        user=seanyg
    )

    Beer(
        name='West Coast Pale',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/06/Cloudwater-West-Coast-Pale-5_-Can-440ml.jpg',
        brewery=cloudwater,
        style=pale,
        region='UK',
        abv=5,
        price=4.49,
        tasting_notes='Inspired by the classic, easy-drinking Pale Ales of America’s West Coast, this is a style where balance between punchy, aromatic hop notes and solid drinkability is key. A clean, dry, lightly resinous and bitter finish sets this beer apart from its hazy counterparts.',
        user=seanyg
    )

    Beer(
        name='IPA',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/03/Cloudwater-A-Soft-Juicy-IPA-6.5_-Can-440ml.jpg',
        brewery=cloudwater,
        style=ipa,
        region='UK',
        abv=6.5,
        price=5.29,
        tasting_notes='Juicy, soft, and full of ripe tropical fruit flavours from a blend of hops and aromatic yeast, this IPA is Cloudwater’s modern take on a classic style. Showcasing hop flavours and yeast esters against a big body from high protein malts, to replicate the mouthfeel of tropical fruit, this beer finishes with a low bitterness to let the hop aromas and flavours linger on your palate',
        user=seanyg
    )

    Beer(
        name='Culinary Concepts Yuzu',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/05/Northern-Monk-Patrons-Project-10.06-Finback-Culinary-Concepts-Yuzu-IPA-6.4_-Can-440ml.jpg',
        brewery=northern_monks,
        style=ipa,
        region='UK',
        abv=6.4,
        price=6.29,
        tasting_notes='Patrons Project 10.06. To complement the sharp, zesty nature of the Yuzu fruit we wanted a base which was fluffy and rounded but still light enough to contribute to a refreshing drink. We went with pilsner malt and a large portion of wheat, backing them up with small portions of flaked wheat and oats for the base. The idea behind this was to put together a malt profile reminiscent of the Wit-style but that still had all the soft character that would be expected of a Northern Monk – Finback IPA. We fermented with our house IPA strain and added yuzu juice at the back end. Finally, we dry- hopped with Citra and Mosaic, generously but not high enough to mask the unique flavour of yuzu.',
        user=seanyg
    )

    Beer(
        name='Faith Pale Ale',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/01/Northern-Monk-Faith-Can-440ml.jpg',
        brewery=northern_monks,
        style=pale,
        region='UK',
        abv=5.4,
        price=2.99,
        tasting_notes='A Modern Pale Ale packed with soft fruit flavours. Smooth, tropical and juicy. You’ve got to have Faith.',
        user=seanyg
    )

    Beer(
        name='Farewell Tangerina Tangerine',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/03/Northern-Monk-Patron_s-Project-15.03-Farewell-Tangerina-Tangerine-Sour-5.7_-Can-440ml.jpg',
        brewery=northern_monks,
        style=sour,
        region='UK',
        abv=5.7,
        price=5.69,
        tasting_notes='For the second in Northern Monk’s series of Patron collaborations with Lucy Ketchin, they showcase the fruit Lucy herself was most eager for them to work with – tangerine. Pilsner malt, flaked oats, kettle-soured wort and El Dorado hopped two ways, combine with lactose, vanilla, and lots and lots of pureed tangerines.',
        user=seanyg
    )

    Beer(
        name='Mosaic IPA',
        image='https://honestbrew.co.uk/wp-content/uploads/2017/03/kernel-Mosaic-IPA.jpg',
        brewery=kernel,
        style=ipa,
        region='UK',
        abv=6.9,
        price=3.39,
        tasting_notes='This beer tastes too good for words',
        user=seanyg
    )

    Beer(
        name='Fantasma GF',
        image='https://honestbrew.co.uk/wp-content/uploads/2018/02/Magic-Rock-Fantasma-Gluten-Free-IPA-6.5_-Can-330ml.jpg',
        brewery=magic_rock,
        style=ipa,
        region='UK',
        abv=6.5,
        price=2.79,
        tasting_notes='What’s that? Gluten-free, you say? Magic Rock have brought every beer-loving celiac’s dream to life with this here corker of an IPA. Hazy, dank and tropically fruity with a restrained bitterness and great drinkability.',
        user=seanyg
    )

    Beer(
        name='BA Turkish Imperial Stout',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/05/Siren-Project-Barista-Bourbon-Turkish-Barrel-Aged-Imperial-Coffee-Stout-11.5_-Bottle-330ml.jpg',
        brewery=siren,
        style=imperial_stout,
        region='UK',
        abv=11.5,
        price=6.49,
        tasting_notes='The original Turkish brew was inspired by Turkey’s robust coffee and included not only vanilla, orange zest, nutmeg, figs, cacao and muscavado but also 45kg of Thai coffee. Before barrel ageing, we added more nutmeg, summer orange zest and coffee. After 18 months sat in second use barrels we’re adding Ecuadorian Gonzalo Gaona coffee in the form of a rich espresso, brewed by Redemption Roasters, to maintain big coffee flavours. This is a rich, unctuous and hedonistic coffee beer with a lot going on.',
        user=seanyg
    )

    Beer(
        name='YU LU',
        image='https://honestbrew.co.uk/wp-content/uploads/2017/03/Siren-YULU-1.jpg',
        brewery=siren,
        style=pale,
        region='UK',
        abv=3.8,
        price=2.49,
        tasting_notes='Yu Lu is an intricate beer with layers of flavour that remain distinctive, yet work in perfect harmony. The name alludes to the mystical history of the humble tea leaf, which delivers subtle bergamot orange and lemon notes here, accentuated by the addition of lemon zest. The delicate hop high notes will leave your taste buds sparkling.',
        user=seanyg
    )

    Beer(
        name='Double Double DDH Coffee',
        image='https://honestbrew.co.uk/wp-content/uploads/2019/05/Siren-Double-Double-DDH-Coffee-Pale-Ale-Bottle-330ml.jpg',
        brewery=siren,
        style=pale,
        region='UK',
        abv=6,
        price=3.69,
        tasting_notes='Our take on the Double-Double is double the coffee and double the dry-hopping! We used Mosaic for a deep berry character, with Amarillo and Ekuanot bolstering the strong hop character. A higher than normal mashing temperature gives a residual sweetness, helped with allergen-free hazelnut extract and some vanilla. The Peruvian Huabal coffee comes via Pharmacie Coffee Roasters, and provides notes of baked apple and orange marmalade with a sweet and full toffee body.',
        user=seanyg
    )

    Beer(
        name='Jet Black Heart',
        image='https://www.ocado.com/productImages/412/412268011_1_640x640.jpg?identifier=03d76792b5521960fd230d3c969ce3b0',
        brewery=brewdog,
        style=stout,
        hops='Hallertauer Taurus',
        region='UK',
        editors_choice=True,
        abv=4.7,
        price=2.00,
        tasting_notes='This stout is black as pitch and smooth as hell. Jet Black Heart is a milk stout with an ebony core. Loaded with oatmeal and primed for a velvet smooth delivery. Cacao, roasted coffee and berry fruits linger in its deepest darkest depths. Full-bodied, rich and decadent to the core.',
        user=seanyg
    )

    Beer(
        name='AW-18 DDH Pale v1',
        image='https://cdn.shopify.com/s/files/1/0940/3274/products/AW18-Brewed-All-Season-DDH-Pale_1024x1024.jpg?v=1540912092',
        brewery=cloudwater,
        style=pale,
        hops='There are some but none specified online',
        region='UK',
        editors_choice=True,
        abv=5.5,
        price=6.60,
        tasting_notes='This is a one-off brew to celebrate Indy Man Beer Con 2018. "DDH" means this Pale has been double dry hopped, using twice the amount of hops as our standard Pale. Expect big citrus and tropical fruit flavours, and a firm, smooth body combined with crushability.',
        user=seanyg
    )


    Beer(
        name='Hazey Daze',
        image='https://d3qgkyg87t4mjz.cloudfront.net/media/catalogue/product/modified/LBF_Hazy.png',
        brewery=london_beer_factory,
        style=ipa,
        hops='Citra, Mosaic, Vic Secret',
        region='UK',
        editors_choice=True,
        abv=4.6,
        price=1.80,
        tasting_notes='A juicy, crushable, session IPA with big tropical notes. Using fully flavoured hazy New England yeast this leaves a citrus hum on the tongue and lashings of pineapple on the nose.',
        user=seanyg
    )

    Beer(
        name='Eternal',
        image='https://cdn.shopify.com/s/files/1/0019/7197/8349/products/b95045113dc180cc69d37d141bddc3166a83d982_1000x1000.jpg?v=1552650063',
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
        name='Bibble',
        image='https://www.beerhawk.co.uk/media/catalog/product/w/i/wild_beer_bibble.png',
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
