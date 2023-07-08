CREATE TABLE IF NOT EXISTS polls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    type TEXT,
    description TEXT,
    date_created DATETIME DEFAULT current_timestamp,
    last_poll DATETIME
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

CREATE TABLE IF NOT EXISTS poll_voter (
    poll_id INTEGER,
    voter_id TEXT,
    name TEXT,
    vote TEXT,
    PRIMARY KEY (poll_id, voter_id)
);