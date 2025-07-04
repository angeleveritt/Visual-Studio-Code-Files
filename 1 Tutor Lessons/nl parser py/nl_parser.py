import pprint
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")                              # Angel note:  unsupervised sentence tokenizer part of nltk.tokenize module
nltk.download("stopwords")                          # Angel note:  common words e.g., the, is , a, and
nltk.download("wordnet")                            # Angel note:  large lexical database of English developed at Princeton.  
# groups words into sets of synonyms called synsets and provides short definitions.  
# also records various semantic relationships btwn these synsets
# WordNet is powerful tool for finding synonyms and antonyms, exploring word meanings, performing semantic similarity comparisons, 
# navigating hypernyms (more general terms) and hyponyms (more specific terms)
# like a dictionary, thesaurus, and ontology all in one
# useful for word sense disambiguation, text classification, semantic search, chatbots and question answering
nltk.download("averaged_perceptron_tagger")         # Angel note:  part of speech (POS) tagger that uses the averaged perceptron algorithm 
# to assign grammatical tags (e.g., noun, verb, adj).  It's the default tagger used by nltk.pos_tag()
# the perceptron is a type of linear classifier.  
# The averaged perceptron improves on it by averaging the weights over all training iterations which helps reduce overfitting and improves generalization
# it's a greedy online learning algorithm
# uses features from the current word and its context (like previous tags, suffixes)
# during training, it guesses a tag, compares it to the correct one, and updates weights accordingly.
# the final model uses the average weight of all weight updates across iterations.
# features used:  current word, previous two predicted tages, word suffixes and prefixes, whether the word is capitalized, numeric, etc
####  didn't we prep our text by making it all lowercase?
# these features are combined into a feature vector, and the tag w the highest score is selected

nltk.download("omw-1.4")                            # Angel note:  Open Multilingual Wordnet verison 1.4.  
# it's a multilingual lexical resource that extends English WordNet by linking it to other WordNets in other languages. 
# this allows you to access translations and synonyms of WordNet synsets across dozens of languages.

valid_characters = string.ascii_lowercase + "-'@ "

#corpus = """The United States of America, also known as the United States or America, is a country primarily located in North America. It is a federal republic of 50 states and a federal capital district, Washington, D.C. The 48 contiguous states border Canada to the north and Mexico to the south, with the semi-exclave of Alaska in the northwest and the archipelago of Hawaii in the Pacific Ocean. The United States also asserts sovereignty over five major island territories and various uninhabited islands in Oceania and the Caribbean."""
with open(r"C:\0 Python Docs\docs to load into python or nltk - JUS\20110221 RDIMS-174248-v5-JustIM_-_Functional_Requirements_-_Gap_Analysis_-_using_ADRI_ICA_Module_2_until_ISO_available_-_DRAFTING_the_SHAPE.txt") as f:
    corpus = f.read()
corpus = corpus.lower()

new_corpus = ""
for letter in corpus:
    if letter not in valid_characters:
        continue
    new_corpus += letter

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

tokens = word_tokenize(new_corpus)

processed_words = []
for word in tokens:
    if word not in stop_words and len(word) > 2:
        lemmatized_word = lemmatizer.lemmatize(word)
        processed_words.append(lemmatized_word)

frequency = {}
for word in processed_words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Processed words:", processed_words)
print("\nWord frequency after processing:")
pprint.pprint(frequency)
print("\nOriginal processed corpus:", new_corpus)
