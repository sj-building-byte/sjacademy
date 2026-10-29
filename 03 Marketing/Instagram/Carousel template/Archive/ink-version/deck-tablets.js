const c=require('./components');
const T=9, K='Tablet guide';
module.exports={ name:'tablets', slides:[
 c.cover({lines:['iPad,','Samsung','or Xiaomi?'],sub:'Which tablet for O and A Levels? Real PKR prices, pen costs included.',pill:'Oct 2026 prices',total:T}),
 c.receipts({n:2,total:T,kick:K,title:'The shelf price is not the real price',hl:'real price',
  left:{title:'iPad 10th Gen',items:[['Tablet','99,599 to 110,000'],['Pencil','25,000 to 29,999']],total:'~125k to 140k'},
  right:{title:'Tab S9 FE',items:[['Tablet','99,000 to 117,999'],['S Pen','Included']],total:'~99k to 118k'}}),
 c.product({n:3,total:T,kick:K,brand:'Samsung',models:'Galaxy Tab S9 FE and S10 FE',rows:[['S9 FE','PKR 99k to 118k'],['S10 FE','PKR 113k']],bullets:['Free Samsung Notes','128GB + microSD','IP68 water resistance'],stamp:'S Pen in the box',catchText:'Want Goodnotes? Test it on Android.'}),
 c.product({n:4,total:T,kick:K,brand:'Apple',models:'iPad 10th Gen and iPad 11',rows:[['10th Gen','PKR 100k to 110k'],['iPad 11','PKR 150k to 185k']],bullets:['Goodnotes and Notability','Smooth handwriting','Should last through A2'],stamp:'No pen',catchText:'Pencil is ~PKR 25k to 30k extra.'}),
 c.product({n:5,total:T,kick:K,brand:'Xiaomi',models:'Pad 6 and Pad 7',rows:[['Pad 6','PKR 98k to 110k'],['Pad 7','PKR 105k to 117k']],bullets:['144Hz screen','About 8,800 mAh battery','256GB storage'],stamp:'No pen',catchText:'Pen ~PKR 20k to 25k, sells out locally.'}),
 c.paper({n:6,total:T,kick:K,title:'Which subjects need a stylus?',hl:'stylus?',code:'9709 &middot; Paper 1',q:'Differentiate y = x&sup3; &minus; 4x &nbsp;[2]',work:'dy/dx = 3x&sup2; &minus; 4',margin:'method marks live in your working',subjects:'Maths (4024/9709), Physics, Chemistry, Accounting, Economics: yes.'}),
 c.big({n:7,total:T,kick:K,text:'A tablet without palm rejection is an expensive YouTube screen.',hl:'expensive YouTube screen.',noteLabel:'Computer Science (2210/9618)',noteText:'Buy a laptop first.'}),
 c.picks({n:8,total:T,kick:K,title:'Our picks',items:[['Pen in the box','Tab S9 FE or S10 FE'],['Apps','iPad 10th Gen + Pencil, ~PKR 125k to 140k'],['Screen and storage','Xiaomi Pad 6 or 7'],['Tighter budget','iPad 9th Gen or Redmi Pad Pro <span class="reg">(pen extra)</span>']]}),
 c.cta({n:9,total:T,text:'A tablet organises your past papers. You still have to mark them.',hl:'mark them.',body:'We mark your answers to the mark scheme.',button:'Book a free demo class',line1:'WhatsApp +92-336-2144454',line2:'DHA Phase 7 or online',foot:'Full guide: link in bio, sjacademy.pk'})
]};
