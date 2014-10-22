# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FreelancerscraperItem(Item):
    # define the fields for your item here like:
    parent_categ_name = Field()
    categ_name_count = Field()
    pass
