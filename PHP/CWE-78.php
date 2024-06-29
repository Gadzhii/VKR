<?php
if (isset($_POST['directory'])) {
    $directory = $_POST['directory'];
    // Уязвимая строка
    $command = "ls " . $directory;
    echo "<pre>" . shell_exec($command) . "</pre>";
}
?>

<form method="post">
    <label for="directory">Введите директорию:</label>
    <input type="text" id="directory" name="directory">
    <input type="submit" value="List Directory">
</form>
