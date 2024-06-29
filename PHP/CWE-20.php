<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    // Получаем параметр 'id' из запроса
    $id = $_GET['id'];

    // Неправильная проверка ввода: проверяется только наличие значения
    if (!empty($id)) {
        // Используем значение параметра 'id' в SQL-запросе без дополнительной проверки
        $query = "SELECT * FROM users WHERE id = $id";

        // Подключение к базе данных
        $conn = new mysqli("localhost", "username", "password", "database");

        // Проверка соединения
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Выполнение запроса
        $result = $conn->query($query);

        // Проверка результатов
        if ($result->num_rows > 0) {
            // Выводим данные пользователя
            while($row = $result->fetch_assoc()) {
                echo "ID: " . $row["id"]. " - Name: " . $row["name"]. " - Email: " . $row["email"]. "<br>";
            }
        } else {
            echo "No results found";
        }

        // Закрываем соединение
        $conn->close();
    } else {
        echo "ID parameter is missing";
    }
}
?>
