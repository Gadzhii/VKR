import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class HardCodedCredentialsExample {

    public static void main(String[] args) {
        String dbUrl = "jdbc:mysql://localhost:3306/mydatabase";
        String username = "admin"; // Hard-coded username
        String password = "password123"; // Hard-coded password

        try {
            Connection connection = DriverManager.getConnection(dbUrl, username, password);
            System.out.println("Connected to the database successfully!");
        } catch (SQLException e) {
            System.out.println("Failed to connect to the database.");
            e.printStackTrace();
        }
    }
}
