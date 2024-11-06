# Project Time- FLASK API!

<img src="https://github.com/user-attachments/assets/5415c02e-1632-4f71-a971-005278994605" width="400" alt="flask haha">

> I refuse to apologize for niche video game references.

We've done a LOT with Flask today, gang! To wit, the following tools:

| Function/Method | Description |
|-----------------|-------------|
| `redirect()` | Sends user to a different URL. |
| `url_for("function/alias")` | Auto-fetches the URL for the specified function. |
| `app.add_url_rule("/path","alias",function)` | Alternative to using a decorator; ideal for larger setups where adjusting `/paths` is easier. |
| `request.args` | Grabs any query parameters. |
| `request.form` | Grabs any form data. |
| `request.method` | Retrieves the method of an incoming request. |
| `render_template` | Renders a (typically) HTML file. |
| `make_response` | Creates a response without sending it to the client yet, allowing you to modify it (e.g., add a cookie). |
| `session` | Allows creation of encrypted client-side cookies that the server can edit, read, or remove. **Don't forget `app.secret_key`!** |
| `abort()` | Halts a request and returns an HTTP error code (e.g., `abort(404)` for a 404 error). |
| `Flask-Limiter` | Limits the rate of incoming requests to your app, helping prevent abuse or overload by specifying maximum requests per route. |

**Project Ideas for Class Time**  
Explore any of these tools in a short project of your choosing. You can do anything you like, but here are some ideas:

### 1. TV Show/Movie Quote Project
- **Endpoints**:
  - `endpoint1` → Return a random quote.
  - `endpoint2` → Return all quotes.
    - Use an HTML form or query argument to prompt for a quote to look up.
- **Cookie/Session**:
  - Save username.
  - Save favorite character.
- **Extras**:
  - Assign rate limiting to specific endpoint(s)
  - Set up custom 400 errors!

---

### 2. Data API (Stats) Project
- **Endpoints**:
  - `endpoint1` → Return specific data (e.g., one Pokémon).
  - `endpoint2` → Return general data (e.g., all Pokémon).
    - Use an HTML form or query argument to prompt for a Pokémon name to look up.
- **Cookie/Session**:
  - Save username.
  - Save favorite Pokémon.
- **Extras**:
  - Assign rate limiting to specific endpoint(s)
  - Set up custom 400 errors!
  
---

### 3. Game Project (e.g., Guess the Number, Recommend a Song, RPG Game)
- **Endpoints**:
  - `endpoint1` → Landing page with HTML.
  - `endpoint2` → Display all game data in JSON format.
- **Cookie/Session**:
  - Save username.
  - Save progress in the game.
- **Extras**:
  - Assign rate limiting to specific endpoint(s)
  - Set up custom 400 errors!
