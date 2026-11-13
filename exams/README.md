# Test Prep subject catalogs

Original illustrative multiple-choice samples for self-study, not copied official exam questions.

- ASVAB: Arithmetic Reasoning, Word Knowledge, Paragraph Comprehension, Mathematics Knowledge. These are the AFQT-related subjects, not the entire ASVAB.
- SAT: Reading and Writing, Math. Actual digital SAT adaptive behavior is not reproduced here.
- ACT: English, Math, Reading, optional Science. This follows the enhanced ACT structure.

The existing TSI course manifest remains at course.json. The full TSI 20-day differentiated curriculum is still unfinished (see docs/IMPLEMENTATION-CONTRACT.md).

## Public authoring contract

1. Keep stable IDs for published exams, subjects and questions.
2. Create each new exam manifest at exams/<exam-id>/track.json, then register it in test-prep.json.
3. Each sample has four answer options, a zero-based correct answer index, and an original explanation. These public keys are for low-stakes practice only, not hidden assessment grading.
4. Never store private assessments, real student information, credentials or official score reports in this repository.
5. Use linked official resources for blueprint updates. Do not copy protected test items.
6. Do not convert sample accuracy directly into AFQT, SAT, ACT or TSIA2 scaled-score predictions.

Validation: python3 scripts/validate_test_prep.py
