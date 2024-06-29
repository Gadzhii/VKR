<?php
// Hard-coded credentials in PHP
$username = "admin";
$password = "password123";

function authenticate($user, $pass) {
    global $username, $password;
    if ($user === $username && $pass === $password) {
        echo "Authentication successful!";
    } else {
        echo "Authentication failed.";
    }
}

// Example usage
authenticate("admin", "password123");
?>
