using System;
using System.Data.SqlClient;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter your username:");
        string username = Console.ReadLine();
        
        string connectionString = "Data Source=server;Initial Catalog=database;User ID=user;Password=password";
        string query = "SELECT * FROM Users WHERE Username = @username";

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            SqlCommand command = new SqlCommand(query, connection);
            command.Parameters.AddWithValue("@username", username);
            connection.Open();
            SqlDataReader reader = command.ExecuteReader();
            
            if (reader.HasRows)
            {
                Console.WriteLine("User found!");
            }
            else
            {
                Console.WriteLine("User not found.");
            }
            
            reader.Close();
        }
    }
}
