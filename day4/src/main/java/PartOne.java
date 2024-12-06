import java.util.Arrays;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PartOne {
    static int ROW;
    static int COL;
    public static int main(char[][] input) {
        ROW = input.length;
        COL = input[0].length;

        char[][] vertical = getVertical(input);

        // System.out.println("Horizontal:");
        // printLines(input);
        // System.out.println("Vertical:");
        // printLines(vertical);

        char[][] northEast = convertToCharArray(getNorthEast(input));
        // printLines(northEast);
        char[][] southEast = convertToCharArray(getSouthEast(input));
        // printLines(southEast);

        int result = 0;

        for (char[][] direction: new char[][][] {input, vertical, northEast, southEast}) {
            for (char[] line: direction) {
                int num = extract(line);
                // System.out.print(num + ": ");
                // for (char c: line) System.out.print(c);
                // System.out.println();
                result += num;
            }
        }

        return result;
    }
    
    public static int extract(char[] line) {
        ArrayList<String> cleaned = new ArrayList<>();

        Pattern pattern = Pattern.compile("XMAS");
        Matcher matcher = pattern.matcher(new String(line));
        
        while(matcher.find()) {
            cleaned.add(matcher.group());
        }

        pattern = Pattern.compile("SAMX");
        matcher = pattern.matcher(new String(line));
        
        while(matcher.find()) {
            cleaned.add(matcher.group());
        }

        return cleaned.size();
    }

    public static ArrayList<ArrayList<Character>> getNorthEast(char[][] input) {
        ArrayList<ArrayList<Character>> result = new ArrayList<>();
        for (int r = 0; r < ROW; r++) {
            int stash = r;
            int c = 0;
            ArrayList<Character> line = new ArrayList<>();
            while(r > -1 && c < COL) {
                line.add(input[r][c]);
                r--;
                c++;
            }
            result.add(line);
            r = stash;
        }

        for (int c = 1; c < COL; c++) {
            int stash = c;
            int r = ROW - 1;
            ArrayList<Character> line = new ArrayList<>();
            while(r > -1 && c < COL) {
                line.add(input[r][c]);
                r--;
                c++;
            }
            result.add(line);
            c = stash;
        }
        return result;
    }
    
    public static ArrayList<ArrayList<Character>> getSouthEast(char[][] input) {
        ArrayList<ArrayList<Character>> result = new ArrayList<>();
        for (int c = COL - 1; c > -1; c--) {
            int stash = c;
            int r = 0;
            ArrayList<Character> line = new ArrayList<>();
            while (r < ROW && c < COL) {
                line.add(input[r][c]);
                r++;
                c++;
            }
            result.add(line);
            c = stash;
        }

        for (int r = 1; r < ROW; r++) {
            int stash = r;
            int c = 0;
            ArrayList<Character> line = new ArrayList<>();
            while(r < ROW && c < COL) {
                line.add(input[r][c]);
                r++;
                c++;
            }
            result.add(line);
            r = stash;
        }
        return result;
    }

    public static char[][] getVertical(char[][] input) {
        char[][] result = new char[COL][ROW];
        for (int c = 0; c < COL; c++) {
            for (int r = 0; r < ROW; r++) {
                result[c][r] = input[r][c];
            }
        }
        return result;
    }

    public static void printLines(char[][] input) {
        for (int r = 0; r < input.length; r++) {
            for (int c = 0; c < input[r].length; c++) {
                System.out.print(input[r][c]);
            }
            System.out.println();
        }
    }

    public static char[][] convertToCharArray (ArrayList<ArrayList<Character>> list) {
        char[][] result = new char[list.size()][];
        int outerPos = 0;

        for (ArrayList<Character> line: list) {
            char[] charArray = new char[line.size()];
            int innerPos = 0;
            for (char each: line) {
                charArray[innerPos++] = each;
            }
            result[outerPos++] = charArray;
        }
        return result;
    }

}
