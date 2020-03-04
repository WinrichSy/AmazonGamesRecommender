import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import string
import time

import matplotlib.ticker as ticker
import itertools
import warnings

from datetime import datetime
from dateutil.parser import parse

#models
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import precision_score, recall_score, accuracy_score, roc_auc_score
from sklearn.decomposition import NMF, TruncatedSVD

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
import unicodedata

from scipy.sparse.linalg import svds

from collections import Counter

#from surprise import SVD, SVDpp, Slope

warnings.filterwarnings('ignore')
plt.style.use('ggplot')

class EDA:
    #========__init__====================#
    #========initializes the EDA object =#
    def __init__(self):

        #initializes variables for NLP use later
        self.stopwords_ = set(stopwords.words('english'))
        self.punctuation_ = set(string.punctuation)
        pass


    #========AUTOLABEL takes in rect objects from ===========================#
    #========subplots and output their numerical values on top of BAR PLOTS =#
    def autolabel(self, rects, ax, orientation='vert'):
        #prints value above vertical bars
        if orientation=='vert':
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(int(height)),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            weight = 'bold',
                            textcoords="offset points",
                            ha='center', va='bottom',
                            size=15)
        #Prints value to the right of horizontal bars
        elif orientation=='hort':
            for rect in rects:
                width = rect.get_width()
                ax.annotate('{}'.format(int(width)),
                            xy=(width, rect.get_y() + rect.get_height() / 2),
                            xytext=(3,-6),
                            textcoords="offset points",
                            size=15)


    #========AUTOLABEL_PERCENT takes in rect objects from ==============#
    #========subplots and output percentage values on top of BAR PLOTS =#
    def autolabel_percent(self, rects, ax, orientation='vert'):
        #Prints percentage above bars for vertical bars
        if orientation=='vert':
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{0:.2f}%'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            weight = 'bold',
                            textcoords="offset points",
                            ha='center', va='bottom',
                            size=15)
        #Prints percentages to the right of bars in horizontal bars
        elif orientation=='hort':
            for rect in rects:
                width = rect.get_width()
                ax.annotate("{0:.2f}%".format(width),
                            xy=(width, rect.get_y() + rect.get_height() / 2),
                            xytext=(3,-6),
                            textcoords="offset points",
                            size=15)

    #========print_bar=====================================#
    #========Print functions for bar graphs specifically ==#
    def print_bar(self, x, y, x_label, y_label, title='insert title', orientation='vert', color='blue',
                  width=0.65, fig_size=(12,7), percentage=False, weight='bold', tick_size=20, title_size=35,
                  label_size=30):

        fig, ax = plt.subplots(figsize=fig_size)
        if orientation=='vert':
            bars_for_annotation = ax.bar(x, y, color=color, align='center', width=width)
        elif orientation=='hort':
            bars_for_annotation = ax.barh(x, y, color=color, align='center')


        plt.xticks(size = tick_size)
        plt.yticks(size = tick_size)
        plt.xlabel(x_label, size=label_size, color=color, weight='bold')
        plt.ylabel(y_label, size=label_size, color=color, weight='bold')
        plt.title(title, fontsize=title_size, color=color, weight='bold')

        if percentage:
            self.autolabel_percent(bars_for_annotation, ax, orientation=orientation)
        elif not percentage:
            self.autolabel(bars_for_annotation, ax, orientation=orientation)

        plt.show()


    #========language_detect takes in a series of STRINGS objects ====#
    #========and returns their expected language code ================#
    def language_detect(self, series):
        import langdetect as ld
        #TODO: determine if langdetect can take in numbers
        if isinstance(series[0],float):
            print('Error: floats were passed instead of strings')
            return

        #TODO: handle NaNs
        #TODO: 1. have to handle exceptions
        # languages = series.apply(lambda x: ld.detect(x))
        languages = []
        for idx, val in enumerate(series):
            try:
                languages.append(ld.detect(val))
            except:
                languages.append('nonsense')

        #TODO: how to do this faster w/o doing list comprehension
        languages = ['zh' if x=='zh-cn' or x=='zh-tw' else x for x in review_language]

        return languages


    #TODO: handle nans in lists of strings by turning them into litterally strings 'nan'?
    #TODO: should I accompany it with means? depenedant on value? string or float? .isna()?
    def handle_nans(self):
        pass

    #========to_datetime converts strings to  ============#
    #========datetime objects and returns list ===========#
    #TODO: test to see if it works
    def to_datetime(self, series):
        return series.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
        # date_time = pd.Series([datetime.strptime(x, '%Y-%m-%d') for x in paris_calendar['date']])

    #======== week returns the dateime in week
    def week(self, series):
        return series.apply(lambda x: x.week)

    #======== month returns the dateime in month
    def month(self, series):
        return series.apply(lambda x: x.month)

    #======== year returns the dateime in year
    def year(self, series):
        return series.apply(lambda x: x.year)

    #===========================NATURAL LANGUAGE PROCESSING==================#
    #TODO: can these be within a class without being in a definition?
    #TODO: add more complexity to take in other languages. maybe add definition?


    #========filter_tokens filters out stop words ============#
    #========and punctuations from sentences =================#
    def filter_tokens(self, sent):
        return([w for w in sent if not w in self.stopwords_ and not w in self.punctuation_])


    #========remove_accents removes accents =================#
    #========from input string ==============================#
    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii.decode()

    #========personal_tokenize will remove accents, tokenize words, =====================================#
    #========filter stopwords and puncutations, and stem words; DEFAULT: ENGLISH, SNOWBALL STEMMER=======#
    def personal_tokenize(self, sentence, language='english', stemmer='snowball'):

        string = " "

        #configure stemmer
        if stemmer=='snowball':
            stemmer = SnowballStemmer(language)


        #remove accents
        input_string = self.remove_accents(sentence)

        #tokenize
        sent_tokens = sent_tokenize(input_string)
        tokens = [sent for sent in map(word_tokenize, sent_tokens)]
        tokens_lower = [[word.lower() for word in sent] for sent in tokens]

        #filtering stopwords and punctuations
        tokens_filtered = list(map(self.filter_tokens, tokens_lower))
        tokens_filtered_list = list(itertools.chain.from_iterable(tokens_filtered))

        #stemming words
        tokens_stemporter = [list(map(stemmer.stem, sent)) for sent in tokens_filtered]
        return string.join(list(itertools.chain.from_iterable(tokens_stemporter)))

    #===========================MODELING===============================#
    def calculate_threshold_values(self, prob, y):
        '''
        Build dataframe of the various confusion-matrix ratios by threshold
        from a list of predicted probabilities and actual y values
        '''
        df = pd.DataFrame({'prob': prob, 'y': y})
        df.sort_values('prob', inplace=True)

        actual_p = df.y.sum()
        actual_n = df.shape[0] - df.y.sum()

        df['tn'] = (df.y == 0).cumsum()
        df['fn'] = df.y.cumsum()
        df['fp'] = actual_n - df.tn
        df['tp'] = actual_p - df.fn

        df['fpr'] = df.fp/(df.fp + df.tn)
        df['tpr'] = df.tp/(df.tp + df.fn)
        df['precision'] = df.tp/(df.tp + df.fp)
        df = df.reset_index(drop=True)
        return df

    def add_random_to_plot_roc(self, ax, label='random'):
        ax.plot([0,1],[0,1], 'k', label="random")
        ax.legend()

    def plot_roc(self, ax, df, label="ROC"):
        ax.plot([1]+list(df.fpr), [1]+list(df.tpr), label=label)
        ax.set_xlabel('fpr')
        ax.set_ylabel('tpr')
        ax.set_title('ROC Curve')
        ax.legend()

    def modelling(self, X, y, model):

