using System;
using System.Collections.Generic;

namespace AjudaAiAPI.Context;

public partial class Atreladum
{
    public int CodTag { get; set; }

    public int CodDemanda { get; set; }

    public virtual Demandum CodDemandaNavigation { get; set; } = null!;

    public virtual Tag CodTagNavigation { get; set; } = null!;
}
