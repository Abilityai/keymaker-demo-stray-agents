---
name: summarize
description: Turn one call transcript in inbox/ into notes/<date>-<client>.md (decisions, actions, questions, client summary).
argument-hint: "<transcript file>"
allowed-tools: [Read, Write, Glob]
user-invocable: true
---

# Summarize

1. Read the transcript. Identify the client and the date from the file name or the first lines.
2. Write `notes/<date>-<client>.md` with four sections: Decisions, Action items (owner, date),
   Open questions, Summary for the client (under 80 words).
3. Never invent. Missing owner = `[OWNER?]`. Missing date = `[DATE?]`.
