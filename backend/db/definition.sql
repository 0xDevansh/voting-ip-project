CREATE TABLE IF NOT EXISTS polls (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    type TEXT,
    description TEXT,
    date_created DATETIME DEFAULT current_timestamp,
    last_poll DATETIME
);

CREATE TABLE IF NOT EXISTS candidates (
    id TEXT PRIMARY KEY,
    name TEXT,
    faction TEXT
);

CREATE TABLE IF NOT EXISTS proposals (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS poll_candidate (
    poll_id INTEGER,
    candidate_id TEXT
);

CREATE TABLE IF NOT EXISTS poll_proposal (
    poll_id INTEGER,
    proposal_id INTEGER
);

CREATE TABLE IF NOT EXISTS voters (
    id TEXT PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS poll_voter (
    poll_id INTEGER,
    voter_id TEXT,
    vote TEXT
);