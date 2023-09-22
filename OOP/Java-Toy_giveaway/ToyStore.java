import java.util.ArrayList;
import java.util.List;
import java.util.Random;
class ToyStore {
    private List<Toy> toys = new ArrayList<>();
    private List<Toy> prizeToys = new ArrayList<>();

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void changeWeight(int toyId, double newWeight) {
        for (Toy toy : toys) {
            if (toy.getId() == toyId) {
                toy.setWeight(newWeight);
                break;
            }
        }
    }

    public void drawPrize() {
        double totalWeight = toys.stream().mapToDouble(Toy::getWeight).sum();
        double randomValue = new Random().nextDouble() * totalWeight;

        for (Toy toy : toys) {
            if (randomValue < toy.getWeight() && toy.getQuantity() > 0) {
                prizeToys.add(toy);
                toy.setQuantity(toy.getQuantity() - 1);
                break;
            }
            randomValue -= toy.getWeight();
        }
    }

    public Toy getPrize() {
        if (prizeToys.isEmpty()) {
            return null;
        }

        Toy toy = prizeToys.remove(0);
        PrizeFile.writeToFile(toy.toString());
        return toy;
    }
}
