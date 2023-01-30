using System;
using System.Collections.Generic;

namespace AjudaAiAPI.Context;

public partial class Tag
{
    public int CodTag { get; set; }

    public string Nome { get; set; } = null!;

    public int Recorrencia { get; set; }

    public virtual Atreladum? Atreladum { get; set; }
}
