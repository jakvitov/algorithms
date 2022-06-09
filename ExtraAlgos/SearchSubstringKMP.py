def findSuffixes(pattern):
    result = [];
    for i in range(len(pattern), 0, -1):
        result.append(pattern[i:]);
    return result;

def findPrefixes(pattern, result):
    for i in range (0, len(pattern)):
        result.append(pattern[:i]);
    return result;

def findLongest(prefixes, suffixes):
    longest = 0;
    for i in range(1, len(prefixes)):
        if (prefixes[i] == suffixes[i]):
            longest = len(suffixes[i]);
    return longest;

#Calculate the LPS table for the KMP search algorithm
def calculateLPS(pattern):
    lps = [];
    for i in range(0, len(pattern)):
        prefix = []
        subpat = pattern[:i + 1];
        prefix = findPrefixes(subpat, prefix);
        suffix = findSuffixes(subpat);
        lps.append(findLongest(prefix,suffix));
    return lps;

#Print all possible occurences of the given pattern in a text - Knuth Morris Pratt algorithm
#m time complexity, but needed preprocessing make it less efficient than Rabin Karp on large pattern searches
def KMPSearch(text, pattern):
    matches = {};
    lps = calculateLPS(pattern);
    print(lps);
    #We iterate i trough text and j trough pattern. Mismatch => j = lps[j-1]
    i = 0;
    j = 0;
    while (i < len(text)):
        if (text[i] == pattern[j]):
            i += 1;
            j += 1;
        if (j == len(pattern)):
            print("%s%s%s" % (text[:i - j], text[i - j: i].upper(), text[i:]));
            j = lps[j - 1];
        elif i < len(text) and pattern[j] != text[i]:
            if (j > 0):
                j = lps[j - 1];
            else:
                i += 1;



text = "AAAAABAAABA";
text = text.lower();
text = text + text + text;
pattern = "AAAA";
pattern = pattern.lower();
KMPSearch(text, pattern);