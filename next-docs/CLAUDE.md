<!-- BEGIN:nextjs-agent-rules -->
# Claude Workspace Notes

This app uses Next.js with repo-specific constraints. Start with `AGENTS.md` in this folder, then follow the framework guidance from `node_modules/next/dist/docs/` before making code changes.

Key points:

- Treat `jupyter-notebooks/` as the source of truth for curriculum content and `next-docs/src/app/` as generated or synchronized presentation content.
- Keep generated artifacts such as `.next/`, `out/`, and `*.tsbuildinfo` out of commits.
- Prefer small changes that preserve existing routing, sidebar generation, and notebook sync behavior.

`AGENTS.md` is the primary instruction file for this app directory.
<!-- END:nextjs-agent-rules -->
