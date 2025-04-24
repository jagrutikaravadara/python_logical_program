import re
from collections import Counter, defaultdict
import heapq

STOP_WORDS = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'of', 'to', 'for', 'with', 'as', 'by', 'that', 'this'}

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, freq):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            heapq.heappush(node.words, (-freq, word))

    def top_k(self, prefix, k):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        seen = set()
        result = []
        for freq_neg, word in sorted(node.words):
            if word not in seen:
                result.append((word, -freq_neg))
                seen.add(word)
                if len(result) == k:
                    break
        return result

def build_analyzer(text):
    words = [w for w in re.findall(r'\b\w+\b', text.lower()) if w not in STOP_WORDS]
    freq = Counter(words)
    trie = PrefixTrie()
    for word, count in freq.items():
        trie.insert(word, count)
    return trie

# Example usage
text = """

There are thoughts and themes that thrive in this thick text. But the text is thick with thought.
"""

trie = build_analyzer(text)
print(trie.top_k('th', 3))  # Returns top 3 words starting with 'th'
