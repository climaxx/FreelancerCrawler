# Freelancer.com spider
# (c) 2014 Brunomag Concept Ltd
# www.brunomag.ro

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from freelancerscraper.items import FreelancerscraperItem
from tabulate import tabulate
import operator
import re
class FreelancerSpider(BaseSpider):
	name="freelancer"
	start_urls = [ "https://www.freelancer.com/job/"  ]

	def parse(self, response):
		htmlresponseinit = HtmlXPathSelector(text=response.body).select('//div[@id="browseJobs"]')
		i_range = range(13)
		for sel in htmlresponseinit:
			items = []
			for i in i_range:

			        item = FreelancerscraperItem()
				id_a_link = "jobCat" + str(i) + "_heading"
			        id_ul_link = "jobCat" + str(i)
			        parent_categ_name = sel.select('p/strong/a[@id="' + id_a_link + '"]/text()').extract()
				item['parent_categ_name'] = parent_categ_name
			        categ_and_count_string =	(sel.select('ul[@id="' + id_ul_link  + '"]/li/a/text()').extract())

			        result = {}
				for categ_and_count in categ_and_count_string:
			           #   Electronics (1234)
				   categ = categ_and_count.split("(")[0].strip()
				   count = re.findall(r'\d+', categ_and_count)[0]
				   result[categ] = int(count)
				sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse = True)
				item['categ_name_count'] = sorted_result
			        items.append(item)
                for item in items:
                        print "--------------*******------------------------------*******----------------"
                        print tabulate(item['categ_name_count'], ["CATEGORY: " + "".join(item['parent_categ_name']), "Count"], tablefmt="grid")
                                
		yield None


