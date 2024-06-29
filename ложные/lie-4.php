<?php
function safe_echo($data) {
    // Эта строка безопасна, так как используется функция htmlspecialchars для экранирования вывода
    echo htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
}

$user_input = "<script>alert('XSS');</script>";
safe_echo($user_input);
?>
