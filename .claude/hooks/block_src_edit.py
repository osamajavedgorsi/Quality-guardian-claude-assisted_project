import json
import sys
import os

# Read the hook input from stdin
input_data = json.loads(sys.stdin.read())
tool_input = input_data.get('tool_input', {})

# Check if the edit targets a file inside src/
file_path = tool_input.get('file_path', '')
if 'CLAUDE.md' in file_path.replace('\\', '/'):
    # Block the edit
    response = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Direct edits to CLAUDE.md are blocked. Use the CLI or request a specific change."
        }
    }
    print(json.dumps(response))
    sys.exit(0)  # Exit 0 with JSON means "block"

# Allow the edit
response = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow"
    }
}
print(json.dumps(response))
sys.exit(0)