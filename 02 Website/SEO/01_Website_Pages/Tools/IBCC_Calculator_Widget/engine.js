/* IBCC public tables reviewed 2026-09-11. Update data and tests together. */
function createIBCCEngine() {
  const reviewed = '2026-09-11';
  const letter = { A:85, B:75, C:65, D:55, E:45 };
  const numeric = {8:87,7:82,6:77,5:70,4:60,3:50};
  const stars = {
    2021:{o:{other:94,mathematics:95,pakistan:93,english:93,urdu:93},a:{other:93,biology:94}},
    2022:{o:{other:95,computer:96},a:{other:95,biology:94,computer:94,mathematics:94}},
    2023:{o:{other:94,mathematics:95,islamiyat:95,urdu:93},a:{other:94,physics:95}},
    2024:{o:{other:94,english:93,urdu:93,pakistan:93},a:{other:94,physics:95,mathematics:95,english:null,urdu:null,pakistan:null,islamiyat:null}},
    2025:{o:{other:94,english:93,urdu:93,pakistan:93},a:{other:94,physics:95,computer:93,english:null,urdu:null,pakistan:null,islamiyat:null}},
    2026:{o:{other:94,english:93,urdu:93},a:{other:94,physics:95,computer:93,english:null,urdu:null,pakistan:null,islamiyat:null}}
  };
  const subjects = {english:'English Language',mathematics:'Mathematics',urdu:'Urdu',islamiyat:'Islamiyat',pakistan:'Pakistan Studies',physics:'Physics',chemistry:'Chemistry',biology:'Biology',computer:'Computer Science',business:'Business',economics:'Economics',accounting:'Accounting',sociology:'Sociology',psychology:'Psychology',history:'History',geography:'Geography',literature:'English Literature',art:'Art & Design',french:'French',arabic:'Arabic',additional:'Additional Mathematics',ict:'ICT'};
  const core = ['english','mathematics','urdu','islamiyat','pakistan'];
  const oElectives = Object.keys(subjects).filter(s=>!core.includes(s));
  const aElectives = Object.keys(subjects).filter(s=>!['english','pakistan','islamiyat','additional','ict'].includes(s));
  const groups = {medical:['physics','chemistry','biology'],engineering:['physics','chemistry','mathematics'],computer:['physics','computer','mathematics']};
  function policy(c) {
    if(c.level==='ssc') return 'ssc';
    if(c.group==='humanities' || c.location==='abroad' || +c.completion<2026) return 'legacy';
    return 'science-2026';
  }
  function convert(row) {
    if(!stars[row.year]) return {error:'Conversion data is verified only for examination years 2021–2026. No 2027 value is assumed.'};
    if(!subjects[row.subject]) return {error:'Choose a supported subject. Other subjects need an individual check.'};
    if(row.grade==='A*'||(row.level==='o'&&row.grade==='9')) {
      const table=stars[row.year][row.level];
      if(!table) return {error:'Unsupported qualification level.'};
      const marks=Object.hasOwn(table,row.subject)?table[row.subject]:table.other;
      return marks===null?{error:'IBCC lists no A* value for this subject and level in this year. Please request an individual check.'}:{marks};
    }
    if(Object.hasOwn(letter,row.grade)) return {marks:letter[row.grade]};
    if(row.level==='o'&&Object.hasOwn(numeric,row.grade)) return {marks:numeric[row.grade]};
    if(row.grade==='2') return {error:'Grade 2 has a published conversion of 40, but this tool does not confirm its acceptance for the required subject. Please check with IBCC.'};
    return {error:'This required subject needs an accepted passing grade. U, F, G and grade 1 cannot be used for a completed estimate.'};
  }
  function calculate(c, rows) {
    const errors=[];
    const add=(message,key)=>errors.push({message,key});
    if(!['ssc','hssc'].includes(c.level)) add('Choose SSC or HSSC.','level');
    if(!['pakistan','abroad'].includes(c.location)) add('Mixed-location or exemption cases need an individual IBCC assessment.','location');
    if(c.status!=='standard') add('This calculator supports the standard Pakistani-national route without exemptions. Please ask IBCC to assess other cases.','status');
    if(c.qualification!=='full') add('Use final GCSE/IGCSE/O Level grades and, for HSSC, full A Level grades. AS-only, double awards and other qualifications need an individual assessment.','qualification');
    if(!['2021','2022','2023','2024','2025','2026','2027'].includes(String(c.completion))) add('Select the year you completed all required O Level subjects.','completion');
    if(!['ssc','humanities',...Object.keys(groups)].includes(c.group)) add('Choose an equivalence group.','group');
    if(c.level==='hssc'&&c.group==='ssc') add('Choose an HSSC equivalence group.','group');
    if(c.level==='hssc'&&c.location==='abroad'&&c.group==='computer') add('The official overseas Computer Science requirements contain conflicting wording. Please confirm your case with IBCC.','group');
    const requiredCore=c.location==='abroad'?core.slice(0,2):core;
    const expectedO=requiredCore.length+3;
    const os=rows.filter(r=>r.level==='o'), as=rows.filter(r=>r.level==='a');
    if(os.length!==expectedO || (c.level==='hssc'&&as.length!==3)) add('Complete the required number of subjects.');
    for(const list of [os,c.level==='hssc'?as:[]]) {
      const seen=new Set();
      for(const r of list) {
        if(!r.subject||!r.grade||!r.year) {add('Complete the subject, grade and examination year.',r.key);continue;}
        if(seen.has(r.subject)) add('A subject cannot be counted twice at the same level.',r.key);
        seen.add(r.subject);
        if(r.level==='o'&&!core.includes(r.subject)&&!oElectives.includes(r.subject)) add('Unsupported O Level subject.',r.key);
        if(r.level==='a'&&!aElectives.includes(r.subject)) add('Unsupported A Level subject.',r.key);
        if(r.level==='o'&&+r.year>+c.completion) add('An O Level exam year is after the completion year. Retakes or improvements need an individual check.',r.key);
        if(r.level==='a'&&+r.year<+c.completion) add('A Level results before O Level completion need an individual check.',r.key);
        const result=convert(r); if(result.error) add(result.error,r.key);
      }
    }
    for(const s of requiredCore) if(!os.some(r=>r.subject===s)) add('Missing compulsory subject: '+subjects[s]+'.');
    if(c.level==='hssc'&&groups[c.group]) {
      for(const s of groups[c.group]) if(!as.some(r=>r.subject===s)) add('This group requires A Level '+subjects[s]+'.');
      for(const s of ['physics','chemistry']) if(!os.some(r=>r.subject===s)) add('This group requires O Level '+subjects[s]+'.');
      if(!os.some(r=>r.subject==='biology'||(c.group!=='medical'&&r.subject==='computer'))) add(c.group==='medical'?'Pre-Medical requires O Level Biology.':'This supported science route requires O Level Biology or Computer Science. Other combinations need IBCC review.');
    }
    const rule=policy(c);
    if(rule==='science-2026'&&as.some(r=>+r.year<=2026)) add('The new science rule specifies O Level completion in 2026 and A Levels thereafter. Same-year or mixed-cohort results need IBCC confirmation.','completion');
    if(errors.length) return {ok:false,errors};
    const active=c.level==='hssc'?[...os,...as]:os;
    const breakdown=active.map(r=>({...r,marks:convert(r).marks,counted:!(rule==='science-2026'&&r.level==='o'&&!core.includes(r.subject))}));
    const counted=breakdown.filter(r=>r.counted), total=counted.reduce((sum,r)=>sum+r.marks,0), max=counted.length*100;
    const sscScience=['physics','chemistry'].every(s=>os.some(r=>r.subject===s))&&os.some(r=>['biology','computer','ict','additional'].includes(r.subject));
    return {ok:true,total,max,percentage:total/max*100,rule,breakdown,group:c.level==='ssc'?(sscScience?'Science':'Arts'):c.group,certificate:rule==='legacy'?total/max*1100:null};
  }
  return {reviewed,subjects,core,oElectives,aElectives,groups,stars,letter,numeric,policy,convert,calculate};
}
if(typeof module!=='undefined'&&module.exports) module.exports=createIBCCEngine;
