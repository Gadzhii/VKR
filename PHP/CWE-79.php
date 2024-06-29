<?php
// Получаем пользовательский ввод
$user_input = $_GET['input'];

// Отображаем пользовательский ввод без какой-либо фильтрации или экранирования
echo "User input: " . $user_input;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vulnerable Page</title>
</head>
<body>
    <form method="get" action="">
        <label for="input">Enter some text:</label>
        <input type="text" id="input" name="input">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
