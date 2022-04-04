# import TextBlob
from textblob import TextBlob

a = TextBlob("TechM is a good compny and alays valule ttheir employeees.")

# using TextBlob.correct() method
a = a.correct()

print(a)
