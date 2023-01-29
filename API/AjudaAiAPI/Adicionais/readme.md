Pacotes necessários:
Microsoft.EntityFrameworkCore v7.0.2
Microsoft.EntityFrameworkCore.Proxies v7.0.2
Microsoft.EntityFrameworkCore.Tools v7.0.2
Microsoft.VisualStudio.Web.CodeGeneration.Design v6.0.11
MySql.EntityFrameworkCore v7.0.0

Para scaffolding:
https://dev.mysql.com/doc/connector-net/en/connector-net-entityframework-core-scaffold-example.html
Ferramentas> Gerenciador de Pacotes NuGet> Console do ger. de pacotes
Digitar o seguinte comando:
Scaffold-DbContext "server=;uid=;pwd=;database=" Mysql.EntityFrameworkCore -OutputDir Context -f
Com a string de conexão escondida, usa-se:
	Scaffold-DbContext Name=ConnectionStrings:Railway Mysql.EntityFrameworkCore -OutputDir Context -f

Teste com banco localhost:
	Scaffold-DbContext "server=127.0.0.1;uid=root;pwd=root;database=teste" Mysql.EntityFrameworkCore -OutputDir Context -f

Para API: Criar Controller com açõs do Entity Framework
Selecionar a Model do banco e a classe de contexto
colocar o seguinte codigo na program.cs para liberar injeção de dep.
 // Liberar injeção de dependência
 builder.Services.AddDbContext<TesteContext>();//trocar o nome da context de acordo com a necessidade
