def is_spam(text, spam_words):
    text = text.lower()
    for word in spam_words:
        if word in text:
            return "spam"
    return "not spam"

spam_words = ["free", "prize", "winner", "cash", "urgent"]
message = "you are winning a free prize now!"
print(is_spam(message, spam_words))
