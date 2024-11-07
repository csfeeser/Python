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

**Project Ideas for Class Time**  
Explore any of these tools in a short project of your choosing. You can do anything you like, but here are some ideas:

### 1. [TV Show/Movie Quote Project](https://thesimpsonsquoteapi.glitch.me/)
- **Endpoints**:
  - `endpoint1` → Return a random quote.
  - `endpoint2` → Return all quotes.
    - Use an HTML form or query argument to prompt for a quote to look up.
- **Cookie/Session**:
  - Save last selected character.
- **NEW**: Integrate a **SQLite3 database** to store favorite quotes or characters persistently across sessions.
- **NEW**: Apply **rate limiting** on the quote lookup endpoints to prevent abuse.
- **NEW**: Create a **custom 400 error page** that displays when a quote lookup fails.
- **NEW**: Use **Jinja2 templates** to style the HTML pages dynamically, showing stored quotes or search results.
- **NEW**: Add **file upload/download functionality** where users can upload their favorite quotes in a file format, which the app can parse and display.

---

### 2. [Data API Project](https://anapioficeandfire.com/)
- **Endpoints**:
  - `endpoint1` → Return specific data (e.g., one Pokémon).
  - `endpoint2` → Return general data (e.g., all Pokémon).
    - Use an HTML form or query argument to prompt for a Pokémon name to look up.
- **Cookie/Session**:
  - Save last searched Pokémon.
- **NEW**: Add **SQLite3** to store frequently searched Pokémon data for quicker access and offline availability.
- **NEW**: Implement **rate limiting** on searches to prevent excessive requests to the API.
- **NEW**: Include a **custom 400 error** for invalid or missing Pokémon searches.
- **NEW**: Use **Jinja2 templates** to format results more attractively and dynamically.
- **NEW**: Allow users to **upload a file** containing a list of Pokémon names to batch search and display all results at once.

---

### 3. [Game Project (e.g., Guess the Number, Trivia, etc.)](https://opentdb.com/api_config.php)
- **Endpoints**:
  - `endpoint1` → Landing page with HTML form to prompt for the answer to a question.
  - `endpoint2` → Displays if the user's guess was correct or not.
  - `endpoint3` → Display all game data in JSON format.
- **Cookie/Session**:
  - Save question guess.
- **NEW**: Use an **SQLite3 database** to store question/answer data, tracking user attempts and high scores.
- **NEW**: Set up **rate limiting** on the question attempts to ensure fair play.
- **NEW**: Create a **custom 400 error page** for invalid question submissions or answers.
- **NEW**: Use **Jinja2 templates** to build an interactive scoreboard and display user stats.
- **NEW**: Add an option for users to **upload trivia questions** in a file format (e.g., CSV), which the app can parse and incorporate into the game dynamically.
