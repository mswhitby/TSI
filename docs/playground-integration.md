# TSI Math in Ms. Whitby's Playground

## What is available now

One complete curriculum week: student lessons, 50 original questions, teacher guides, an explained key, resource selections, and a printable student packet. Lessons require no account. No authentication, enrollment, saved student progress, or dashboard is implemented in this repository.

## Proposed student experience

1. Open TSI Math from Playground.
2. Sign in with an individual Playground username and password; no GitHub account, Google SSO, or Google Classroom connection is required by this design.
3. Enter a teacher's class code to request membership, or use a teacher-created account already assigned to the class.
4. Open today's assigned 30-minute lesson, submit the independent exit ticket, and see a next step.

The exact credential system still needs implementation and review. Do not imitate username authentication by inventing student email addresses or by placing shared secrets in a public frontend. Class codes authorize enrollment only; they are not student passwords or staff-role grants. Verify roster membership before teachers can access a student's records. Teachers can close or rotate enrollment codes.

## Proposed staff access

| Role | Scope | Actions |
|---|---|---|
| Student | Own records | Complete lessons; review own attempts and feedback |
| Teacher | Assigned class sections | Assign lessons; review approved roster; reset credentials through a secure staff action |
| Counselor | Assigned caseload/cohort | Review progress and official retest status; export authorized records |
| Academic dean | Authorized school cohort | Review aggregates; filter by teacher, section, strand, and retest status |

Staff accounts require explicit approval. Every read/write operation must check identity and scope on the server. A hidden dashboard link is not access control. Preserve existing Playground users and GitHub-based course access when adding a new student sign-in method.

## Proposed progress records

Stable student and section IDs; session ID; item ID; skill ID; attempt timestamp; first response; correctness; hint use; independent/supported status; correction; and lesson completion. Keep first attempts immutable when a student retries. Do not equate opening a resource with completing or understanding it.

Report independent performance and completion separately. Record official CRC score, diagnostic level, and test date in an explicitly separate official-results record with a source and entry date. Do not publish student-level information or credentials in this curriculum repository.

## Suggested first implementation

Add the TSI course reader using `course.json`; support printable lessons immediately. Next, implement the approved non-GitHub account flow and section membership, then save independent exit-ticket attempts. Add teacher reporting before counselor/dean aggregate views. Pilot with one advisory class before wider use. Google Classroom is optional future integration, not a prerequisite.

This document is a design specification, not a claim that these features exist.
