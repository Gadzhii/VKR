using System;

class Program
{
    static void Main()
    {
        // Инициализация переменной maxValue значением максимального допустимого значения для 32-битного целого числа
        int maxValue = int.MaxValue; // maxValue = 2147483647
        
        // Попытка увеличить maxValue на 1, что приведет к переполнению целого числа
        // В результате, значение result станет минимально возможным значением для 32-битного целого числа
        int result = maxValue + 1; // result = -2147483648 (переполнение)

        // Вывод значения переменной result в консоль
        Console.WriteLine("Result: " + result); // Выведет: Result: -2147483648
    }
}
