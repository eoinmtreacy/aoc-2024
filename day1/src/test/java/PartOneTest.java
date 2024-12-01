import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import core.InputReader;

public class PartOneTest {
    @Test
    public void testSample() {
        try {
            int[][] input = InputReader.readInputAsInt("src/test/resources/sample.txt");
            assertEquals(PartOne.main(input), 11);
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
