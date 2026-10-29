const c=require('./components');
module.exports={name:'tablets',slides:[
 c.cover({pill:'Buying guide &middot; Oct 2026',l1:'iPad vs Samsung',l2pre:'vs',l2hl:'Xiaomi',sub:'Which tablet for O and A Levels?',
  cards:[{kind:'ipad',name:'iPad',price:'&asymp; PKR 100k+'},{kind:'samsung',name:'Samsung',price:'&asymp; PKR 99k+'},{kind:'xiaomi',name:'Xiaomi',price:'&asymp; PKR 98k+'}],hand:'read before buying',cta:'Swipe'}),
 c.product({n:2,pillText:'1 &middot; Apple &middot; 2/8',kind:'ipad',title:'Apple iPad 10th Gen<br>and iPad 11 (A16)',price:'10th Gen (64GB) <b>~PKR 100k to 110k</b><br>iPad 11 (128GB) <b>~PKR 137k to 150k</b>',bullets:['Goodnotes and Notability','Lasts 5 years through A2','7,606 mAh all-day battery'],catchText:'<b>The catch:</b> Pencil adds ~PKR 25k to 30k. Real 10th Gen total: ~PKR 125k to 140k.',cardH:400,bs:50,tw:270,cs:42}),
 c.product({n:3,pillText:'2 &middot; Samsung &middot; 3/8',kind:'samsung',title:'Samsung Tab S9 FE<br>and Tab S10 FE',price:'S9 FE <b>~PKR 99k to 118k</b><br>S10 FE <b>~PKR 113k to 120k</b>',bullets:['S Pen included<br>(PKR 0 extra)','Free Samsung Notes','128GB + microSD + IP68'],circleIdx:0,hand:'&#10003; our pick for value',catchText:'<b>The catch:</b> test Goodnotes on Android first.',cardH:440,bs:44,tw:230,cs:36,gap:22,hs:56}),
 c.product({n:4,pillText:'3 &middot; Xiaomi &middot; 4/8',kind:'xiaomi',title:'Xiaomi Pad 6<br>and Pad 7',price:'Pad 6 <b>~PKR 98k to 110k</b><br>Pad 7 (256GB) <b>~PKR 105k to 124k</b>',bullets:['144Hz screen','About 8,840 mAh battery','256GB storage'],catchText:'<b>The catch:</b> pen ~PKR 20k to 25k extra and sells out locally.',cardH:420,bs:48,tw:260,cs:42}),
 c.pen({n:5,pillText:'The pen rule &middot; 5/8',title:'Which subjects need a stylus?',hl:'stylus?',q:'Differentiate y = x&sup3; &minus; 4x',work:'dy/dx = 3x&sup2; &minus; 4',subjects:'Maths (4024/9709), Physics, Chemistry, Accounting, Economics: yes.',warn:'A tablet without palm rejection is an expensive YouTube screen.',hand:'Computer Science? Buy a laptop first.'}),
 c.table({n:6,pillText:'More options &middot; 6/8',title:'Other tablet options',sub:'Verified Pakistan prices across retailers (Oct 2026)',
  headers:['Model','PKR price','Stylus','Best for'],
  rows:[
   ['iPad 9th Gen (10.2")','~78k to 90k','Extra (~25k)','Budget iPad',false],
   ['Redmi Pad Pro (12.1")','~80k to 86k','Extra (~20k)','Big 120Hz screen',true],
   ['Redmi Pad 2 (11" Wi-Fi)','~66k to 72k','Extra (~20k)','Lowest-cost pen tab',true],
   ['Redmi Pad SE (11")','~55k','No active pen','Video lectures',false],
   ['Tab A9 / A9+ Wi-Fi','~32k / 44k-51k','No S-Pen','Reading PDFs',false],
   ['Tab S9 FE+ / S10 FE+','~123k / 152k','In box (PKR 0)','12.4" split-screen',true]
  ],
  hand:'highlighted rows = best value outside the main 3 picks'}),
 c.picks({n:7,pillText:'Our picks &middot; 7/8',title:'Our picks',items:[['Pen in the box','Tab S9 FE or S10 FE'],['Apps','iPad 10th Gen + Pencil, ~PKR 125k to 140k'],['Screen and storage','Xiaomi Pad 6 or 7'],['Tighter budget','iPad 9th Gen or Redmi Pad Pro <span class="reg">(pen extra)</span>']]}),
 c.cta({n:8,text:'A tablet organises your past papers. You still have to mark them.',hl:'mark them.',body:'We mark your answers to the mark scheme.',button:'Book a free demo class',line1:'WhatsApp +92-336-2144454',line2:'DHA Phase 7 or online',foot:'Full guide: link in bio'})
]};
