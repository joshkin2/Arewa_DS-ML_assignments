url = 'https://en.wikipedia.org/wiki/Outline_of_machine_learning'
import requests
text = requests.get(url).content.decode('utf-8')
print(text[:1000])

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    script = False
    res = ""
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ["script","style"]:
            self.script = True
    def handle_endtag(self, tag):
        if tag.lower() in ["script","style"]:
            self.script = False
    def handle_data(self, data):
        if str.strip(data)=="" or self.script:
            return
        self.res += ' '+data.replace('[ edit ]','')
parser = MyHTMLParser()
parser.feed(text)
text = parser.res
print(text[:1000])

import sys
!{sys.executable} -m pip install nlp_rake

import nlp_rake
extractor = nlp_rake.Rake(max_words=2,min_freq=3,min_chars=5)
res = extractor.apply(text)
res

import matplotlib.pyplot as plt
def plot(pair_list):
    k,v = zip(*pair_list)
    plt.bar(range(len(k)),v)
    plt.xticks(range(len(k)),k,rotation='vertical')
    plt.show()
plot(res)

!{sys.executable} -m pip install wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud(background_color='white',width=800,height=600)
plt.figure(figsize=(15,7))
plt.imshow(wc.generate_from_frequencies({ k:v for k,v in res }))

plt.figure(figsize=(15,7))
plt.imshow(wc.generate(text))

wc.generate(text).to_file('images/ds_wordcloud.png')
