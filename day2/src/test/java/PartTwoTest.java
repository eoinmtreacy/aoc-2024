import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import core.InputReader;

public class PartTwoTest {
    // @Test
    // public void testSample() {
    //     try {
    //         int[][] input = InputReader.readInputAsInt("src/test/resources/sample.txt");
    //         assertEquals(PartTwo.main(input), 4);
    //     } catch (Exception e) {
    //         e.printStackTrace();
    //     }
    // }
    
    @Test
    public void testTest() {
        try {
            int[][] input = InputReader.readInputAsInt("src/test/resources/test.txt");
            assertEquals(PartTwo.main(input), 2);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testInput() {
        try {
            int[][] input = InputReader.readInputAsInt("src/test/resources/input.txt");
            System.out.println(PartTwo.main(input));
            // 506 too low
            // 519 too low 
            // 549 too high
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
