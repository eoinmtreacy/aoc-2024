import java.util.Arrays;

public class PartOne {
    public static int main(int[][] input) {
        return Arrays.stream(input)
                    // .parallel()
                    .mapToInt(line -> isSafe(line))
                    .sum();
    } 

    private static int isSafe(int[] line) {
        for (int num: line) System.out.print(num + " ");
        if (isAscending(line) || isDescending(line)) {
            return 1;
        }
        else {
            return 0;
        }
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
