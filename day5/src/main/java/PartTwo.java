import java.util.Arrays;
import java.util.List;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class PartTwo {
    static HashMap<Integer, HashSet<Integer>> rulesMap;
    public static int main(ArrayList<int[]> rules, ArrayList<int[]> lines) {
        // hashmap for the orderings
        rulesMap = new HashMap<>();
        for (int[] rule: rules) {
            if (!rulesMap.containsKey(rule[0])) {
                rulesMap.put(rule[0], new HashSet<>());
            }
            rulesMap.get(rule[0]).add(rule[1]);
        }

        RulesComparator rulesComparator = new RulesComparator();

        int result = 0;

        for (int[] line: lines) {
            ArrayList<Integer> list = new ArrayList<>();
            PriorityQueue<Integer> pq = new PriorityQueue<>(rulesComparator);

            for (int num : line) {
                list.add(num);
                pq.add(num);
            }

            List<Integer> listPq = pq.stream().sorted(rulesComparator).collect(Collectors.toList());

            if (!list.equals(listPq)) {
                int mid = listPq.size() / 2;
                result += listPq.get(mid);
            } 
            
        }
        return result;
    }

    public static class RulesComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer a, Integer b) {
            if (!rulesMap.containsKey(a)) return 0;
            if (!rulesMap.get(a).contains(b)) return 0;
            return -1;
        }
    }
}