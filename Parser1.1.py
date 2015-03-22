# encoding: utf-8
import sys
import errno
import urllib2
import json
from bs4 import BeautifulSoup
class Parser:
    user_agent = (
        "Mozilla/5.0 "
        "(X11; Ubuntu; Linux x86_64; rv:30.0) "
        "Gecko/20100101 Firefox/30.0"
    )
    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.num_of_file = 1
        #self.file = "quotes_json" + str(self.num_of_file)
        #self.id_of_file = open(self.file, "w")
    def get_url(self, page_number):
        return "http://bash.im/index/%s" % page_number
    def fetch_page(self, page_number):
        req = urllib2.Request(url=self.get_url(page_number), headers={"User-Agent": self.user_agent})
        f = urllib2.urlopen(req)
        return f.read()
    def parse_all_pages(self):
        for page_number in xrange(self.start_page, self.end_page + 1):
            self.parse_quotes(page_number)
    def parse_quotes(self, page_number):
        print page_number
        html = self.fetch_page(page_number)
        soup = BeautifulSoup(html)
        quote_divs = soup.find_all("div", class_="quote")
        for quote_div in quote_divs:
            quote = {}
            text_div = quote_div.find("div", class_="text")
            if not text_div:
                continue
            quote["text"] = "\n".join(filter(lambda x: isinstance(x,unicode), text_div.contents))
            quote["id"] = self.num_of_file
            self.write_quote(quote)
    def write_quote(self, quote):
        self.id_of_file = open(str(self.num_of_file), "w")
        json.dump(quote, self.id_of_file, indent = 2)
        self.num_of_file += 1


arguments = sys.argv
if (
    len(arguments) == 3
    and arguments[1].isdigit()
    and arguments[2].isdigit()
):
    start_page = int(arguments[1])
    end_page = int(arguments[2])
    if start_page > 0 and end_page >= start_page:
        p = Parser(start_page, end_page)
        p.parse_all_pages()
    else:
        sys.stderr.write("Please check the page numbers\n")
        sys.exit(errno.EINVAL)
else:
    sys.stderr.write("Invalid arguments\n")
    sys.exit(errno.EINVAL)