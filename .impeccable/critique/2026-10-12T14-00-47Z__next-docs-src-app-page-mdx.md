---
target: docs homepage
total_score: 25
max_score: 40
na_heuristics:
p0_count: 0
p1_count: 2
timestamp: 2026-10-12T14-00-47Z
slug: next-docs-src-app-page-mdx
---
Method: dual-agent (A: 4c63985a-364e-4605-88b6-5637e8548800 · B: fffd7e55-4e83-4199-b972-04417225702a)

## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|------:|-----------|
| 1 | Visibility of System Status | 2 | Progress is surfaced as 0 of 999 modules, but does not provide a useful next step. |
| 2 | Match System / Real World | 3 | The learning-path framing is clear; terms such as ReAct, MCP, and RAG are unexplained. |
| 3 | User Control and Freedom | 3 | Clear navigation choices; no meaningful undo/cancel interaction is needed on this static index. |
| 4 | Consistency and Standards | 3 | Repeated cards and phase structure help, though their treatments and prominence vary. |
| 5 | Error Prevention | 2 | The page does not explain prerequisites or effort before routing learners into tracks. |
| 6 | Recognition Rather Than Recall | 3 | Named phases and destinations aid recognition, but there is no clear resume/continue cue. |
| 7 | Flexibility and Efficiency | 2 | Multiple paths serve different learners, but mobile hides search and there is no direct resume path. |
| 8 | Aesthetic and Minimalist Design | 2 | Repeated entry points and the fixed progress widget compete with the learning path. |
| 9 | Help Users Recognize, Diagnose, and Recover from Errors | 2 | The homepage offers no task-specific recovery/help cue; destination errors would leave this surface. |
| 10 | Help and Documentation | 3 | Search, roadmaps, references, and glossary help, but beginner orientation is thin. |
| **Total** | | **25/40** | **Acceptable** |

## Design Specificity Verdict

**LLM assessment:** The phase sequence, AI-specific syllabus, notebook/quizzes, and reference paths make the page recognizably a curriculum hub. The visual language remains mostly category-standard: a dark gradient hero, badges, stat panel, and repeated card grids could be reused for many learning products. The strongest product-specific opportunity is to make the intended learner journey—not the breadth of the catalog—the organizing idea.

**Deterministic scan:** The source detector ran on `CurriculumHome.tsx` and `HubPage.tsx` and reported one finding: `gray-on-color` at `next-docs/src/components/HubPage.tsx:49` (`text-slate-950` on `bg-sky-400`). This is a false positive for the primary CTA: the rendered foreground/background contrast measured 9.25:1. No source finding was reported in `CurriculumHome.tsx`.

**Browser evidence:** The detector script was injected successfully on the homepage, and its visual labels rendered in the `[Human]` browser tab. Labels included overused Arial/single-font hierarchy, cramped padding, decorative radial glow, low-contrast text, and undersized functional text. Treat these as review signals rather than confirmed violations; the source scan's CTA contrast flag is demonstrably false. The browser also logged 56 React duplicate-child-key errors, including `assignment` and `notebook`; these are runtime implementation warnings, not detector-design findings.

## Overall Impression

The homepage is attractive and its curriculum is thoughtfully grouped, but the first decision is less clear than the content suggests. On mobile, a persistent learning-progress widget physically covers the primary CTA, while the displayed 0-of-999 total makes the curriculum feel larger rather than more approachable. Fix that mobile collision first, then make the beginner path unambiguously dominant.

## What's Working

- “AI Learning Path” and “Start from zero” make the broad purpose and beginner entry point explicit.
- The three curriculum phases create a useful high-level map from foundations to production and specialization.
- Separate agent and cheatsheet shortcuts give returning learners a faster route without removing the sequential curriculum.

## Priority Issues

1. **[P1] The fixed progress widget obscures the mobile primary action.** At a 390×844 viewport, the “Start the curriculum” CTA and `.fixed.bottom-6.right-6` widget overlap. The widget also displays `0 of 999 modules`, despite the hero describing a `35+` core path. This blocks the first action and makes the workload feel intimidating. Hide or collapse the widget on the homepage/mobile, reserve a non-overlapping region, and show a track-level progress total only when it helps the learner choose a next step. **Suggested command:** `/impeccable adapt`.

2. **[P1] The recommended route competes with several parallel entry points.** The hero has three actions; three spotlight cards follow; the phase cards and quick links repeat some destinations. A first-time learner has to decide among starting from zero, viewing roadmaps, agents, cheatsheets, and several phase links before the page states a first milestone. Keep “Start the curriculum” as the sole primary action, label the others as alternatives for experienced learners/reference use, and make the first step obvious. **Suggested command:** `/impeccable clarify`.

3. **[P2] Phase cards ask newcomers to choose among too many topics without context.** Phases 2 and 3 each show five topic links, and terms such as RAG, MCP, and ReAct appear without definitions or prerequisite/effort cues. Show a small number of anchors, name one next milestone, and route the complete sequence through the roadmap. **Suggested command:** `/impeccable clarify`.

4. **[P2] Mobile removes key navigation aids.** At narrow widths, `globals.css` hides `.nextra-search` and `.nextra-toc`; on a deep documentation site this removes search and page-local orientation precisely where navigation space is limited. Restore search through a visible mobile control and expose the TOC as a collapsible panel. **Suggested command:** `/impeccable adapt`.

## Persona Red Flags

- **Jordan, first-timer:** “Start from zero” is reassuring, but Jordan still sees several equally plausible routes and no first milestone, time/effort expectation, or explanation of agent-track acronyms.
- **Casey, mobile user:** At 390×844 the fixed progress/login panel overlaps the primary CTA, and mobile search/TOC are hidden. The first tap is obstructed and the quickest way to locate a topic disappears.
- **Riley, stress-tester:** “35+” in the hero versus “0 of 999 modules” in progress creates conflicting expectations about scope and makes it unclear what counts as a module.

## Cognitive Load

Checklist failures: single focus (three hero actions compete with the beginner route); chunking (phase groups expose four or five topic links); visual hierarchy (the mobile floating widget covers the primary CTA); minimal choices (multiple parallel entry points and five-link phase groups); progressive disclosure (many routes and utilities are presented on one long page). Grouping and working-memory continuity are strong; the page does not require remembering prior-screen information. **5/8 failed — high cognitive load.**

## Emotional Journey

The broad promise creates excitement, and “Start from zero” briefly reassures. The repeated routes and large scope count then introduce uncertainty about where to begin and how much work lies ahead. Returning learners benefit from the shortcuts, but the first-time learner needs a smaller, clearer first win.

## Minor Observations

- The browser overlay flagged the Arial-only typography and limited font hierarchy; the visible page relies heavily on size and weight for distinction. A deliberate display/body pairing could improve identity and scan rhythm.
- “Hot path” may be unfamiliar to newcomers; “Maths” differs from US English spelling used elsewhere.
- The React duplicate-key messages (`assignment`, `notebook`) should be investigated separately; they did not prevent the homepage from rendering during this review.
- No `PRODUCT.md` or design context was present. `/impeccable init` can capture durable audience and product intent before a future visual refinement.

## Questions to Consider

- If a learner has ten minutes, what first result should “Start the curriculum” promise?
- Should progress on the homepage emphasize completed core tracks rather than a 999-page denominator?
- Which mobile navigation aid matters most on this curriculum: persistent search, a collapsible table of contents, or both?
