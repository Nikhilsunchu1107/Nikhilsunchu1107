# Code Deletion Log

## [2026-11-10] Refactor Session — Dead Code Cleanup

### Unused Functions Removed
- `tools/profile/render.py` — Function: `_shade(hexc, f)`
  - Reason: Defined but never called anywhere in the codebase (confirmed via grep across `tools/`). A pure-Python hex-color shade helper left over from an earlier draft; the contribution city uses inline `ROOFS` colors instead.
  - Verification: `vulture --min-confidence 60` reports no remaining dead code (only 3 fontTools `Options` attributes flagged, which are consumed internally by the library, not dead). `py_compile` passes for all modules. All `test_streaks` tests pass. `render.py` regenerates all 15 SVGs byte-identical to the committed `assets/` output.

### Detection Summary
- Tools used: `ruff check` (unused imports/variables), `vulture` (dead functions/attributes), manual grep for callers.
- Unused imports: none (no F401/F841).
- Unused functions: `_shade` only.
- Commented-out / unreachable code: none.
- Duplicate code blocks: none suitable for consolidation (the recurring glow+solid render pairs in `build_header`/`build_card`/`build_link_button` are intentional visual effects, not accidental duplication).

### Impact
- Files deleted: 0
- Functions removed: 1 (`_shade`)
- Lines removed: 4
- Output change: none (SVGs byte-identical)

### Testing
- `python3 -m py_compile` on all modules: pass
- `tools/profile/tests/test_streaks.py`: all 4 tests pass
- `tools/profile/render.py` regenerates 15 SVGs identical to `assets/`
