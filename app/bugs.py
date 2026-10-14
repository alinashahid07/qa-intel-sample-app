import os


def bug_active(name: str) -> bool:
    # reads the comma separated list of active bugs from the environment
    active = os.environ.get("INJECT_BUG", "")
    return name in [b.strip() for b in active.split(",") if b.strip()]