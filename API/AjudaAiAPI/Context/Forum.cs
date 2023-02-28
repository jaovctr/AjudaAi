using System;
using System.Collections.Generic;

namespace AjudaAiAPI.Context;

public partial class Forum
{
    public int IdForum { get; set; }

    public virtual ICollection<Topico> Topicos { get; } = new List<Topico>();
}
