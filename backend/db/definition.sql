CREATE TABLE IF NOT EXISTS polls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    type TEXT,
    description TEXT,
    security_key TEXT,
    secure_mode INTEGER,
    num_voters INTEGER,
    date_created DATETIME DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS poll_candidate (
    poll_id INTEGER,
    candidate_id TEXT,
    name TEXT,
    faction TEXT,
    PRIMARY KEY (poll_id, candidate_id)
);

CREATE TABLE IF NOT EXISTS poll_proposal (
    poll_id INTEGER,
    proposal_id INTEGER,
    name TEXT,
    description TEXT,
    PRIMARY KEY (poll_id, proposal_id)
);

CREATE TABLE IF NOT EXISTS votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poll_id INTEGER,
    vote TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);