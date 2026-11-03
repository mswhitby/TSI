# Teacher contributions and a schoolwide TSI bank

This is a proposed workflow, not an implemented upload service. The open Playground demo contains sample lessons and a facilitator preview; it has no staff content accounts, uploads, or shared student reporting.

## Two destinations

**My Library:** a teacher's drafts, uploaded files, linked resources, and questions. A teacher can preview and publish a version to assigned sections. Unassigned students and other teachers cannot browse private drafts.

**School Bank:** reviewed materials discoverable by approved school staff. Teachers submit a copy from their library; a designated reviewer can request changes or approve a version. Approval does not automatically assign anything to students. Teachers select or adapt an approved resource for their classes.

## A practical authoring form

1. Choose Lesson, Practice Set, Resource Link, or File.
2. Add a title, estimated minutes, strand, skill tags, prerequisite skills, and student directions.
3. Add content using a simple editor; accept a PDF or supported image/document attachment as a resource. Keep executable HTML and scripts out of uploads.
4. For questions, add answer format, correct answer, explanation, hints, and likely misconceptions. Import from a validated template only after a useful manual editor exists.
5. Add source attribution and permission/reuse information. Link licensed third-party materials unless redistribution is permitted.
6. Preview both student and facilitator views, including a printable option.
7. Save as a private draft, publish to assigned sections, or submit a copy to the school bank.

## Review and versions

Statuses: Draft, Submitted, Changes Requested, Approved, Archived. Review mathematical accuracy, answer-key agreement, clarity, accessibility, timing, skill tags, and source permissions. Reviewer comments stay with the submitted version. Only approved versions appear in school-bank searches.

Copying from the bank creates a separate teacher-owned draft with attribution and a reference to the source version. Publishing changes creates a new immutable version. Existing assignments and student attempts retain the version they used; teachers may explicitly assign a newer version later.

## Permissions and storage

Staff roles are assigned by an administrator, not inferred from a class code. Staff authentication must work without requiring GitHub; the exact credential flow remains to be implemented. All content reads, writes, assignment actions, reviews, and downloads need server-side authorization.

Files belong in protected object storage, with type/size validation, controlled download access, safe preview behavior, and an appropriate upload-scanning process. Draft and key files must not be placed in the public curriculum repository. A class code grants enrollment only. Students see only published material assigned to their approved classes and their own work.

## Suggested records

- Material: owner, type, title, school, strand, skills, estimated minutes, source attribution.
- Version: immutable student content, protected teacher key, attachment references, author, creation timestamp.
- Review: submitted version, reviewer, decision, comments, decision timestamp.
- Assignment: section, published version, instructions, availability/due dates.
- Attempt: student, assignment/version, item, first response, later attempts, support/hint use, timestamps.

## First implementation after the demo

Start with private teacher drafts, resource links/PDFs, simple multiple-choice and numeric questions, student preview, and section assignments. Add school-bank review and copy/adapt next. Build reporting from actual attempts only after student sign-in and roster access are approved and tested. Google Classroom integration is optional; it is not required by this design.
