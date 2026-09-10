## Single-User Play

One human controls their assigned company (or explicitly assigned companies). Ask which example company/assets they want and how many NPCs to include; do not silently force the four-company example. Additional companies must have an explicit human controller or be assigned as autonomous NPCs. Use the default NPC policy unless the human requests another; do not ask them to choose or approve each NPC action. The human confirms setup, rule clarifications, and progression.

## Local Runtime

No game-specific package installation or external data is required. Use an available code-execution tool/runtime for arithmetic, random generation, and ledger checks; check availability before play. If none is available, explain the limitation and ask before installing anything. Do not require network access for gameplay.

Save session checkpoints and an append-only event record in a distinct local directory for this game, keeping previous sessions intact. Report the save location. On resume, load and reconcile the checkpoint before asking for the next pending action. Never overwrite another session or apply game instructions to unrelated coding tasks.
