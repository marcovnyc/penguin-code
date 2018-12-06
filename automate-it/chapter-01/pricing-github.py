from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
#plans = tree.xpath('\\"pricing-card/text()')
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("Pricing:", pricing)
