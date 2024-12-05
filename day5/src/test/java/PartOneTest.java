import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import core.InputReader;

public class PartOneTest {

    @Test
    public void testInputReader () {
        try {
            ArrayList<ArrayList<int[]>> input = InputReader.readTwoChunks("src/test/resources/sample.txt");
            assertEquals(PartOne.main(input.get(0), input.get(1)), 143);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Test
    public void testInput() {
        try {
            ArrayList<ArrayList<int[]>> input = InputReader.readTwoChunks("src/test/resources/input.txt");
            System.out.println(PartOne.main(input.get(0), input.get(1)));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

