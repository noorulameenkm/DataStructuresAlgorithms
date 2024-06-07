import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Comparator;
import java.util.function.Supplier;

record Input(List<String> dictionary, String sentence) {}

public class ReplaceWords {
    public String replaceWords(List<String> dictionary, String sentence) {
        Map<String, List<String>> lookupTable = new HashMap<>();
        Supplier<List<String>> initSupplier = () -> new ArrayList<String>();
        for(String d : dictionary) {
            String firstChar = d.substring(0, 1);
            List<String> existingList = lookupTable.getOrDefault(
                firstChar, initSupplier.get());
            existingList.add(d);
            existingList.sort(Comparator.naturalOrder());
            lookupTable.put(firstChar, existingList);
        }

        StringBuilder builder = new StringBuilder();
        String[] splitString = sentence.split(" ");
        for(int i = 0; i < splitString.length; i++) {
            if(!lookupTable.containsKey(splitString[i].substring(0, 1))) {
                builder.append(splitString[i]);
            } else {
                List<String> lst = lookupTable.get(splitString[i].substring(0, 1));
                boolean found = false;
                for(String s : lst) {
                    if(splitString[i].startsWith(s)) {
                        builder.append(s);
                        found = true;
                        break;
                    }
                }

                if(!found) {
                   builder.append(splitString[i]); 
                }
            }
            
            if(i != splitString.length - 1)
                builder.append(" ");

        }

        return builder.toString();
    }

    public static void main(String[] args) {
        ReplaceWords replaceWords = new ReplaceWords();
        List<Input> inputs = List.of(
            new Input(List.of(
                "cat","bat","rat"
            ), "the cattle was rattled by the battery"),
            new Input(List.of(
                "a","b","c"
            ), "aadsfasf absbs bbab cadsfafs")
        );

        inputs.forEach((input) -> System.out.println(replaceWords.replaceWords(input.dictionary(), input.sentence())));
    }
}