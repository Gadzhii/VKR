using System;

class ImproperInputValidation
{
    static void Main()
    {
        Console.Write("Enter your age: ");
        string ageInput = Console.ReadLine();
        // Некорректная проверка входных данных: нет проверки на то, что введенное значение является числом
        int age = int.Parse(ageInput);
        Console.WriteLine("Your age is: " + age);
    }
}