#     X = vectorizer.fit_transform(text_series)

#     if model.__class__.__name__ == "GaussianNB":
#         X = X.toarray()

        X_train, X_test, y_train, y_test = train_test_split(X, y)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)

        probs = model.predict_proba(X_test)[:,1]
        roc_auc = roc_auc_score(y_test, probs)
        thresh_df =calculate_threshold_values(probs, y_test)

        return (precision, recall, accuracy, probs, roc_auc, thresh_df)
#     return (probs, thres_df, roc_auc)

    def svd_mat(self, df, k=10):
        u, s, vt = svds(df, k)
        sigma = np.diag(s)
        user_biz_predictions = u @ sigma @ vt + df.mean(axis=0).to_numpy()
        return s, user_biz_predictions

    def remov_duplicates(self, input):
        # split input string separated by space
        input = input.split(" ")

        # joins two adjacent elements in iterable way
        for i in range(0, len(input)):
          input[i] = "".join(input[i])

        # now create dictionary using counter method
        # which will have strings as key and their
        # frequencies as value
        UniqW = Counter(input)

        # joins two adjacent elements in iterable way
        s = " ".join(UniqW.keys())
        return s

    #==========
    #=========
    def TFIDF_model(self, tokens, model_type = 'svd'):

        self.vectorizer = TfidfVectorizer(stop_words = self.stopwords_, ngram_range = (1,1))

        doc_word = self.vectorizer.fit_transform(tokens)

        if model_type == 'svd':
            self.svd = TruncatedSVD(8)
            return self.svd.fit_transform(doc_word)
        elif model_type == 'nmf':
            self.nmf = NMF(8)
            return self.nmf.fit_transform(doc_word)
        else:
            return


    def display_topics(self, model, feature_names, no_top_words, no_top_topics, topic_names=None):
        count = 0
        for ix, topic in enumerate(model.components_):
            if count == no_top_topics:
                break
            if not topic_names or not topic_names[ix]:
                print("\nTopic ", (ix + 1))
            else:
                print("\nTopic: '",topic_names[ix],"'")
            print(", ".join([feature_names[i] for i in topic.argsort()[:-no_top_words-1:-1]]))
            count += 1

    #===COUNTDOWN_TO_MENU===============
    #===Count down to return to 'menu'==
    def countdown(self, message, countdown_time = 5):
        countdown = countdown_time
        while(countdown>0):
            print('{}...{}'.format(message, countdown), end='\r')
            countdown -= 1
            time.sleep(1)
