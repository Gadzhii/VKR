import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class ImproperInputValidation {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Введите ваш возраст: ");
        try {
            String ageInput = reader.readLine();
            // Некорректная проверка входных данных: нет проверки на то, что введенное значение является числом
            int age = Integer.parseInt(ageInput);
            System.out.println("Ваш возраст: " + age);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (NumberFormatException e) {
            System.out.println("Неверный формат возраста");
        }
    }
}
