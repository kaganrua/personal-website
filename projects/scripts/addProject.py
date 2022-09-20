"""
from django.db import models
from projects import models.Project

p1 = Project(title = "2020 US Elections",description= "Collected data from both political spectrum using Reddit API, and preprocessed, analyzed and interpreted the data.",technology="Python, Pandas, Scikit-learn, NLTK, BeautifulSoup, Reddit REST API",image = "img/project1.png")
p1.save()

p2 = Project(title= "Text Classification using Phonological Features",description="Investigated possible usage of phonetical alphabet in text classification tasks, using Convolutional and Recurrent Neural Network",technology="Python, Numpy, Tensorflow, Google Cloud, NLTK, Matplotlib, Jupyter Notebook",image = "img/project2.png")
p2.save()

#p3 = Project(title="Word Sense Disambiguation",description="Built a semi-supervised Machine Learning model that predicts the meaning of a sentence in a given context",technology="Python, Numpy, NLTK, Scikit-learn",image="img/project3.png")

p3.save()

#p4 = Project(title="Sabouteur Game Agent",description="Engineered an AI agent for Sabouteur Card Game, using the Monte-Carlo reinforcement learning algorithm.",technology="Java",image="img/project4.png")

p3 = Project(title="Operating System",description="Developed an Operating System in C and mimiced hardware components such as CPU",technology="C",image="img/project5.png")
"""
