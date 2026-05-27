# scripts/

Standalone scripts that run from the command line (no MCP / no Claude needed).

## sync_jobs.py - Bidirectional sync with the "Job Applications" Notion DB

One-time setup:

1. Create a Notion internal integration at https://www.notion.so/profile/integrations
   - Type: Internal
   - Capabilities: Read content, Update content, Insert content
2. Open the **Job Search** page in Notion. Click the `...` menu in the top right -> **Connections** -> search for your new integration and add it. This gives the integration access to the page and its child database.
3. Copy the integration's "Internal Integration Secret".
4. Create a `.env` file in the repo root (already gitignored):

   ```
   NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. Install dependencies:

   ```
   pip install requests python-dotenv
   ```

Daily use:

```bash
# After /job-tracker adds new rows to tracker.md
python scripts/sync_jobs.py push

# After marking statuses in Notion
python scripts/sync_jobs.py pull

# See drift between the two sides without writing
python scripts/sync_jobs.py status
```

Notes:

- Dedup key is the **Link** column. Rows without a link are skipped on push.
- Push only updates a Notion row if at least one field changed.
- Pull regenerates `tracker.md` from scratch, sorted by Date Found (newest first), grouped by status priority. The file's surrounding prose (legend, etc.) is preserved by the template in `write_tracker()`.
- Database ID and data-source ID are hardcoded in the script. If the DB is recreated, update `DATABASE_ID` at the top.

---

## daily_dashboard.py

Generates the morning dashboard. Scheduled via Windows Task Scheduler at 8:30 AM Asia/Jerusalem. See CLAUDE.md for details.
