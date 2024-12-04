import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import core.InputReader;

public class PartTwoTest {

    @Test
    public void testInputReader () {
        try {
            char[][] input = InputReader.readInput("src/test/resources/sample.txt");
            assertEquals(PartTwo.main(input), 9);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testInput() {
        try {
            char[][] input = InputReader.readInput("src/test/resources/input.txt");
            System.out.println(PartTwo.main(input));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
