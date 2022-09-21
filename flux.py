import feedparser

def getfeed():
    feed = feedparser.parse("https://trends.google.com/trends/trendingsearches/daily/rss?geo=FR")
    entry = feed.entries[0]
    
    search = entry.ht_approx_traffic
    date = entry.published
    title = entry.title
    resume = entry.ht_news_item_snippet
    link = entry.ht_news_item_url

    return search, date[:-14], title, resume, link


print(f"🔭 {getfeed()[0]} \n📅 {getfeed()[1]}\n😳 {getfeed()[2]} \n📋 {getfeed()[3]}\n📰 {getfeed()[4]}")