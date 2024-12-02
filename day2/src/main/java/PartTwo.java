import java.util.Arrays;

public class PartTwo {
    public static int main(int[][] input) {
        return Arrays.stream(input)
                    .map(line -> genIntervals(line))
                    .mapToInt(intervals -> isSafe(intervals))
                    .sum();
    } 

    private static int isSafe(int[] line) {
        // for (int num: line) System.out.print(num + " ");

        if (isAscending(line) || isDescending(line)) {
            System.out.println(" - safe");
            return 1;
        }
        else {
            System.out.println(" - unsafe");
            return 0;
        }
    }

    private static int[] genIntervals (int[] line) {
        int[] result = new int[line.length - 1];
        int curr = line[0];
        for (int i = 1; i < line.length; i++) {
            result[i - 1] = line[i] - curr;
            curr = line[i];
            System.out.print(result[i - 1] + " ");
        }
        System.out.println();
        return result;
    }

    private static boolean isAscending (int[] intervals) {
        boolean chance = true;
        for (int i = 0; i < intervals.length - 1; i++) {
            if (intervals[i + 1] <= 0 || intervals[i + 1] > 3) {
                if (chance) {
                    chance = false;
                    int sum = intervals[i] + intervals [i + 1];
                    if (sum <= 0 || sum > 3) {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean isDescending (int[] intervals) {
        boolean chance = true;
        for (int i = 0; i < intervals.length - 1; i++) {
            if (intervals[i + 1] >= 0 || intervals[i + 1] < -3) {
                if (chance) {
                    chance = false;
                    int sum = intervals[i] + intervals [i + 1];
                    if (sum >= 0 || sum < -3) {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
