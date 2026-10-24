"""MCP server for CQRS Read-Model Projector."""
import sys
import json
from client import CQRSReadModelProjector

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "project_cqrs_read_model",
                "description": "Transforms mutation events into denormalized read view with invalidation tags",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "events": {"type": "array"}
                    },
                    "required": ["events"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "project_cqrs_read_model":
            events = params.get("arguments", {}).get("events", [])
            res = CQRSReadModelProjector.project_and_invalidate(events)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
