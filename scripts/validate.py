"""Validate content and independently recompute numeric answers; no dependencies."""
import ast,json,re
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
def calc(s):
 tree=ast.parse(s,mode='eval')
 def visit(n):
  if isinstance(n,ast.Constant) and type(n.value) in (int,float):return F(ast.get_source_segment(s,n))
  if isinstance(n,ast.UnaryOp) and isinstance(n.op,(ast.UAdd,ast.USub)):return visit(n.operand)*(1 if isinstance(n.op,ast.UAdd) else -1)
  if isinstance(n,ast.BinOp):
   a,b=visit(n.left),visit(n.right)
   if isinstance(n.op,ast.Add):return a+b
   if isinstance(n.op,ast.Sub):return a-b
   if isinstance(n.op,ast.Mult):return a*b
   if isinstance(n.op,ast.Div):return a/b
  raise ValueError('Unsupported arithmetic')
 return visit(tree.body)
def verify(rule,answer):
 kind=rule['kind']
 if kind=='expression':assert calc(rule['expression'])==F(str(answer)),(rule,answer)
 elif kind=='linear_solution':
  a,b,c,d=map(lambda x:F(str(x)),rule['coefficients']);x=F(str(answer))
  assert a!=c and a*x+b==c*x+d,(rule,answer)
 elif kind=='line':
  normalized=answer.replace(' ','').replace('−','-')
  expected=f"y={rule['m']}x{rule['b']:+}"
  assert normalized==expected,(normalized,expected)
 elif kind=='vertical_slope':
  (x1,y1),(x2,y2)=rule['points'];assert x1==x2 and y1!=y2 and answer=='undefined'
 elif kind=='cheaper':
  av=F(str(rule['a'][0]))+F(str(rule['a'][1]))*rule['input'];bv=F(str(rule['b'][0]))+F(str(rule['b'][1]))*rule['input']
  assert answer==('A' if av<bv else 'B' if bv<av else 'equal')
 elif kind=='line_points':assert all(F(str(y))==F(str(answer['m']))*F(str(x))+F(str(answer['b'])) for x,y in rule['points'])
 else:raise ValueError(kind)
def main():
 data=read('content/week-01-student.json');keys=read('teachers/week-01/answers.json')['items'];manifest=read('course.json');seen=set();mc_count=0
 for d in data['days']:
  items=[q for group in ['warmup','guided','practice','exit','check'] for q in d.get(group,[])]
  assert len(items)==10
  if d['day']<5:assert [len(d[g]) for g in ['warmup','guided','practice','exit']]==[2,2,4,2]
  for q in items:
   id=q['id'];assert id not in seen;seen.add(id);a=keys[id]
   assert a['skill_id']==q['skill_id'];assert not any(k in q for k in ['answer','correct','explanation','validation'])
   if q['label'].startswith(('E','Q')):assert 'hint' not in q
   rule=a['validation']
   if q['response_type']=='multiple_choice':
    mc_count+=1;assert [o['label'] for o in q['options']]==list('ABCD')
    assert rule['correct_label']==a['answer'];chosen=next(o for o in q['options'] if o['label']==a['answer'])
    assert set(a['distractor_notes'])==set('ABCD')-{a['answer']}
    verify(rule['calculation'],chosen['value'])
    # Exactly one option must satisfy the published model or arithmetic.
    valid=0
    for o in q['options']:
     try:verify(rule['calculation'],o['value']);valid+=1
     except (AssertionError,ValueError,TypeError,KeyError):pass
    assert valid==1,(id,valid)
   else:verify(rule,a['answer'])
 assert seen==set(keys) and len(seen)==50 and mc_count==10
 assert len(manifest['weeks'][0]['sessions'])==5
 for session in manifest['weeks'][0]['sessions']:
  assert session['minutes']==30 and sum(x['minutes'] for x in session['timing'])==30
  for k in ['student_lesson','teacher_guide']:assert (ROOT/session[k]).is_file()
 resources=read('resources/pearson-selections.json')
 from urllib.parse import urljoin
 for r in resources['resources']:
  raw=r['lrURL'];expected=raw if re.match(r'^https?://',raw) else urljoin(resources['base_url'],raw)
  assert r['resolved_url']==expected and r['source_catalogs']
 # Local Markdown links resolve; external URLs are retained, not availability-checked.
 for p in ROOT.rglob('*.md'):
  for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if not re.match(r'^https?://|^#',link):assert (p.parent/link.split('#')[0]).exists(),(p,link)
 packet=(ROOT/'print/week-01-student-packet.html').read_text()
 assert len(re.findall(r"<section class='page ",packet))==10
 assert 'distractor_notes' not in packet and 'answer-key' not in packet
 print('PASS: 5 sessions × 30 minutes; 50 unique items; all numerical/model answers recomputed; 10 unambiguous multiple-choice keys; local links and resource URL rules verified.')
if __name__=='__main__':main()
