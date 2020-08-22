from textblob import TextBlob
line = input('enter in hindi')
text = TextBlob(line)
print(text.detect_language())
print(text.translate(to='en'))
# print(TextBlob('hi there, its meee').correct())