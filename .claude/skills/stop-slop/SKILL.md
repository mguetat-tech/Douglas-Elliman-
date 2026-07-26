---
name: stop-slop
description: Engineering discipline checklist to avoid AI-generated code slop in this repo — unnecessary abstractions, dead code, padded comments, defensive checks for impossible states. Use before finishing any code change to index.html, assistant.html, estimation.html, or netlify/functions/claude.js, or whenever the user says "no slop", "keep it clean", or asks for a review of a diff's quality.
---

# Stop Slop

This repo is a small, hand-rolled static site (three HTML files with inline
`<style>`/`<script>`, one Netlify function). It has no build step, no framework,
no test suite. That means there's nothing to catch bloat except a second look
before committing. Run this checklist on every diff before calling a change done.

## Reject on sight

- **New abstractions for one caller.** A helper function, config object, or
  "manager" used from exactly one place is slop — inline it. Three similar
  `document.getElementById(...).value` lines are fine; a `getFieldValue(id)`
  wrapper around them is not.
- **Comments that restate the code.** `/* loop over posts */` above a loop that
  obviously loops over posts adds nothing. Only comment a non-obvious *why*
  (e.g. the Safari surrogate-pair fix in `assistant.html`'s `fixSurrogates`,
  or the "URL absolue" fix for Safari's `getApiUrl` — those are real gotchas
  worth flagging; most lines aren't).
- **Dead code and commented-out blocks.** Delete, don't comment out. Git has
  the history.
- **Defensive checks for states that can't happen.** This is client-side code
  talking to one Netlify function with a fixed payload shape — don't add
  `typeof x === 'undefined'` guards or try/catch around code paths that can't
  throw. Validate only real boundaries: user form input before sending, and
  the fetch response in `netlify/functions/claude.js` (untrusted network I/O).
- **Backwards-compat shims.** There's no external consumer of this code.
  Renaming an id/function means updating every reference, not keeping an
  alias around.
- **Feature flags or config knobs nobody asked for.** If a post-generation
  option isn't wired to a UI control, it doesn't belong.
- **Copy-pasted blocks across the three HTML files instead of noticing the
  duplication.** `index.html`, `assistant.html`, and `estimation.html` already
  share header/footer markup and CSS variables by convention — match the
  existing pattern (same `--navy`/`--teal`/etc. custom properties, same class
  names) rather than inventing a parallel styling scheme for a new page.

## Before finishing, check the diff for

1. Every new function/variable has more than one real use, or is trivially
   short enough that a wrapper would be longer than the code it replaces.
2. No comment could be deleted without losing information a reader needs.
3. Nothing was left half-wired (a button with no handler, a KB fact with no
   corresponding UI field, an env var read but never used).
4. Generated marketing copy (see the `marketing` skill) reads as specific and
   earned, not generic filler — the same "no slop" bar applies to prose, not
   just code. Reject `belle opportunité`-style padding same as you'd reject a
   pointless wrapper function.
5. The change is the smallest diff that satisfies the actual request — no
   drive-by refactors of surrounding code that wasn't asked about.
