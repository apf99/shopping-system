import pandas as pd
from pdf_code import print_receipt

df = pd.read_csv('articles.csv')

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df['id'] == int(self.article_id), 'name'].squeeze()
        self.price = df.loc[df['id'] == int(self.article_id), 'price'].squeeze()
        self.stock = df.loc[df['id'] == int(self.article_id), 'in stock'].squeeze()

    def available(self):
        return self.stock > 0

    def purchase(self):
        df.loc[df['id'] == int(self.article_id), 'in stock'] -= 1
        self.stock = df.loc[df['id'] == int(self.article_id), 'in stock'].squeeze()
        df.to_csv('articles.csv', index=False)

class Receipt:
    def __init__(self, article):
        self.article = article

    def print(self):
        print_receipt(article.name, article.price)


print(df)

article_ID = input('Enter the ID of the article: ')
article = Article(article_ID)
if article.available():
    article.purchase()
    receipt = Receipt(article)
    receipt.print()
else:
    print('Item is not available')

