import java.util.PriorityQueue;

public class PartOne {
    public static int main(int[][] input) {
        int sum = 0;
        PriorityQueue<Integer> pq1 = new PriorityQueue<>(), pq2 = new PriorityQueue<>();
        for (int[] pair: input) {
            pq1.add(pair[0]);
            pq2.add(pair[1]);
        }
        while (!pq1.isEmpty()) {
            sum += Math.abs(pq1.poll() - pq2.poll());
        }
        return sum;
    }
}
