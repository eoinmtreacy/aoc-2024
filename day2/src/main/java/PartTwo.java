import java.util.Arrays;

public class PartTwo {
    public static int main(int[][] input) {
        return Arrays.stream(input)
                    .map(line -> genIntervals(line))
                    .mapToInt(intervals -> isSafe(intervals))
                    .sum();
    } 

    private static int isSafe(int[] line) {
        for (int num: line) System.out.print(num + " ");

        if (safeUp(line) || safeDown(line)) {
            // System.out.println(" - safe");
            System.out.println();
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
        }
        return result;
    }

    private static boolean safeUp (int[] intervals) {
        // System.out.print("Safe up? ");
        boolean chance = true;
        if (intervals[0] <= 0 || intervals[0] > 3) {
            chance = false;
        }
        for (int i = 1; i < intervals.length - 1; i++) {
            // System.out.println("interval: " + intervals[i] + "chance: " + chance); 
            if (intervals[i] <= 0 || intervals[i] > 3) {
                if (chance) {
                    chance = false;
                    int newDiff = intervals[i] + intervals[i - 1];
                    if (newDiff <= 0 || newDiff > 3) return false;
                } else {
                    return false;
                }
            }


        }
        if (intervals[intervals.length - 1] <= 0 || intervals[intervals.length - 1] > 3) {
                if (!chance) return false;
        }
        return true;
    }

    private static boolean safeDown (int[] intervals) {
        // System.out.print("Safe down? ");
        boolean chance = true;
        if (intervals[0] >= 0 || intervals[0] < -3) {
            chance = false;
        }
        for (int i = 1; i < intervals.length - 1; i++) {
            // System.out.println("interval: " + intervals[i] + "chance: " + chance); 
            if (intervals[i] >= 0 || intervals[i] < -3) {
                if (chance) {
                    chance = false;
                    int newDiff = intervals[i] + intervals[i - 1];
                    if (newDiff >= 0 || newDiff < -3) return false;
                } else {
                    return false;
                }
            }
        }
        if (intervals[intervals.length - 1] >= 0 || intervals[intervals.length - 1] < -3) {
                if (!chance) return false;
        }
        return true;
    }



}
