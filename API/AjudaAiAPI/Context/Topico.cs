using System;
using System.Collections.Generic;

namespace AjudaAiAPI.Context;

public partial class Topico
{
    public int IdTopicos { get; set; }

    public int IdForum { get; set; }

    public int CodUsuario { get; set; }

    public DateTime DataTopico { get; set; }

    public string? Texto { get; set; }

    public virtual Usuario CodUsuarioNavigation { get; set; } = null!;

    public virtual ICollection<Comentario> Comentarios { get; } = new List<Comentario>();

    public virtual Forum IdForumNavigation { get; set; } = null!;
}
