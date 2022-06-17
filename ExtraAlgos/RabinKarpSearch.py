modular = 95257;

#Find all occurences of a pattern in a text using the Rabin-Karp algorithm
def search(text, pattern):
    base = 256;
    patternHash = 0;
    textHash = 0;
    highestDecimal = pow(base, len(pattern) - 1) % modular;

    #We calculate both hashes
    for i in range(len(pattern)):
        patternHash = (patternHash * base + ord(pattern[i])) % modular;
        textHash = (textHash * base + ord(text[i])) % modular;

    #Calculate hashes for pieces of text and compare them
    for i in range(len(text) - len(pattern)):
        #Next hash
        textHash = ((textHash - (ord(text[i]) * highestDecimal))*base + ord(text[i + len(pattern)])) % modular;
        if (textHash < 0):
            textHash = textHash + modular;

        if (textHash == patternHash):
            print("%s%s%s" % (text[:i + 1], text[i + 1:i + 1 +len(pattern)].upper(), text[i+ 1 +len(pattern):]));


search("bahojahojahoj","ahoj");