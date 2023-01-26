using AjudaAiAPI.Connection;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AjudaAiAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ConnectionController : ControllerBase
    {       
        [HttpGet]
        public async Task<ActionResult<object>> TestarConexao()
        {
            ConnectionClass c = new ConnectionClass();

            return c.Conectar();
        }
    }
}
