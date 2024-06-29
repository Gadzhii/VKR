// Hard-coded credentials in JavaScript
const username = "admin";
const password = "password123";

function authenticate(user, pass) {
    if (user === username && pass === password) {
        console.log("Authentication successful!");
    } else {
        console.log("Authentication failed.");
    }
}

// Example usage
authenticate("admin", "password123");
