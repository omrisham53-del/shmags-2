# Work-PC security hook for Claude Code (PreToolUse, matcher = Bash).
#
# Why this exists: the deny rules in settings.json block network/exfiltration
# at the level of named commands (curl, wget, git push, ...). They cannot see
# inside a script. This hook reads the FULL command text Claude is about to run
# and blocks it if it contains any network/exfiltration indicator, even when
# hidden inside something like:  python -c "import requests; requests.post(...)"
#
# How it works: Claude Code pipes the tool call to this script as JSON on stdin.
# Exit code 2 blocks the call and feeds the stderr message back to Claude.
# Exit code 0 lets it through. Any parse error fails open (exit 0) so a malformed
# payload never silently blocks all work.

$ErrorActionPreference = "Stop"

$raw = [Console]::In.ReadToEnd()
if (-not $raw) { exit 0 }

try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$cmd = ""
if ($payload.tool_input -and $payload.tool_input.command) {
    $cmd = [string]$payload.tool_input.command
}
if (-not $cmd) { exit 0 }

# Patterns that have no business running on a machine holding client data.
# Matched case-insensitively against the raw command text.
$blocked = @(
    'curl',
    'wget',
    'invoke-webrequest',
    'invoke-restmethod',
    '\biwr\b',
    '\birm\b',
    'start-bitstransfer',
    'requests\.(get|post|put|patch|delete|request)',
    'urllib',
    'httpx',
    'http\.client',
    'socket\.',
    'smtplib',
    'ftplib',
    'paramiko',
    'webhook',
    'https?://',
    '\bscp\b',
    '\bssh\b',
    '\bsftp\b',
    '\bnc\b',
    'telnet',
    'git\s+push'
)

foreach ($p in $blocked) {
    if ($cmd -imatch $p) {
        [Console]::Error.WriteLine(
            "BLOCKED by work-PC security hook: the command matches the pattern '$p'. " +
            "Network, upload, and push operations are disabled on this machine to keep " +
            "client data local. If this is legitimate, run it yourself in a terminal " +
            "outside Claude Code."
        )
        exit 2
    }
}

exit 0
