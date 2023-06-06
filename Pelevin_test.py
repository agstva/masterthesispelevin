import spacy, codecs
from collections import Counter
CHAPTERS = [
    "ГОЛЬДЕНШТЕРН ВСЕ",
    "ПОЕДИНОК",
    "СВИДЕТЕЛЬ ПРЕКРАСНОГО",
    "БРО КУКУРАТОР",
    "КОШЕЧКА",
    "МИТИНА ЛЮБОВЬ",
    "HOMO OVERCLOCKED"
]
сhapters = []
with open("./data/Pelevin.txt", "r") as f:
    text = f.read()
    chap = text.split(CHAPTERS[0]) [1:]

print("Loaded file")

chapter1 = chap[0]
nlp = spacy.load("ru_core_news_lg") # lg : it gives a much cleaner list with a large model

print("Loaded model")
print("Processing text")
doc = nlp(chapter1)
print("Finished processing text")
#sentences = list(doc.sents) # devide in sent
#sentence = (sentences[1])

# for line in sentences:
#     print(line)

ents = list(doc.ents) #extract entities
#print(ents[0].label)
#print(ents[0].label_)
#print(ents[0].text)

places = []
print("Extract locations")
for ent in ents:
    if (ent.label_ == "LOC") or (ent.label_ == "GPE"):
        places.append(ent.lemma_) #text
# print(set(places))
count = Counter(places)
#print(places)
with codecs.open("final.txt", "w", "utf8") as f:
    for ent in count.most_common():
        f.write(ent[0] + ":" + str(ent[1])+"\n")
print("Finished!")