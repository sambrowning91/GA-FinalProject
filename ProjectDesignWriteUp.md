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
* What questions do you have about your project? What are you not sure you quite yet understand? (The more honest you are about this, the easier your instructors can help).
* What are the assumptions and caveats to the problem?
    * What data do you not have access to but wish you had?
    * What is already implied about the observations in your data set? For example, if your primary data set is twitter data, it may not be representative of the whole sample (say, predicting who would win an election)
* What are the risks to the project?
    * What's the cost of your model being wrong? (What's the benefit of your model being right?)
    * Is any of the data incorrect? Could it be incorrect?

### Outcomes
* What do you expect the output to look like?
* What does your target audience expect the output to look like?
* What gain do you expect from your most important feature on its own?
* How complicated does your model have to be?
* How successful does your project have to be in order to be considered a "success"?
* What will you do if the project is a bust (this happens! but it shouldn't here)?
