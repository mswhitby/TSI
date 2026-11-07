# TSI Math Advisory

Five 30-minute sessions for seniors preparing to retake TSIA2 Mathematics. Math teachers facilitate the lessons. This repository supplies curriculum for a future TSI Math section of **Ms. Whitby's Playground**.

## Start with the sample week

**Week 1: Percents and linear relationships** develops one connected set of foundational skills. It is not a complete TSIA2 review; geometry, statistics, probability, and nonlinear algebra need later weeks.

| Session | Focus | Student materials | Teacher materials |
|---|---|---|---|
| 1 | Percents in everyday decisions | [Lesson](lessons/week-01/day-01-percents.md) | [Facilitator guide](teachers/week-01/day-01.md) |
| 2 | Solve and check linear equations | [Lesson](lessons/week-01/day-02-equations.md) | [Facilitator guide](teachers/week-01/day-02.md) |
| 3 | Connect slope, tables, and equations | [Lesson](lessons/week-01/day-03-slope.md) | [Facilitator guide](teachers/week-01/day-03.md) |
| 4 | Build and compare linear models | [Lesson](lessons/week-01/day-04-models.md) | [Facilitator guide](teachers/week-01/day-04.md) |
| 5 | Independent weekly check and corrections | [Practice check](lessons/week-01/day-05-check.md) | [Facilitator guide](teachers/week-01/day-05.md) |

- [Complete printable student packet](print/week-01-student-packet.html): download and open in a browser, then Print. Contains all five sessions and workspace, with no teacher key.
- [Week overview](teachers/week-01/overview.md), [explained answer key](teachers/week-01/answer-key.md), and [progress recording template](tracking/week-01-template.csv).
- [Pearson resource selections and provenance](resources/README.md).

Students do not need GitHub accounts to use teacher-distributed printouts or downloaded lesson files. GitHub hosts the curriculum, not student accounts. The open Playground demo provides browser-only practice; signup, class-code enrollment, and a school dashboard are not implemented.

### Playground demo

The curriculum is also packaged into the [open TSI Math Playground demo](https://www.mswhitby.com/playground/#/course/tsi-math), with interactive practice, browser-only first/latest check results, and a [facilitator preview](https://www.mswhitby.com/playground/#/course/tsi-math/teacher). No login is required. Signup, class-code enrollment, teacher uploads, and schoolwide reporting remain unimplemented. See the [teacher contribution proposal](docs/teacher-content-bank.md) for personal libraries and a reviewed school bank.

## How to run it

Sessions 1–4: 3 minutes retrieval, 7 minutes instruction, 12 minutes supported practice, 5 minutes independent exit ticket, and 3 minutes reflection. The supported-practice block starts with two guided problems followed by four independent problems. Optional extensions are outside the required work.

Session 5: 2 minutes directions, 18 minutes for the 10-item check, 7 minutes for corrections after collecting first attempts, and 3 minutes to select a next step. This is a classroom planning limit, not a simulation of TSIA2 timing. Adjust classroom pacing for students' established accommodations.

Each lesson has original worked examples and questions. Teachers can teach entirely from the packet; external videos and interactives are optional supplements. Show reasoning on paper. A basic calculator may be used after setting up an equation; this classroom policy does not reproduce the official test's item-specific calculator availability.

## Interpreting the results

Record first-attempt exit-ticket scores separately from supported practice and corrections. The Week 1 check measures this week's skills, not overall college readiness. Do not convert its percentage, Pearson resource count, or a MATH locator code into a predicted official TSIA2 score.

Math college readiness is CRC 950 or higher, or CRC below 950 with Diagnostic Level 6. The computer-adaptive assessment depends on the questions administered and the responses, rather than a universal number-correct passing rule. See [College Board's score guide](https://accuplacer.collegeboard.org/accuplacer/pdf/tsia2-interpreting-your-scores.pdf) and [technical manual](https://accuplacer.collegeboard.org/accuplacer/pdf/tsia2-technical-manual.pdf).

## Content and future Playground integration

- `course.json`: ordered week/session manifest with stable activity IDs and timings.
- `content/week-01-student.json`: student-facing content, problems, worked examples, and hints. No answer-key fields.
- `teachers/week-01/answers.json`: correct answers, explanations, skill tags, and independent numerical checks.
- `lessons/`: generated readable Markdown lessons, canonical content authored in the student JSON.
- `teachers/`: facilitator guides and explained key. These are authoring materials, not access-protected assessment secrets.
- `resources/pearson-selections.json`: captured Pearson fields, source catalogs, and resolved URLs.
- `docs/playground-integration.md`: proposed account, class, and reporting design; implementation status is explicit.

The repository is public. Keep student names, credentials, official score reports, and completed progress files outside it. Teacher keys are visible in repository source; a later secure assessment service must keep scoring and role checks on the server.

## Build and validate

Requires Python 3. No external packages are needed.

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

The build regenerates student Markdown, the printable HTML packet, and the teacher answer key from the two JSON files. Validation checks activity IDs, timing, exact rational arithmetic for numerical answers, equation substitutions, multiple-choice keys, manifest references, resource URL handling, and separation of student data from teacher keys.

## Sources and reuse

All authored lesson prose, worked examples, questions, and teacher explanations are original companion materials. Pearson resources remain linked with their original identifiers and metadata; no Pearson PDF, video, or interactive is copied here. Topic alignment uses [College Board's Mathematics Test Specifications](https://accuplacer.collegeboard.org/accuplacer/pdf/tsia2-mathematics-test-specifications.pdf), particularly the CRC content descriptions. This is an independent instructional project, not an official College Board or Pearson assessment.

## Four-strand content expansion (draft)

Four new original lessons are now authored in `lessons/strands/` and indexed in `content/strand-lessons-v1.json`: unit rates/proportions, factoring quadratics, right triangles/area, and data summaries/probability. Each has a guided worked example and four multiple-choice practice questions; explained instructional keys are in `teachers/strands/`. These files are **draft curriculum**, not yet included in `course.json` or the live Playground build. Published Week 1 IDs, order, student progress, and points remain unchanged.

Run `python3 scripts/validate_strands.py` for structural checks and `python3 scripts/validate.py` for existing Week 1 checks. The new answer explanations require teacher editorial review before publication; these are not protected grading tests. More lessons are needed for complete TSIA2 coverage.
