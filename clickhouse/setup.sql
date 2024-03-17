CREATE DATABASE IF NOT EXISTS poc;

CREATE OR REPLACE TABLE poc.events (
    id String,
    timestamp DateTime64,
    data String
) ENGINE = MergeTree()
ORDER BY (id);