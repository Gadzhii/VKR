const { exec } = require('child_process');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Введите директорию: ', (directory) => {
    // Уязвимая строка
    const command = `ls ${directory}`;
    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Ошибка выполнения команды: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout:\n${stdout}`);
    });

    rl.close();
});
