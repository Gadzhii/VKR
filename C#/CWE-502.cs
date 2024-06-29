using System;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;

[Serializable]
public class User
{
    public string Name { get; set; }
    public int Age { get; set; }
}

public class Program
{
    public static void Main()
    {
        byte[] userData = ReceiveUserData();
        User user = Deserialize(userData);
        Console.WriteLine($"User: {user.Name}, Age: {user.Age}");
    }

    public static byte[] ReceiveUserData()
    {
        // В реальном сценарии это могут быть данные, полученные от пользователя
        return new byte[] { /* данные */ };
    }

    public static User Deserialize(byte[] data)
    {
        IFormatter formatter = new BinaryFormatter();
        using (Stream stream = new MemoryStream(data))
        {
            return (User)formatter.Deserialize(stream);
        }
    }
}
