import java.io.*;

public class VulnerableDeserialization {
    public static void main(String[] args) {
        try {
            // Получение данных для десериализации (может быть из внешнего источника)
            byte[] data = receiveData();
            // Десериализация данных без проверки
            ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(data));
            Object obj = ois.readObject();
            ois.close();
            
            // Использование десериализованного объекта
            if (obj instanceof User) {
                User user = (User) obj;
                System.out.println("User: " + user.getName());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static byte[] receiveData() {
        // Пример данных (в реальной ситуации данные могут поступать из внешнего источника)
        try {
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(baos);
            oos.writeObject(new User("Alice"));
            oos.close();
            return baos.toByteArray();
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}

class User implements Serializable {
    private String name;

    public User(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
