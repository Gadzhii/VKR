function safeDisplay(userInput) {
    // Эта строка безопасна, так как используется экранирование
    const safeContent = document.createTextNode(userInput);
    document.body.appendChild(safeContent);
}

const input = "<script>alert('XSS');</script>";
safeDisplay(input);
