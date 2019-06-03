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
        info='Our work at Cloudwater starts with the intention of helping you relax and unwind with the finest quality modern beers we can make. We employ all the passion, skills, dreams, and experience of our team, and harness up-to-the-minute brewing science and techniques, out of respect for the ingredients our suppliers work hard to grow and process, and out of our gratitude for your support and trust. // We’re devoted to offering you value through bold, precise flavours, bottomless drinkability, the lowest possible off-flavour presentation, and consistency from one beer to the next. // Founded in 2014, we brewed our first beers on February 14th 2015. In our short history, we have made hundreds of different beers, in styles old and new, classical and imagined, evolving our brewing skills, honing our sensory evaluation techniques, and trialling fermentation and process changes in pursuit of ever higher-quality beer. // Outside our range of evolving and one-off seasonal beers, we collaborate with some of the world’s best breweries, and we also produce modern takes on classic styles. Though modern beer is our focus, we honour those that trail-blaze around us, and that pioneered before us by a constant focus on quality and innovation.',
        user=seanyg)

    buxton = Brewery(
        name='Buxton',
        logo='https://i0.wp.com/www.thedrinkers.co.uk/wp-content/uploads/2017/12/buxton.png?fit=1055%2C1200&ssl=1',
        image='https://static1.squarespace.com/static/59a862328fd4d227956d1f66/t/5a5e736ce2c4834114a25f23/1516140513892/DSC06411-01.jpeg',
        founded='2017',
        area='Buxton',
        info='Buxton brwery, ',
        user=seanyg
)

    northern_monks = Brewery(
        name='Northern Monks',
        logo='https://static1.squarespace.com/static/56e53b52859fd07e03b6c49f/t/5ac46e2d758d46be7f08e0d3/1522822711814/Screen+Shot+2018-04-04+at+06.47.23.png',
        image='https://www.leeds-art.ac.uk/media/563129/northern-monk-header.jpg',
        founded='2013',
        area='Leeds',
        info='INSPIRED BY OUR NORTHERN SURROUNDINGS AND THE HISTORY OF MONASTIC BREWING PRACTICED ACROSS THE REGION FOR THOUSANDS OF YEARS, WE COMMIT OURSELVES TO CREATING THE HIGHEST QUALITY BEERS, COMBINING THE BEST OF TRADITIONAL MONASTIC BREWING VALUES WITH A PROGRESSIVE APPROACH TO INGREDIENTS AND TECHNIQUES. COMMUNITY AND COLLABORATION ARE AT THE CORE OF OUR BUSINESS. WE FOCUS ON WORKING WITH ANYONE WHO SHARES OUR PASSION, AND OUR VALUES. WE REGULARLY COLLABORATE WITH NATIONAL AND INTERNATIONAL BREWERIES, BUSINESSES AND CHARITIES TO HELP STRENGTHEN THE NORTH FOR POSITIVE CHANGE, AND TO CONTINUALLY DIVERSIFY OUR OWN OFFERING. ONE OF THE WAYS WE DO THIS IS THROUGH OUR PATRONS PROJECTS.',
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

    kernel = Brewery(
        name='Kernel',
        logo='https://www.beyondbeer.de/media/image/39/58/d3/the_kernel-logo-beyond-beer1.png',
        image='https://static1.squarespace.com/static/5055e59ce4b02b42cb30023c/t/5a48f4a50d92977993059408/1514730674825/56.jpg?format=1500w',
        founded='2010',
        area='London',
        info='The brewery springs from the need to have more good beer. Beer deserving of a certain attention. Beer that forces you to confront and consider what you are drinking. Upfront hops, lingering bitternesses, warming alcohols, bodies of malt. Lengths and depths of flavour. We make Pale Ales, India Pale Ales and old school London Porters and Stouts towards these ends. Bottled alive, to give them time to grow.',
        user=seanyg
    )

    london_beer_factory = Brewery(
        name='London Beer Factory',
        logo='https://static.designmynight.com/uploads/2017/05/londonbeerfactory-1-optimised.jpg',
        image='https://imbibe.com/media/31294/beer-factory-crowdfunding.jpg',
        founded='2014',
        area='London',
        info='The London Beer Factory is a craft brewery founded in early 2014 by brothers Ed and Sim Cotton. // From day one we have been committed to producing beer with character; beer with unique flavours and engaging aromas; beer brimming with personality and distinctive qualities.// Distilling these principles into every single brew, we have developed a broad range of unfiltered, unpasteurised beer, incorporating a wide array of hops and malts from around the world. //Our Core Range includes five beers, all of which are available in keg, can and bottle format. //Our Pilot Range enables us to produce a new beer every month, available in a variety of formats, depending on the style of beer. // We hope you enjoy them all as much as we do and if you have any more questions about our beers or our brewery then please do get in touch. We’d love to hear from you.',
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

    magic_rock = Brewery(
        name='Magic Rock',
        logo='https://www.magicrockbrewing.com/cms/wp-content/themes/magicrock/images/logo@2x.png',
        image='https://www.magicrockbrewing.com/cms/wp-content/uploads/2015/10/brewery-hire-web.jpg',
        founded='2011',
        area='Huddersfield',
        info='Inspired by local brewing traditions and the vibrant US craft beer scene, Magic Rock Brewing is the culmination of a lifelong passion for beer. Richard Burhouse (aided by head brewer Stuart Ross) started the brewery in 2011 in an old out-building of the family business (an importer of crystals and natural gifts) in Huddersfield, West Yorkshire. // Alongside a distinctive core range we produce an ever changing line up of idiosyncratic beers with an innovative quality driven approach. Our Same but Different beers are packed with intense yet approachable flavours which will challenge and inspire, but above all remain balanced and drinkable. // In line with a desire to reflect US beer culture and enhance the UK beer scene, local designer Rich Norgate was commissioned from day one to create a modern and contemporary look for our brand which would resonate with a new wave of beer drinkers bored by the traditional beer landscape. // Initial reaction to the beers exceeded expectations and a fantastic first six months culminated in the brewery being voted 2nd best new brewery in the world 2012 (and 5 times a top 100 world brewer since) on the independent ratings site RateBeer.com. To meet demand, capacity was increased twice in the first year with additional fermenting vessels added in October 2011 and January 2012. // In 2015 the brewery moved to a new facility in Birkby, Huddersfield less than 10 minutes’ walk from the town centre, featuring a 4,000 sqft Tap Room and automated canning facility. The move also facilitated an expansion of brewing operations with the installation of a 50hl brewing system and additional fermenters. In the intervening years production has tripled and currently stands at around 15,500hl pa (2.7million pints).',
        user=seanyg
    )

    north_brewing_co = Brewery(
        name='North Brewing Co.',
        logo='https://www.northbrewing.com/wp-content/uploads/2016/12/North-Brewing-Co-Logo-bk-2.png',
        image='https://cdn-b.william-reed.com/var/wrbm_gb_hospitality/storage/images/7/7/7/5/2595777-1-eng-GB/North-Brewing-Co-growing-across-the-globe_wrbm_large.jpg',
        founded='2015',
        area='Leeds',
        info='North Brewing Co was founded in 2015 by John Gyngell and Christian Townsley, the pioneers behind legendary Leeds beer venue North Bar, which opened in 1997. Known as “the first craft beer bar in Britain”, North Bar influenced a new wave of modern beer bars and breweries across the country, including their own. // In 2015 they turned their 10-year dream of making their own beer into a reality by opening a 15bbl brewery, featuring a 200-person capacity tap room, just half a mile from their original flagship North Bar in Leeds. // The core range and seasonal specials epitomise what they look for in beer: big juicy flavours with tonnes of hops; fun, playful and interesting flavour combinations; classics that demonstrate an uncompromising approach to quality. // The brewery has worked with some of the best breweries in the world, collaborating with the likes of Lervig Øl (Norway), Dry & Bitter (Denmark), Basqueland Brewing Project (ESP), Het Uiltje (NL), De Molen (NL), Other Half and Finback (USA), Magic Rock, BrewDog, Verdant, Thornbridge, Track Brewing and Wylam Brewery (UK). // In just two years North Brewing Company has received both national and international recognition.',
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

    lambic = Style(
        name='Lambic',
        info='Lambic (\'lɒmbiːk or \'læmbɪk) is a type of beer brewed in the Pajottenland region of Belgium southwest of Brussels and in Brussels itself at the Cantillon Brewery. Lambic beers include gueuze and kriek lambic. Lambic differs from most other beers in that it is fermented through exposure to wild yeasts and bacteria native to the Zenne valley, as opposed to exposure to carefully cultivated strains of brewer\'s yeast. This process gives the beer its distinctive flavour: dry, vinous, and cidery, usually with a sour aftertaste.'
    )

    table_beer = Style(
        name='Table Beer',
        info='Table beer (also known as small ale or table beer) is a lager or ale that contains a lower amount of alcohol by volume (ABV) than other beers, typically between 0.5% to 2.8%. Sometimes unfiltered and porridge-like, it was a favored drink in Medieval Europe and colonial North America against more expensive beer with higher alcohol. Small beer was also produced in households for consumption by children and servants.'
    )

    neipa = Style(
        name='NE IPA',
        info='New England India pale ales are a style of IPA invented in Vermont in the early 2010s. They are characterized by juicy, citrus, and floral flavours, with a more subtle and less piney hop taste than typical IPAs. They also have a smooth consistency or mouthfeel, and a hazy appearance. These characteristics are achieved using a combination of brewing techniques, including the use of particular strains of yeast, the timing of adding the hops, and adjusting the chemistry of the water. The style has become popular among New England brewers. New England IPAs need not be brewed in New England. It was officially recognized as a separate beer style, the Juicy or Hazy India Pale Ale, by the Brewers Association in 2018.'
    )

    belgian = Style(
        name='Belgian',
        info='Beer in Belgium varies from pale lager to amber ales, lambic beers, Flemish red ales, sour brown ales, strong ales and stouts. In 2016, there were approximately 224 active breweries in Belgium, including international companies, such as AB InBev, and traditional breweries including Trappist monasteries. On average, Belgians drink 84 liters of beer each year, down from around 200 each year in 1900. Most beers are bought or served in bottles, rather than cans, and almost every beer has its own branded, sometimes uniquely shaped, glass. In 2016, UNESCO inscribed Belgian beer culture on their list of the intangible cultural heritage of humanity.'
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
        name='Eternal',
        image='https://cdn.shopify.com/s/files/1/0019/7197/8349/products/b95045113dc180cc69d37d141bddc3166a83d982_1000x1000.jpg?v=1552650063',
        brewery=northern_monks,
        style=ipa,
        hops='There are some but none specified online',
        region='UK',
        editors_choice=True,
        abv=4.1,
        price=2.39,
        tasting_notes='A product brewed for almost 7,000 years, a quest for perfection that never ends. Citrusy, light and refreshing. To Eternity.',
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
