from textblob import TextBlob
 
blob = TextBlob("Comment vas-tu?")
 
print(blob.detect_language())
 
print(blob.translate(to='es'))
print(blob.translate(to='en'))
print(blob.translate(to='zh'))