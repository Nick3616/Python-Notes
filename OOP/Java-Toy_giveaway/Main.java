public class Main {
    public static void main(String[] args) {
        ToyStore store = new ToyStore();
        store.addToy(new Toy(1, "Медведь", 10, 30.0));
        store.addToy(new Toy(2, "Кукла", 15, 50.0));
        store.addToy(new Toy(3, "Машина", 5, 20.0));

        store.drawPrize();
        Toy prize = store.getPrize();

        System.out.println("Призовая игрушка: " + prize);
    }
}