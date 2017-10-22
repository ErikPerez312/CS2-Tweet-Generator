import re
# import requests

# DIFFBOT_API_URL = 'https://erowid.org/culture/characters/watts_alan/watts_alan_article1.shtml'
# DIFFBOT_DEV_TOKEN = '3fb8e1cfa2d8f1b6110dd509cf388d0c'

# def get_article(article_url):
#     # set request params for API request
#     params = { 'token': DIFFBOT_DEV_TOKEN,
#                'url': article_url,
#                'discussion': 'false' }

#     res = requests.get(DIFFBOT_API_URL, params) # hit the Diffbot API
#     res_obj = res.json()['objects'][0]          # parse the response object

#     return res_obj['text']                      # pull out the text

# if __name__ == '__main__':
#     import sys
#     urls_file = open(sys.argv[1])
#     output_file = open('corpus.txt', 'w')

#     corpus = ''

#     for line in urls_file:
#         url = line.strip() # remove leading/trailing whitespace
#         article = get_article(url)
#         corpus += article

#     output_file.write(corpus)
#     print('Corpus saved to {}'.format(output_file.name))


sentence = "There's more than 27 pots"
string_no_numbers = re.sub("\d+", " ", sentence)

print(string_no_numbers)