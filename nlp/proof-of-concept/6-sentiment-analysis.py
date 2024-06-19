from transformers import pipeline

classifier = pipeline('sentiment-analysis')

feeds = {
    "sky_news": [
        "Greece shuts schools and Acropolis as heatwave hits: Greece has shuttered tourist hotspots and schools across Athens as the first heatwave of the summer strikes.",
        "'These are impossible conditions': Mother of freed hostage feared the worst for son held by Hamas: Evgeniia Kozlova was at home in St Petersburg last weekend when she got the call from her Israeli liaison officers.",
        "Post Office campaigner Alan Bates given knighthood - but insists there's still 'work to do': The campaigner has insisted the honour won't change his life, while his wife Suzanne told Sky News she is \"very proud\" of her \"very deserving\" husband.",
        "E.coli: Full list of products recalled by sandwich suppliers: Dozens of sandwiches, wraps and salads have been recalled as health officials work to track down the source of an E.coli outbreak - here are all the products recalled.",
    ],
    "bbc_news": [
        "Greek schools close because of 'historic' heatwave: Lots of schools in Greece have shut as the country experiences its first heatwave of the summer.",
        "King and Queen appear in Order of Garter ceremony: It was a plume with a view for the royals at Windsor this afternoon, as the King and Queen took part in the Order of the Garter ceremony.",
        "Petrol prices higher than they should be, says RAC: British drivers are facing petrol and diesel prices that are \"far higher than they should be\", according to the RAC.",
        "'A win is a win': England fans react to opening match: England fans have celebrated the team's victory over Serbia in their first Euro 2024 match.",
    ],
    "reuters": [
        "Freed hostage from Gaza needs 'time to heal', loved ones say: The mother of Andrey Kozlov, a hostage freed from Gaza, says she's the 'happiest' she's ever been",
        "Pentagon ran secret anti-vax campaign to undermine China during pandemic: The U.S. military launched a clandestine program amid the COVID crisis to discredit China’s Sinovac inoculation – payback for Beijing’s efforts to blame Washington for the pandemic. One target: the Filipino public. Health experts say the gambit was indefensible and put innocent lives at risk.",
        "Young British royals say 'We love you, Papa' in Father's Day message: The three young children of British heir-to-the-throne Prince William and his wife Kate released a Father's Day message and photograph on Sunday, saying \"We love you, Papa\".",
        "Ukraine to sign security agreements with Japan and US at G7: Ukraine's President Volodymyr Zelenskiy said he would sign a security agreement with Japan as well as one with the United States at the Group of Seven summit in Italy on Thursday."
    ],
    "japan_times": [
        "U.S. ran secret anti-vaccine campaign to undermine China during pandemic: At the height of the COVID-19 pandemic, the U.S. military launched a secret campaign to counter what it perceived as China’s growing influence in the Philippines, a nation hit especially hard by the deadly virus.",
        "In perspective: a firsthand account of this year’s G7: In an increasingly multipolar world, the bloc's relevance comes into question, but any attempt to foster dialogue and ease tensions should be welcomed.",
        "Aid groups welcome pauses in fighting but say Israel must do more to ease hunger: Some aid groups expressed skepticism that the Israeli military’s action would be transformative.",
        "Clock ticking for transfer of Tokyo giant panda cub twins to China: With the twin giant panda cubs at Tokyo's Ueno Zoo turning 3 years old on Sunday, the clock is ticking for their eventual transfer to China."
    ],
}

sentiments = {}
for feed, articles in feeds.items():
    sentiments[feed] = [ {'text': article, **(classifier(article)[0])} for article in articles ]

print(sentiments)