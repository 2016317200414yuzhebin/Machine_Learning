import gensim
import pandas as pd

df = pd.read_json("Cell_Phones_and_Accessories_5.json", lines = True)

review_text = df.reviewText.apply(gensim.utils.simple_preprocess)

model = gensim.models.Word2Vec(
    window = 10,
    min_count = 2,
    workers = 4,
)

model.build_vocab(review_text, progress_per = 1000)
model.train(review_text, total_examples = model.corpus_count, epochs = model.epochs)
model.save("./word2vec-amazon-cell-accessories-reviews-short.model")
model.wv.most_similar("awful")