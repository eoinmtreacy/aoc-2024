import java.util.Arrays;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PartTwo {
    static int ROW;
    static int COL;

    public static int main(char[][] input) {
        ROW = input.length;
        COL = input[0].length;

        int result = 0;

        for (int r = 1; r < ROW - 1; r++) {
            for (int c = 1; c < COL - 1; c++) {
                if (input[r][c] == 'A' && isXMAS(r, c, input)) result++;
            }
        }
        return result;
    }

    private static boolean isXMAS(int r, int c, char[][] grid) {
        String southEast = new String(
            new char[] {
                grid[r - 1][c - 1],
                grid[r][c],
                grid[r + 1][c + 1]
            }
        );

        String northEast = new String(
            new char[] {
                grid[r - 1][c + 1],
                grid[r][c],
                grid[r + 1][c - 1]
            }
        );

        // System.out.println(northEast + " " + southEast);

        return (
            (southEast.equals("MAS") || southEast.equals("SAM"))
            &&
            (northEast.equals("MAS") || northEast.equals("SAM"))
        );
    }

} 