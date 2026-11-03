"""Build readable lessons and print files from the authored JSON. Standard library only."""
import json, html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
def esc(s):return html.escape(str(s))
def item_md(q):
 text=f"**{q['label']}.** {q['prompt']}\n"
 for o in q.get('options',[]):text+=f"\n- {o['label']}. {o['text']}"
 if q.get('hint'):text+=f"\n\n<details><summary>Optional practice hint</summary>\n\n{q['hint']}\n\n</details>"
 return text+'\n\nWork / answer: __________________________________________\n'
def item_html(q):
 opts=''.join(f"<li>{esc(o['label'])}. {esc(o['text'])}</li>" for o in q.get('options',[]))
 return f"<div class='question'><p><b>{esc(q['label'])}.</b> {esc(q['prompt'])}</p>"+(f"<ul class='options'>{opts}</ul>" if opts else '')+"<div class='workspace' aria-label='Space for written work'></div></div>"
def header(d,part):return f"<header><p class='eyebrow'>MS. WHITBY’S PLAYGROUND · TSI MATH · WEEK 1</p><h1>Day {d['day']}: {esc(d['title'])}</h1><p>{esc(part)}</p><p class='identity'>Name __________________________ Class __________ Date __________</p></header>"
def section(title,items):return f"<h2>{esc(title)}</h2><div class='grid'>"+''.join(item_html(q) for q in items)+'</div>'
def main():
 data=read('content/week-01-student.json');key=read('teachers/week-01/answers.json')['items'];pages=[];key_md=['# Week 1 explained answer key','Teacher reference. Record first attempts before giving explanations. Corrections are separate evidence.','']
 for d in data['days']:
  md=[f"# Day {d['day']}: {d['title']}",'',f"**Goal:** {d['goal']}",'','Name: ____________________ Class: __________ Date: __________','']
  if d['day']<5:
   md+=['**30-minute plan:** Retrieval 3 min · Mini-lesson 7 min · Guided/practice 12 min · Exit 5 min · Reflection 3 min.','','## Retrieval — 3 minutes','']
   md += [item_md(q) for q in d['warmup']]
   md+=['## Mini-lesson — 7 minutes','']+d['mini_lesson']+['','### Worked examples','']
   for e in d['examples']:md += [f"**{e['prompt']}**",'']+[f"{i+1}. {s}" for i,s in enumerate(e['steps'])]+['']
   md+=['## Guided and independent practice — 12 minutes','','Start G1–G2 with your teacher, then try P1–P4. Show a setup. Hints are optional practice support.','']
   md += [item_md(q) for q in d['guided']+d['practice']]
   md+=['## Independent exit ticket — 5 minutes','','Work without hints or examples until your teacher records your first attempt.','']+[item_md(q) for q in d['exit']]
   md+=['## Reflection — 3 minutes','',d['reflection'],'','________________________________________________________']
   mini=''.join(f'<p>{esc(s)}</p>' for s in d['mini_lesson'])
   examples=''.join('<article class="example"><h3>'+esc(e['prompt'])+'</h3><ol>'+''.join(f'<li>{esc(s)}</li>' for s in e['steps'])+'</ol></article>' for e in d['examples'])
   pages.append(f"<section class='page teaching'>{header(d,'Learn and try together · Page 1 of 2')}{section('Retrieval · 3 minutes',d['warmup'])}<h2>Mini-lesson · 7 minutes</h2>{mini}<div class='grid examples'>{examples}</div>{section('Guided practice · Start the 12-minute practice block',d['guided'])}</section>")
   pages.append(f"<section class='page practice'>{header(d,'Independent practice and exit ticket · Page 2 of 2')}{section('Practice · Complete the 12-minute practice block',d['practice'])}<div class='exit'><h2>Independent exit ticket · 5 minutes</h2><p>Complete without hints. Your teacher records the first attempt before review.</p><div class='grid'>"+''.join(item_html(q) for q in d['exit'])+f"</div></div><h2>Reflection · 3 minutes</h2><p>{esc(d['reflection'])}</p><div class='reflection-space'></div></section>")
   groups=[('Retrieval',d['warmup']),('Guided practice',d['guided']),('Practice',d['practice']),('Exit ticket',d['exit'])]
  else:
   md+=['**30-minute plan:** Directions 2 min · Independent check 18 min · Corrections 7 min · Reflection 3 min.','','This classroom check covers this week’s skills. It is not an official TSIA2 test or a score predictor. Choose one answer for each item and show your setup. Follow your teacher’s classroom calculator directions.','']
   md += [item_md(q) for q in d['check']]
   md+=['## Corrections — after first attempts are collected','',d['reflection'],'','Original thinking: ________________________________________','','Correction and reason: ___________________________________','','Next skill to practice: ___________________________________']
   for index in range(2):
    questions=d['check'][index*5:index*5+5]
    directions='Directions 2 min · Independent check 18 min total across both pages. This is a classroom skill check, not an official TSIA2 test or predicted score.' if index==0 else 'Continue independently. After first attempts are collected: corrections 7 min and reflection 3 min.'
    pages.append(f"<section class='page check'>{header(d,f'Practice check · Page {index+1} of 2')}<p>{esc(directions)}</p>"+''.join(item_html(q) for q in questions)+(f"<h2>Correction and next step</h2><p>{esc(d['reflection'])}</p><div class='reflection-space'></div>" if index else '')+'</section>')
   groups=[('Weekly check',d['check'])]
  (ROOT/f"lessons/week-01/{d['slug']}.md").write_text('\n\n'.join(md)+'\n')
  key_md += [f"## Day {d['day']}: {d['title']}",'']
  for label,questions in groups:
   key_md += [f'### {label}','']
   for q in questions:
    a=key[q['id']];answer=a['answer'];display=answer if not isinstance(answer,dict) else json.dumps(answer)
    key_md += [f"**{q['label']}: {display}.** {a['explanation']}",'']
    if a.get('distractor_notes'):key_md+=['Distractors: '+' '.join(f"{k}: {v}" for k,v in a['distractor_notes'].items()),'']
 style='''@page{size:letter;margin:.45in}*{box-sizing:border-box}body{font:11pt/1.35 Arial,sans-serif;color:#1e293b;background:#e8edf2;margin:0}main{max-width:8.5in;margin:auto}.toolbar{padding:18px;background:#193652;color:white;position:sticky;top:0;z-index:1}.toolbar button{font:inherit;padding:8px 14px;border:0;border-radius:4px;cursor:pointer}.toolbar p{margin:6px 0}.page{background:white;margin:18px auto;padding:.25in;min-height:10in;break-after:page;page-break-after:always}.page:last-child{break-after:auto;page-break-after:auto}.eyebrow{font-size:8pt;letter-spacing:1px;color:#536579;margin:0}h1{font-size:17pt;line-height:1.15;color:#193652;margin:8px 0}h2{font-size:11pt;color:#193652;border-bottom:1px solid #b7c5d4;padding-bottom:4px;margin:12px 0 6px}h3{font-size:10pt;margin:0 0 6px}p{margin:5px 0}.identity{font-size:9pt;margin:10px 0 14px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.question,.example{break-inside:avoid}.question{border:1px solid #c6d0dc;border-radius:5px;padding:8px}.workspace{height:38px;background:repeating-linear-gradient(to bottom,transparent 0,transparent 18px,#edf0f4 19px,transparent 20px)}.examples{margin:8px 0}.example{background:#f0f4f8;padding:10px;border-left:3px solid #6483a4}.example ol{padding-left:16px;margin:4px 0;font-size:10pt}.teaching .question{font-size:10pt}.practice .workspace{height:62px}.exit{margin-top:16px;border-top:2px solid #193652}.reflection-space{height:48px;border-bottom:1px solid #c6d0dc}.options{display:grid;grid-template-columns:1fr 1fr;list-style:none;padding:0;margin:6px 0;font-size:10pt;gap:3px}.check .question{margin:7px 0;padding:7px}.check .workspace{height:29px}.toolbar a{color:white}@media print{body{background:white}.toolbar{display:none}main{max-width:none}.page{margin:0;padding:0;min-height:0}a{color:inherit;text-decoration:none}.question,.example{border-radius:0}}@media screen and (max-width:640px){.page{padding:16px;min-height:0}.grid{grid-template-columns:1fr}.toolbar{position:static}}'''
 html_doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>TSI Math Advisory — Week 1 student packet</title><style>{style}</style></head><body><nav class="toolbar" aria-label="Packet actions"><strong>Week 1 · Percents and linear relationships</strong><p>Five 30-minute sessions. Student materials only. Download this file and open it in a browser to print.</p><button type="button" onclick="window.print()">Print student packet</button></nav><main>{''.join(pages)}</main></body></html>'''
 (ROOT/'print/week-01-student-packet.html').write_text(html_doc)
 (ROOT/'teachers/week-01/answer-key.md').write_text('\n\n'.join(key_md)+'\n')
 print('Built 5 student lessons, 10 intended print sections, and explained teacher key.')
if __name__=='__main__':main()
