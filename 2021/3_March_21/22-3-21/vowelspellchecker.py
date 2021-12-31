class Solution:
    def spellchecker(self, wordlist, queries):
        def replace_vowel(word):
            return "".join("*" if c in "aeiou" else c for c in word)
        perfect_match = set(wordlist)
        case_error, vowel_error = dict(), dict()
        for word in wordlist:
            word2 = word.lower()
            case_error.setdefault(word2, word)
            vowel_error.setdefault(replace_vowel(word2), word)

        def solve(query):
            if query in perfect_match:
                return query
            lower_query = query.lower()
            if lower_query in case_error:
                return case_error[lower_query]
            vowel_query = replace_vowel(lower_query)
            if vowel_query in vowel_error:
                return vowel_error[vowel_query]
            return ""
        return map(solve, queries)
