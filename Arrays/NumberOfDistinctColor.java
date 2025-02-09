import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class NumberOfDistinctColor {
    public int[] queryResults(int limit, int[][] queries) {
        Map<Integer, Integer> ballToColor = new HashMap<>();
        Map<Integer, Integer> colorToCount = new HashMap<>();
        int[] result = new int[queries.length];
        int i = 0;
        for(int[] query: queries) {
            int ball = query[0];
            int color = query[1];

            if(ballToColor.containsKey(ball)) {
                int prevColor = ballToColor.get(ball);
                ballToColor.put(ball, color);
                colorToCount.put(color, colorToCount.getOrDefault(color, 0) + 1);
                colorToCount.put(prevColor, colorToCount.get(prevColor) - 1);
                if(colorToCount.get(prevColor) <= 0) colorToCount.remove(prevColor);
            } else {
                ballToColor.put(ball, color);
                colorToCount.put(color, colorToCount.getOrDefault(color, 0) + 1);
            }

            result[i] = colorToCount.size();
            i++;
        }

        return result;
    }

    public static void main(String[] args) {
        NumberOfDistinctColor noc = new NumberOfDistinctColor();
        int limit = 4;
        int[][] queries = {{1,4},{2,5},{1,3},{3,4}};
        int[] result = noc.queryResults(limit, queries);
        System.out.println(Arrays.toString(result));

        queries = new int[][]{{0,1},{1,2},{2,2},{3,4},{4,5}};
        result = noc.queryResults(limit, queries);
        System.out.println(Arrays.toString(result));
    }
}
