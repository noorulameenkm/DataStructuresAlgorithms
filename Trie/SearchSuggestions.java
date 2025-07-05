package Trie;

import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class Trie {
    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for(char c : word.toCharArray()) {
            int index = c - 'a';
            if(node.children[index] == null)
                node.children[index] = new TrieNode();
            node = node.children[index];
        }
        node.isEnd = true;
    }

    public List<String> searchAll(String prefix) {
        TrieNode node = root;
        for(char c: prefix.toCharArray()) {
            int index = c - 'a';
            if(node.children[index] == null) return Collections.emptyList();
            node = node.children[index];
        }
        return dfs(node, new StringBuilder(prefix), new ArrayList<>());
    }

    private List<String> dfs(TrieNode node, StringBuilder prefix, List<String> words) {
        if(words.size() == 3) return words;
        if(node.isEnd) words.add(prefix.toString());

        for(char c = 'a'; c < 'z'; c++) {
            if(node.children[c - 'a'] != null) {
                prefix.append(c);
                dfs(node.children[c - 'a'], prefix, words);
                prefix.deleteCharAt(prefix.length() - 1);
            }
        }

        return words;
    }
}

public class SearchSuggestions {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        List<List<String>> result = new ArrayList<>();
        Trie trie = new Trie();
        for(String product: products) trie.addWord(product);
        StringBuilder builder = new StringBuilder();
        for(char c : searchWord.toCharArray()) {
            builder.append(c);
            result.add(trie.searchAll(builder.toString()));
        }
        return result;
    }

    public static void main(String[] args) {
        final SearchSuggestions searchSuggestions = new SearchSuggestions();
        System.out.println(searchSuggestions.suggestedProducts(new String[]{"apple", "apricot", "application"}, "app"));
    }
}

