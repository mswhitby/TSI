# Test Prep repository migration — proposal, 2026-11-13

**Review branch only. No production deploy or repository rename has occurred.**

## Target

Evolve the existing mswhitby/TSI repository into mswhitby/test-prep, preserving Git history, TSI files and all published IDs.

The legacy course.json identifier must remain tsi-math even if the GitHub repository name changes. Keep the 20-day TSI work in its present paths. The new test-prep.json is a separate top-level multi-exam manifest.

## New files

- test-prep.json — registry of TSI, ASVAB, SAT and ACT
- exams/asvab/track.json — 4 AFQT-related subjects, original examples
- exams/sat/track.json — Reading and Writing; Math
- exams/act/track.json — English, Math, Reading and optional Science
- scripts/validate_test_prep.py — extra catalog validation, independent of existing TSI checks

## Safe sequence

1. Review the curriculum branch; validate new catalogs alongside existing TSI scripts.
2. Adapt central Playground content packaging, GitHub CI checkout references and provenance to support the future repository name and new manifest, while preserving historical TSI paths and IDs.
3. Replace temporary React-preview sample copies with the new source manifest and validated packaged student-safe files.
4. Once integration is approved, rename the GitHub repository via GitHub Settings from TSI to test-prep. Old URLs may redirect, but CI and documentation references should be updated explicitly.
5. Publish only after verified tests, permission checks and preview review.

This is formative content, not full exams, official practice tests or standardized score predictors. The 20-day TSI replacement is still incomplete. React Test Prep hub is being reviewed in mswhitby/playground-react draft PR #11, separately from real student data.
