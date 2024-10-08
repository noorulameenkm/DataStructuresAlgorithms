public class SentenceSimilarity {
    
    public static void main(String[] args) {
        SentenceSimilarity sentenceSimilarity =
        new SentenceSimilarity();

        System.out.println(
            sentenceSimilarity
            .areSentencesSimilar("My name is Haley", "My Haley")
        );
        System.out.println(
            sentenceSimilarity
            .areSentencesSimilar("of", "A lot of words")
        );
        System.out.println(
            sentenceSimilarity
            .areSentencesSimilar("Eating right now", "Eating")
        );
    }

    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] words1 = sentence1.split(" ");
        String[] words2 = sentence2.split(" ");

        if(words1.length > words2.length) {
            String[] temp = words1;
            words1 = words2;
            words2 = temp;
        }

        int length1 = words1.length;
        int length2 = words2.length;

        int matchFromStart = 0;
        int matchFromEnd = 0;

        while(matchFromStart < length1 && words1[matchFromStart].equals(words2[matchFromStart])) {
            matchFromStart ++;
        }

        while(matchFromEnd < length1 && words1[length1 - 1 - matchFromEnd].equals(words2[length2 - 1 - matchFromEnd])) {
            matchFromEnd ++;
        }

        int totalMatches = matchFromStart + matchFromEnd;
        return totalMatches >= length1;

    }
}
