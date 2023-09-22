import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

class PrizeFile {
    private static final String FILE_NAME = "prizes.txt";

    public static void writeToFile(String prize) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME, true))) {
            writer.write(prize);
            writer.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
