public class PartTwo {
    static int[][] DIRECTIONS = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} }; 
                                        // north east south west -- right turns
    static int ROW;
    static int COL;

    public static int main(char[][] input) {
        ROW = input.length;
        COL = input[0].length;
        int result = 0;

        int[] start = findStart(input);

        for (int r = 0; r < ROW; r++) {
            for (int c = 0; c < COL; c++) {
                char stash = input[r][c];
                input[r][c] = '#';
                if (loops(start[0], start[1], start[2], input)) result++;
                input[r][c] = stash;
            }
        }

        return result;
    }

    private static boolean loops(int r, int c, int idx, char[][] input) {

        boolean[][][] visited = new boolean[ROW][COL][4];

        while(r > -1 && c > -1 && r < ROW && c < COL) {
            if (visited[r][c][idx]) return true;

            visited[r][c][idx] = true;

            int pR = r + DIRECTIONS[idx][0];
            int pC = c + DIRECTIONS[idx][1];

            if (pR > -1 && pC > -1 && pR < ROW && pC < COL) {
                if (input[pR][pC] == '.') {
                    r = pR;
                    c = pC;
                } else {
                    while(input[pR][pC] == '#') {
                        idx = (idx + 1) % 4;
                        pR = r + DIRECTIONS[idx][0];
                        pC = c + DIRECTIONS[idx][1];
                    }
                    r = pR;
                    c = pC;
                }
            } else {
                break;
            }
        }

        return false;
    }

    private static int[] findStart (char[][] input) {
        int idx;
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
                    return new int[]{r,c, idx};
                }
            }
        }
        return new int[] {0,0,0};
    } 

}