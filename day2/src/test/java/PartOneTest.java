import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import core.InputReader;

public class PartOneTest {

    @Test
    public void testInputReader () {
        try {
            int[][] input = InputReader.readInputAsInt("src/test/resources/sample.txt");
            assertEquals(input.length, 6);
            assertEquals(input[0].length, 5);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    @Test
    public void testSample() {
        try {
            int[][] input = InputReader.readInputAsInt("src/test/resources/sample.txt");
            assertEquals(PartOne.main(input), 2);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testInput() {
        try {
            int[][] input = InputReader.readInputAsInt("src/test/resources/input.txt");
            System.out.println(PartOne.main(input));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
