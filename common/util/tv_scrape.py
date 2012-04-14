import urllib
from lxml.html import parse
import time

css_selector  = "html body.us div#mantle_skin div div._bento"
css_selector += " div._mpu_grid div._col_a div._col_a2 div"
css_selector += " div.m ul.videos li.video div._image_container "
css_selector += "div._watch_button div.view_options"
css_selector += " a.option div.network"
print(css_selector)

doc =\
    parse(urllib.urlopen("http://www.tv.com/shows/mad-men/watch/?order=-1&page=1&q=&ajax=1&episode_type_range=1-2&vdmid_free=on&vdmid_paid=on&vdmid_5=on&vdmid_6=on&vdmid_7=on&vdmid_10=on&vdmid_11=on&vdmid_12=on&vdmid_13=on&season=")).getroot()
links = doc.cssselect(css_selector)
for link in links:
    print '%s: %s' % (link.text_content(), link.get('href'))
