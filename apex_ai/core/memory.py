from __future__ import annotations
import os
import sqlite3
from pathlib import Path

class MemoryStore:
    def __init__(self, path: str | None = None):
        self.path = Path(path or os.getenv("APEX_DB_PATH", "data/apex.sqlite3"))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path) as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            db.commit()

    def add(self, session_id: str, role: str, content: str) -> None:
        with sqlite3.connect(self.path) as db:
            db.execute("INSERT INTO messages(session_id, role, content) VALUES(?,?,?)",
                       (session_id, role, content))
            db.commit()

    def recent(self, session_id: str, limit: int = 12) -> list[dict[str, str]]:
        with sqlite3.connect(self.path) as db:
            rows = db.execute(
                "SELECT role, content FROM messages WHERE session_id=? ORDER BY id DESC LIMIT ?",
                (session_id, limit),
            ).fetchall()
        return [{"role": r, "content": c} for r, c in reversed(rows)]

    def clear(self, session_id: str) -> None:
        with sqlite3.connect(self.path) as db:
            db.execute("DELETE FROM messages WHERE session_id=?", (session_id,))
            db.commit()
