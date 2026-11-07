# One-month TSI mathematics implementation contract

This is the **replacement** program, not an extension of the prior five-day sample. Target: 20 school days of 30-minute sessions; all four TSIA2 Mathematics strands at **Basic**, **Proficient**, and **Advanced** levels. No content gates.

## Placement

- **TSI study code** `MATH01` through `MATH81` maps to four independent levels in `content/math-locator-profiles.json`. The workbook uses a base-three code sequence with Statistics changing fastest.
- **Teacher placement** may override the recommended level or starting lesson.
- **Diagnostic** offers an alternative recommendation. Placement and enrollment are distinct concepts.
- Show **Recommended for you** first and a visible **Browse all** expansion listing every strand, unit, lesson, and level. Every lesson can be opened regardless of recommendation.

## Lesson experience

For each scheduled topic and each of the three levels, author (a) a short prerequisite check, (b) a step-by-step worked **Learn** example, (c) four independently authored **Practice** items with four answer options each, (d) explanation for every answer and common mistake, and (e) an exit check. Scaffold complexity changes by level, not just the numbers. Use the Pearson workbook to link directly to appropriate videos, PDFs and interactives. Never copy copyrighted resource content.

## One-month class flow

Days 1–20 are listed in `content/20-day-program.json`. Day 1 is a placement/diagnostic day. Days 5, 10, 15 and 19 are checkpoints or reassessments; Day 20 is an independent mixed review/simulation. The 30-minute classroom schedule is a suggested pacing framework, **not** an access restriction.

## Assessment and progress

Learn and Practice may show feedback immediately. Simulation must hide answers and explanations until the attempt is submitted, disallow in-attempt backtracking where the assessment contract requires it, and respect item-specific calculator settings. Preserve first attempts separately from retries. Student history and earned points persist across curriculum replacement; retired published IDs must not be reused.

## Publication readiness

The four sample lessons in `lessons/strands` are **not a complete curriculum**. The program is not ready for student release until all strand-level lessons and assessments are authored, content is validated, and the actual Playground student and teacher interfaces are integrated. Curriculum work belongs to `mswhitby/TSI`; authentication, grading, and data persistence belong to `mswhitby/playground`. Do not publish teacher keys as hidden grading tests.
