using MySql.Data.MySqlClient;

namespace AjudaAiAPI.Connection
{
    public class ConnectionClass
    {
        protected string connectionstr = "server=127.0.0.1;uid=root;pwd=root;database=teste";
		public string Conectar()
        {
			string status = "nothing happened";
			try
			{
				MySqlConnection connection = new MySql.Data.MySqlClient.MySqlConnection();
				connection.ConnectionString = connectionstr;
				connection.Open();
				status = "connected";
			}
			catch (MySql.Data.MySqlClient.MySqlException ex)
			{
				status = ex.Message;
				Console.WriteLine(ex.Message);
				throw;
			}


			return status;
        } 
		
    }
}
