"""Validate supplemental strand lessons and answer references (standard library)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'content/strand-lessons-v1.json').read_text())
assert catalog['schema_version']==1
ids=set()
strands=set()
for item in catalog['lessons']:
    assert item['id'] not in ids
    ids.add(item['id'])
    strands.add(item['strand'])
    assert item['status']=='draft'
    path=ROOT/item['student_lesson']
    keypath=ROOT/item['teacher_key']
    assert path.is_file() and keypath.is_file()
    lesson=path.read_text()
    key=json.loads(keypath.read_text())
    assert key['lesson_id']==item['id']
    assert '## Learn' in lesson and '## Practice' in lesson and '## Reflect' in lesson
    assert len(key['items'])==4
    assert all(entry['correct'] in 'ABCD' and entry['explanation'] for entry in key['items'])
    assert lesson.count('### ') == 4
    assert all(lesson.count(f'**{letter}.**')==4 for letter in 'ABCD')
assert strands=={'quantitative','algebraic','geometry','statistics'}
legacy=json.loads((ROOT/'course.json').read_text())
assert [s['id'] for s in legacy['weeks'][0]['sessions']]==[f'tsi-w01-d{i:02d}' for i in range(1,6)]
print('PASS: four strand lessons, 16 four-option practice questions, distinct draft IDs, intact published week-01 IDs.')
