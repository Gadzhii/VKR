using System;
using System.IO;

public class Program
{
    public static void Main()
    {
        // Пример небезопасного кода с уязвимостью CWE-22 (Path Traversal)
        string directory = "/var/www/uploads/";
        string userInput = "../../../../../etc/passwd";

        string fullPath = Path.Combine(directory, userInput);

        try
        {
            // Проверка существования файла по введенному пользователем пути
            if (File.Exists(fullPath))
            {
                // Операции с файлом, если он существует
                Console.WriteLine($"Файл {fullPath} найден.");
            }
            else
            {
                Console.WriteLine($"Файл {fullPath} не найден.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка: {ex.Message}");
        }
    }
}
