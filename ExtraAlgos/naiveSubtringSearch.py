#A naive algorithm to find substrings in text, we compare whole pattern after every shift, with no
#preprocessing nor hash simplification. Classical m*n time complexity

def match(text, pattern):
    if (text == pattern):
        return True;
    return False;

#Naive text searching pattern algo with m*n time complexity
def naiveSearch(txt, pattern):
    #We shift every letter and than match making the time complexity  O=m*n (technially O=(m-n)*n)
    for i in range(0, len(txt) - len(pattern)):
        if (match (txt[i:i+len(pattern)], pattern)):
            print("%s%s%s" % (txt[:i], txt[i:i+len(pattern)].upper(), txt[i+len(pattern):]));

text = "AAAAABAAABA";
text = text.lower();
text = text + text + text;
pattern = "AAAA";
pattern = pattern.lower();
naiveSearch(text, pattern);