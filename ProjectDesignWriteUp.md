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
* Description of data set available, at the field level (see table)
* If from an API, include a sample return (this is usually included in API documentation!) (if doing this in markdown, use the javacription code tag)

### Domain knowledge
* What experience do you already have around this area?
* Does it relate or help inform the project in any way?
* What other research efforts exist?
    * Use a quick Google search to see what approaches others have made, or talk with your colleagues if it is work related about previous attempts at similar problems.
    * This could even just be something like "the marketing team put together a forecast in excel that doesn't do well."
    * Include a benchmark, how other models have performed, even if you are unsure what the metric means.

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
