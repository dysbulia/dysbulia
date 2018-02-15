from coinmarketcap import Market
import time
import pandas as pd

coinmarketcap = Market()
print(coinmarketcap.ticker("bitcoin"))

coins = coinmarketcap.ticker()


def scrape():

    for i in range(96):
        #this creates a dataframe with the top 100 coins
        coinArray = pd.DataFrame([pd.Series(coins[i]) for i in range(100)]).set_index('id')

        #timestamps and stores the csv file
        location = 'Data/'+str(time.time())+'.csv'
        coinArray.to_csv(location)

        #waits an hour until collecting data again
        time.sleep(3600)
        scrape()
        print("Scraped " + time.time())


scrape()
