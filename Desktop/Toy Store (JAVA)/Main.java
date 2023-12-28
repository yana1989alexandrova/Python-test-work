public class Main {
    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();

        toyStore.addToy(1, "Кукла", 10, 30);
        toyStore.addToy(2, "Машинка", 15, 20);
        toyStore.addToy(3, "Мяч", 20, 50);

        toyStore.updateWeight(2, 10); // Изменение веса для игрушки "Машинка"

        toyStore.drawToys(3); // Розыгрыш трех игрушек
    }
}
