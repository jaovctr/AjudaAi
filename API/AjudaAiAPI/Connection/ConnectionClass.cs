using MySql.Data.MySqlClient;

namespace AjudaAiAPI.Connection
{
    public class ConnectionClass
    {
		//dotnet user-secrets set "ConnectionStrings:Railway" "server=containers-us-west-117.railway.app:8048;dns-srv=true;uid=root;pwd=hPF8hemC7JW6yCHuGGKZ;database=railway"
		string connectionstr = "server=containers-us-west-117.railway.app;port=8048;user id=root;password=hPF8hemC7JW6yCHuGGKZ;database=railway";
                               

        public string Conectar()
        {
			string status = "nothing happened";
			try
			{
				MySqlConnection connection = new MySqlConnection();
				connection.ConnectionString = connectionstr;
				connection.Open();
				status = "connected";
			}
			catch (MySqlException ex)
			{
				status = ex.Message;
				Console.WriteLine(ex.Message);
				throw;
			}


			return status;
        } 
		
    }
}
