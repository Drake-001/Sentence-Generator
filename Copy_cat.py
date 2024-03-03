import random

def input_passages(n):
    passages = {}
    for i in range(n):
        identifier = input(f"Enter the identifier for passage {i+1} (e.g., 'Ulysses'): ")
        passage = input("Now, enter the passage: ")
        passages[identifier] = passage
    return passages

def split_sentences(passages):
    sentences = []
    for identifier, passage in passages.items():
        for sentence in passage.split('. '):
            if sentence:  # Check if the sentence is not empty
                sentences.append((sentence + '.', identifier))  # Append sentence with period and identifier
    return sentences

def mix_and_tag_sentences(sentences):
    random.shuffle(sentences)  # Mix sentences randomly
    for sentence, identifier in sentences:
        print(f"{sentence} [{identifier}]")

def main():
    num_passages = int(input("How many passages will you input? "))
    passages = input_passages(num_passages)
    sentences = split_sentences(passages)
    mix_and_tag_sentences(sentences)

if __name__ == "__main__":
    main()
