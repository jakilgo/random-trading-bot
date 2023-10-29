import csv
import random

def get_tickers():
    tickers = []
    with open('constituents.csv', newline='') as sp_tickers:
        f = csv.reader(sp_tickers, delimiter=' ', quotechar='|')
        tickers = [row[0].split(',')[0] for row in f]
        tickers.pop(0)

    return tickers

def buy_or_sell():
    return random.choice(['buy', 'sell'])

def main():
    tickers = get_tickers()
    print(buy_or_sell(), random.choice(tickers))



if __name__ == '__main__':
    main()