import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

import core.InputReader;

public class PartTwoTest {

    @Test
    public void testSample () {
        try {
            char[][] input = InputReader.readInput("src/test/resources/sample.txt");
            assertEquals(PartTwo.main(input), 6);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testInput() {
        try {
            char[][] input = InputReader.readInput("src/test/resources/input.txt");
            System.out.println(PartTwo.main(input));
            // 1413 too high
            // 1398 too high
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

