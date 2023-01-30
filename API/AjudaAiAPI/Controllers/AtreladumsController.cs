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
    public class AtreladumsController : ControllerBase
    {
        private readonly RailwayContext _context;

        public AtreladumsController(RailwayContext context)
        {
            _context = context;
        }

        // GET: api/Atreladums
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Atreladum>>> GetAtrelada()
        {
            return await _context.Atrelada.ToListAsync();
        }

        // GET: api/Atreladums/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Atreladum>> GetAtreladum(int id)
        {
            var atreladum = await _context.Atrelada.FindAsync(id);

            if (atreladum == null)
            {
                return NotFound();
            }

            return atreladum;
        }

        // PUT: api/Atreladums/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutAtreladum(int id, Atreladum atreladum)
        {
            if (id != atreladum.CodTag)
            {
                return BadRequest();
            }

            _context.Entry(atreladum).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!AtreladumExists(id))
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

        // POST: api/Atreladums
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Atreladum>> PostAtreladum(Atreladum atreladum)
        {
            _context.Atrelada.Add(atreladum);
            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateException)
            {
                if (AtreladumExists(atreladum.CodTag))
                {
                    return Conflict();
                }
                else
                {
                    throw;
                }
            }

            return CreatedAtAction("GetAtreladum", new { id = atreladum.CodTag }, atreladum);
        }

        // DELETE: api/Atreladums/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteAtreladum(int id)
        {
            var atreladum = await _context.Atrelada.FindAsync(id);
            if (atreladum == null)
            {
                return NotFound();
            }

            _context.Atrelada.Remove(atreladum);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool AtreladumExists(int id)
        {
            return _context.Atrelada.Any(e => e.CodTag == id);
        }
    }
}
