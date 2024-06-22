We all have used services like Netflix, Amazon, and Youtube. 
These services use very sophisticated systems to recommend the best items to their users to make their experiences great.

Types of Candidate Generation Systems:
Content-based filtering System
Collaborative filtering System

Content-based filtering system: 
Content-Based recommender system tries to guess the features or behavior of a user given the item’s features, he/she reacts positively to.
During recommendation, the similarity metrics (We will talk about it in a bit) are calculated from the item’s feature vectors and
the user’s preferred feature vectors from his/her previous records. 
Then, the top few are recommended.
Content-based filtering does not require other users' data during recommendations to one user.

Collaborative filtering System: 
Collaborative does not need the features of the items to be given. Every user and item is described by a feature vector or embedding.
It considers other users’ reactions while recommending a particular user. 
It notes which items a particular user likes and also the items that the users with behavior and likings like him/her likes, to recommend items to that user.
It collects user feedbacks on different items and uses them for recommendations.

Link for further explanation - "https://towardsdatascience.com/introduction-to-recommender-systems-1-971bd274f421"
