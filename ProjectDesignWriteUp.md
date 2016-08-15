# Project Design Writeup - Investment Management News Articles Recommender System

### Project Problem and Hypothesis

* In the current Economic landscape the volume of news articles being written about topics that impact the investment management industry is increasingly rapidly. As an interested party in the industry (employee of an Investment Manager, Industry Consultant, Financial Analyst, Member of the public who owns financial products) it has become very challenging to remain abreast of indsutry news. Combine this weight of available information with a busy work day/week and it is easy to see how individuals miss out on vital pieces of information. 
* This project aims to develop a recommender system that scrapes financial news companies' websites and prioritizes a recommended selection of articles for readers on a daily/weekly basis.
* The intial step will be to create a recommender system that is capable of providing a list of one-off recommendations for the given time horizon. Next, I will aim to integrate the recommender system with Slack so that it is able to incorporate feedback from users.
* There are multiple facets to this problem that can be partially or completely resolved by Machine Learning technqiues:
   * Natural Language Processing - first and foremost this is a natural language processing challenge. Beginning with multiple corpora on any given day or week we must process these and tokenize the content, grouping into topics where possible.
   * Once I have "NLP'd" the article I should be able to use multiple variables to build a binary classification model to predict first and foremost 'Interesting or Not'. Then I need to be able to rank our remaining articles from Most interesting to least interesting (how?)
   * Finally, I would like to be able to integrate the results on a daily basis and allow users to 'upvote' or 'downvote' articles. This could be done on aggregate, or at an individual user level in order to leverage collaborative filtering approaches and continuously improve the engine
* As an initial guess, I expect that the sentiment of an article will have a key impact in predicting 'level of interestingness'. strongly negative or positive articles are expected to provide the greatest interest to users. Additionally I would like to add an 'IsClient' dummy variable that indicates whether the article is talking about one of my firm's clients. If the article is, then I expect this to heavily influence whether or not the article is found to be interesting.

### Datasets
* The data available to me for this topic is limited and will require html scraping of various news sources. In order to enable my project to be scalable and deliver some results in the near-term (rather than becoming bogged down in trying to scrape the entire daily financial news literature on the worldwide web) I will focus on the following sites in priority order, and will likely start with only 2 websites, extending as time permits:
1. citywire.co.uk/wealth-manager
2. http://www.funds-europe.com/news
3. http://www.ignites.com
4. https://next.ft.com/ftfm
* Many of the above require credentials to access the full article. For consideration will be how to store this credentials offline and access them in my script such that they are not uploaded to, and therefore exposed on, GitHub

### Domain knowledge
* I have worked in the Investment Management industry for 2-3 years and as such have good knowledge of the avaialable news sources and what might indicate whether or not an article is deemed of high or low interest to industry-concerned individuals (at my firm at least)
* Similar projects do exist, but with a focus on creating news article recommendation systems for Front Office researchers and analysts in the industry. For example recommending articles that may give some previously unnoticed insight into the performance of a company, or indeed using twitter sentiment analysis to provide early indication of macroeconomic factors

### Project Concerns
* Key concerns at present include the following:
  * The depth of my understanding of NLP - this is likely, I expect, to be the most time-consuming area, just processing each of the articles, in a repeatable fashion.
  * Being able to predict 'level of interestingness' - I assume this will need some level of input on my behalf to create some training reference set that the model can use. This feels as though it will be fairly arbitrary though, and what volume is required?
  * There's an awful lot to do in the time available, particularly if I want to take the Slack part of it to any level of completeness - I think I will likely have a lot of follow-up items afterwards!
* Assumptions and caveats:
    * A key assumption that will be included initially is that my personal preferences are reflective across the population of industry professionals. How I classify whether an article is interesting or not will influence how the model is trained - it could very well be the case that something that is interesting to me, is not interesting to others and vice versa.
    * I do not have access to webpage readership data which is unfortunate as this would give a very good indication of the perceived level of interestingness for each comment based on the general reader base. One idea was to use number of comments on the article as a proxy for this, but typically articles do not receive any comments at all and so this is unlikely to be a good predictor. 
    * The data will already be focused on Investment Management since the websites focused on are providers of news to that sector. We are not crawling generic news websites and looking for articles about Investment Maangement

### Outcomes
* I expect the output to be a daily/weekly ranked top 'n' articles
* My target audience expects the output to be served in a way that is readily consumable, and that provides them an opportunity to feed back into the modeeling of 'interesting articles'.
* The model could start very simple, with just, for example, the top 'Citywire' articles of the week, and then move to a higher frequency and cadence of recommendations, and incorporate additional sources.
* If rolled out to colleagues then the audience will be highly critical! My model needs at least an 85% success rate in identifying an 'interesting' article, otherwise adoption is likely to be poor.
