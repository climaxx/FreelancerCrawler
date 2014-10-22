# Scrapy settings for freelancerscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'freelancerscraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['freelancerscraper.spiders']
NEWSPIDER_MODULE = 'freelancerscraper.spiders'
DEFAULT_ITEM_CLASS = 'freelancerscraper.items.FreelancerscraperItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

