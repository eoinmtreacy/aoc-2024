import java.util.Arrays;
import java.util.List;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class PartTwo {
    static int[][] DIRECTIONS = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} }; 
                                        // north east south west -- right turns
    static boolean[][] obstacles;
    static int idx;
    static int ROW;
    static int COL;
    static int[] pos;

    public static int main(char[][] input) {
        ROW = input.length;
        COL = input.length;
        findStart(input);
        boolean [][] visited = new boolean[ROW][COL];
        int result = 0;

        while(pos[0] > -1 && pos[1] > -1 && pos[0] < ROW && pos[1] < COL) {
            // System.out.println(pos[0] + " " + pos[1]);
            // if (visited[pos[0]][pos[1]] == false) {
            //     result++;
            //     visited[pos[0]][pos[1]] = true;
            // }

            if (loops(pos[0], pos[1], idx, input)) result++;

            int dR = DIRECTIONS[idx][0];
            int dC = DIRECTIONS[idx][1];
            int r = pos[0] + dR;
            int c = pos[1] + dC;
            if (r > -1 && c > - 1 && r < ROW && c < COL) {
                if (input[r][c] == '.') {
                    pos[0] += dR;
                    pos[1] += dC;
                } else {
                    while(input[r][c] == '#') {
                        idx = (idx + 1) % 4;
                        dR = DIRECTIONS[idx][0];
                        dC = DIRECTIONS[idx][1];
                        r = pos[0] + dR;
                        c = pos[1] + dC;
                    }
                    pos[0] += dR;
                    pos[1] += dC;
                }
            } else break;
        }

        return result;
    }

    private static boolean loops(int r, int c, int idx, char[][] input) {
        System.out.println("Checking "  + r + " " + c + " " + DIRECTIONS[idx][0] + " " + DIRECTIONS[idx][1]);
        boolean [][][] visited = new boolean[ROW][COL][4];
        visited[r][c][idx] = true;
        idx = (idx + 1) % 4;

        while(r > - 1 && c > -1 && r < ROW && c < COL) {
            System.out.println("moving "  + r + " " + c + " " + DIRECTIONS[idx][0] + " " + DIRECTIONS[idx][1]);
            if (visited[r][c][idx]) return true;

            visited[r][c][idx] = true;

            int dR = DIRECTIONS[idx][0];
            int dC = DIRECTIONS[idx][1];
            int pR = r + dR;
            int pC = c + dC;
            if (pR > -1 && pC > - 1 && pR < ROW && pC < COL) {
                if (input[pR][pC] == '.') {
                    r = pR;
                    c = pC;
                } else {
                    while(input[pR][pC] == '#') {
                        idx = (idx + 1) % 4;
                        pR = r + DIRECTIONS[idx][0];
                        pC = c +  DIRECTIONS[idx][1];
                    }
                    r = pR;
                    c = pC;
                }
            } else break;
        }

        return false;
    }

    private static void findStart (char[][] input) {
        for (int r = 0; r < ROW; r++) {
            for (int c = 0; c < COL; c++) {
                char tile = input[r][c];
                if (tile != '.' && tile != '#') {
                    if (tile == '^') {
                        idx = 0;
                    } else if (tile == '>') {
                        idx = 1;
                    } else if (tile == 'v') {
                        idx = 2;
                    } else {
                        idx = 3;
                    }
                    pos = new int[]{r,c};
                }
            }
        }

    } 

}