
import java.util.Arrays;
import java.util.stream.IntStream;

public class PartTwo {
    public static int main(int[][] input) {
        return Arrays.stream(input)
                    .mapToInt(line -> isSafe(line))
                    .sum();
    } 

    private static int isSafe(int[] line) {
        if (isAscending(line) || isDescending(line)) return 1;

        for (int i = 0; i < line.length; i++) {
            int[] left = Arrays.copyOfRange(line, 0, i);
            int[] right = Arrays.copyOfRange(line, i + 1, line.length);

            int[] sub = IntStream.concat(Arrays.stream(left), Arrays.stream(right)).toArray();

            // for (int num : sub) System.out.print(num + " ");
            // System.out.println();


            if (isAscending(sub) || isDescending(sub)) return 1;
        }

        return 0;
    }

    private static boolean isAscending (int[] line) {
        int current = line[0];
        for (int i = 1; i < line.length; i++) {
            if (current >= line[i] || current + 3 < line[i]) {
                return false;
            }
            current = line[i];
        }
        return true;
    }

    private static boolean isDescending (int[] line) {
        int current = line[0];
        for (int i = 1; i < line.length; i++) {
            if (current <= line[i] || current - 3 > line[i]) {
                return false;
            }
            current = line[i];
        }
        return true;
    }
}


