using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AjudaAiAPI.Context;

namespace AjudaAiAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TopicosController : ControllerBase
    {
        private readonly RailwayContext _context;

        public TopicosController(RailwayContext context)
        {
            _context = context;
        }

        // GET: api/Topicos
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Topico>>> GetTopicos()
        {
            return await _context.Topicos.ToListAsync();
        }

        // GET: api/Topicos/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Topico>> GetTopico(int id)
        {
            var topico = await _context.Topicos.FindAsync(id);

            if (topico == null)
            {
                return NotFound();
            }

            return topico;
        }

        // PUT: api/Topicos/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutTopico(int id, Topico topico)
        {
            if (id != topico.IdTopicos)
            {
                return BadRequest();
            }

            _context.Entry(topico).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!TopicoExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Topicos
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Topico>> PostTopico(Topico topico)
        {
            _context.Topicos.Add(topico);
            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateException)
            {
                if (TopicoExists(topico.IdTopicos))
                {
                    return Conflict();
                }
                else
                {
                    throw;
                }
            }

            return CreatedAtAction("GetTopico", new { id = topico.IdTopicos }, topico);
        }

        // DELETE: api/Topicos/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteTopico(int id)
        {
            var topico = await _context.Topicos.FindAsync(id);
            if (topico == null)
            {
                return NotFound();
            }

            _context.Topicos.Remove(topico);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool TopicoExists(int id)
        {
            return _context.Topicos.Any(e => e.IdTopicos == id);
        }
    }
}
