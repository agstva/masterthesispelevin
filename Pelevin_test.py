import spacy 
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

chapter1 = chap[0]
nlp = spacy.load("ru_core_news_lg")

doc = nlp(chapter1)
sentences = list(doc.sents)
# print(sentences[1])
for line in sentences:
    print(line)

print("Master branch")
