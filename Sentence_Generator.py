import nltk
import random
import csv

# # Download punkt
# nltk.download('punkt')

def tokenize_text_to_sentences(text):
    """Tokenizes a given text into sentences"""
    return nltk.sent_tokenize(text)

def load_texts(filenames):
    """Load texts from files and tokenize into sentences"""
    sentences = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences.extend(tokenize_text_to_sentences(text))
    return sentences

def randomize_sentences(sentences, n=20):
    """Randomly select n sentences from the list"""
    return random.sample(sentences, n)

if __name__ == "__main__":
    filenames = ["C:/Users/ddavi/Python projects/Sentence_Gen/ulysses.txt", "C:/Users/ddavi/Python projects/Sentence_Gen/rainbow.txt", "C:/Users/ddavi/Python projects/Sentence_Gen/homer.txt"]
    sentences = load_texts(filenames)
    randomized_sentences = randomize_sentences(sentences, 20)

    csv_path = "C:/Users/ddavi/Python projects/Sentence_Gen/sentences.csv"

    with open(csv_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for sentence in randomized_sentences:
            writer.writerow([sentence])

    for sentence in randomized_sentences:
        print(sentence)
