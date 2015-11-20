# Scrapy settings for data_gov_ph project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'data_gov_ph'

SPIDER_MODULES = ['data_gov_ph.spiders']
NEWSPIDER_MODULE = 'data_gov_ph.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'data_gov_ph (+http://open-contracting.github.io)'

# Bird's default settings
TELNETCONSOLE_ENABLED = False
WEBSERVICE_ENABLED = False
CONCURRENT_REQUESTS = 5
DOWNLOAD_DELAY = 0.25
