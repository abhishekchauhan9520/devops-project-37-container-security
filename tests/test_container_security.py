from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
dockerfile = (ROOT / "Dockerfile").read_text()
compose = (ROOT / "docker-compose.yml").read_text()

assert "USER app" in dockerfile
assert "HEALTHCHECK" in dockerfile
assert "--no-cache-dir" in dockerfile

assert "read_only: true" in compose
assert "no-new-privileges:true" in compose
assert "cap_drop:" in compose
assert "- ALL" in compose
assert "pids_limit:" in compose
assert "mem_limit:" in compose
assert "cpus:" in compose
print("Container security assertions passed")
