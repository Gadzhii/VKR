using System;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter a command to execute:");
        string userInput = Console.ReadLine();

        // Уязвимость CWE-78: выполнение команды без проверки ввода
        Process process = new Process();
        process.StartInfo.FileName = "cmd.exe";
        process.StartInfo.Arguments = "/C " + userInput;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.RedirectStandardOutput = true;
        process.Start();

        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();

        Console.WriteLine("Command output:");
        Console.WriteLine(output);
    }
}
