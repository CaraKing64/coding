
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = []
with open("words_alpha.txt", 'r') as doc:
    ls = doc.readlines()
    for w in ls:
          words.append(w.replace('\n', ''))

def match(word, max_matches=None):
    word = word.lower()
    scores = {}
    for w in words:
        scores[w] = getSimilarity(word, w)
    sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    if max_matches == None:
        return sorted_scores
    best = list(sorted_scores.keys())[:max_matches]
    best_dict = {}
    for w in best:
        #print(w, sorted_scores[w])
        best_dict[w] = sorted_scores[w]
    return best_dict

def compareDictionaries(dict1, dict2):
    count = 0
    for k in list(dict1.keys()):
        if k in list(dict2.keys()):
            count += dict1[k] - abs(dict1[k] - dict2[k])
    return count

def getSimilarity(word1, word2, debug=False):
    word1 = word1.lower()
    word2 = word2.lower()
    longer = word1 if len(word1) > len(word2) else word2
    shorter = word1 if longer == word2 else word2
    #print(longer, shorter)

    w1dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    w2dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for l in list(word1):
        w1dict[l] += 1
    for l in list(word2):
        w2dict[l] += 1
    letter_match_count = 0
    letter_index_match_count = 0
    letter_pair_match_count = 0
    for l in alphabet:
        while w1dict[l] > 0 and w2dict[l] > 0:
            letter_match_count += 1
            w1dict[l] -= 1
            w2dict[l] -= 1
    if letter_match_count / len(longer) > 0.5:
        for i in range(len(shorter)):
            if longer[i] == shorter[i]:
                letter_index_match_count += 1
        
        lpdict = {}
        spdict = {}
        for i in range(len(shorter)-1):
            lp = longer[i] + longer[i+1]
            sp = shorter[i] + shorter[i+1]
            if lp not in list(lpdict.keys()):
                lpdict[lp] = 0
            lpdict[lp] += 1
            if sp not in list(spdict.keys()):
                spdict[sp] = 0
            spdict[sp] += 1
        letter_pair_match_count = compareDictionaries(spdict, lpdict)

    letter_match_score = letter_match_count - (len(longer)-len(shorter))
    letter_index_match_score = letter_index_match_count
    letter_pair_match_score = letter_pair_match_count
    score = round(1*letter_match_score + 0.5*letter_index_match_score + 2*letter_pair_match_score, 4)
    if debug:
        print("W1", word1, "W2", word2, "LMS", letter_match_score, "LIMS", letter_index_match_score, "LPMS", letter_pair_match_score, "S", score)
    return score

#print(getSimilarity("understandable", "undertandable"))
#print(match("undertandable", 5))

while True:
    word_to_match = input("Enter a word (you can even spell it wrong): ")
    result = list(match(word_to_match, 1).keys())[0]
    print(f"Did you mean {result}?")


