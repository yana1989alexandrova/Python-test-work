import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ToyStore {
    private List<Toy> toys = new ArrayList<>();

    public void addToy(int id, String name, int quantity, double weight) {
        Toy newToy = new Toy(id, name, quantity, weight);
        toys.add(newToy);
    }

    public void updateWeight(int toyId, double newWeight) {
        for (Toy toy : toys) {
            if (toy.getId() == toyId) {
                toy.setWeight(newWeight);
                break;
            }
        }
    }

    public void drawToys(int numToys) {
        if (toys.isEmpty()) {
            System.out.println("В магазине нет игрушек.");
            return;
        }

        double totalWeight = toys.stream().mapToDouble(Toy::getWeight).sum();
        Random random = new Random();

        for (int i = 0; i < numToys; i++) {
            double randomValue = random.nextDouble() * totalWeight;
            double cumulativeWeight = 0;

            for (Toy toy : toys) {
                cumulativeWeight += toy.getWeight();
                if (randomValue <= cumulativeWeight) {
                    if (toy.getQuantity() > 0) {
                        System.out.println("Вы выиграли игрушку: " + toy.getName());
                        toy.setQuantity(toy.getQuantity() - 1);
                        break;
                    } else {
                        System.out.println("Извините, игрушка " + toy.getName() + " закончилась.");
                        break;
                    }
                }
            }
        }
    }
}
