using System;

class Program
{
    static void Main()
    {
        string str = null;
        int length = str.Length; // Dereferencing a null pointer 'str'
        Console.WriteLine("Length of the string: " + length);
    }
}
