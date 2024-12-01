import java.util.HashMap;

public class PartTwo {
    public static long main(int[][] input) {
        long sum = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int[] pair: input) {
            if (!map.containsKey(pair[1])) {
                map.put(pair[1], 0);
            }
            map.put(pair[1], map.get(pair[1]) + 1);
        }

        for (int[] pair: input) {
            if (map.containsKey(pair[0])) {
                sum += pair[0] * map.get(pair[0]);
            }
        }

        return sum;
    }
}
