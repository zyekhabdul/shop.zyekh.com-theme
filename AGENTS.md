# AGENTS.md — Storefront Theme Instructions (`shop.zyekh.com-theme`)

## Mandatory AI Execution Workflow

Every AI agent working in this repository MUST strictly follow the 6-step execution workflow:
`PRD → Plan/Breakdown → Review Plan → Incremental Implementation → Automated Verification → Human Review Checkpoint`

Reference: `/home/fuckadmin/Documents/Obsidian Vault/09-Panduan-Projek/WORKFLOW-AI-AGENT-STANDARD.md`

## Safety Rails & Guidelines

- **Vanilla CSS & Liquid**: Use standard Liquid tags and Vanilla CSS. Do not add TailwindCSS or unnecessary npm dependencies without explicit user request.
- **Verification**: Run `shopify theme check` or syntax checks before completing tasks.
- **Git Control**: `git commit` is permitted for local checkpoints. `git push` is strictly prohibited without explicit user prompt.
