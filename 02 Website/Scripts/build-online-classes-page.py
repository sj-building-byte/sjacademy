import json, re, html

WA = "https://wa.me/923362144454?text="
REG = "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjYwMjMiLCJ0b2dnbGUiOmZhbHNlfQ%3D%3D"
MAPS = "https://maps.app.goo.gl/QSrQVThJrZMzJgKF8"
B = "https://www.sjacademy.pk"

from urllib.parse import quote
def wa(msg):
    return WA + quote(msg, safe="")

DEMO = wa("Hi SJ Academy, I'd like to book a free online demo class.\nLevel: AS\nSubject: Maths (9709)\nSession: May/June 2027\nMode (in class or online): Online\nJoining from: \n(Ref: ONL-AS)\nMy name is ")
Q = wa("Hi SJ Academy, I have a question about your online classes.\nJoining from: \n(Ref: ONL-Q)\nMy name is ")

TICK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 13.5c2 1.4 3.4 3 4.6 5C11 12.5 14.5 8 20 4.5"/></svg>'
CIRCLE = '<svg class="sj-circle" viewBox="0 0 120 70" preserveAspectRatio="none" aria-hidden="true"><path d="M14 38C10 18 40 6 68 7c27 1 44 13 42 30-2 16-30 24-56 23C28 59 8 50 13 30" fill="none" stroke="#FE6100" stroke-width="2.6" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>'

def demo_link(cls, label, loc, extra=""):
    return f'<a class="{cls}" href="{DEMO}" target="_blank" rel="noopener" data-onl-demo data-loc="{loc}"{extra}>{label}</a>'

def link(href, text, go=False, loc=None, ext=False):
    c = "sj-link sj-link-go" if go else "sj-link"
    a = f' data-loc="{loc}"' if loc else ""
    t = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="{c}" href="{href}"{t}{a}>{text}</a>'

# ---------------- FAQ (visible text and schema come from the same list) ----------------
FAQ = [
 ("What is the fee for online O Level and A Level classes?",
  f"The same as in class: from Rs. 8,500 a month per subject for O Level, and from Rs. 10,500 a month per subject for AS and A2, plus a one-time admission fee of Rs. 3,500. You get 10% off when you pay 3 months upfront. Full figures are on the {link(B+'/fee-structure/','fee structure page')}."),
 ("Can students outside Pakistan join SJ Academy online?",
  "Yes. Online classes are open to students anywhere, as long as the class times work where you live. The UAE, Oman, Saudi Arabia, Qatar, Bahrain and Kuwait are 1 or 2 hours behind Pakistan, so most classes land in the afternoon or early evening there."),
 ("What time are the classes in Dubai, Riyadh or Doha?",
  "Timings are set in Pakistan time. The UAE and Oman are 1 hour behind Pakistan, and Saudi Arabia, Qatar, Bahrain and Kuwait are 2 hours behind. None of these countries changes its clocks, so a class time never moves. A 7 PM class in Karachi starts at 6 PM in Dubai and 5 PM in Riyadh or Doha. The class finder at the top of this page shows every class in your local time."),
 ("Is the online class the same as the class in Karachi?",
  "Yes. Online students join the same live class, with the same teacher, as the students in the classroom in Karachi. A few subjects also run a separate online batch at another time, and the class finder labels them. Lab practicals are the one exception: they are taught in the lab in Karachi."),
 ("What happens if my child misses an online class?",
  "Internet connections have bad days, on both sides of the screen. Classes are recorded, so a missed class, for a school trip, an exam or a dropped connection, is not a missed topic."),
 ("How are answers marked in online classes?",
  "Online students write answers the same way the students in the room do, send them in online, and get them back marked against the Cambridge mark scheme. That way they see which line lost the mark, not just the total."),
 ("Which subjects can I study online?",
  "O Level and IGCSE: Maths, Physics, Chemistry, Biology, Accounting, Business, Economics, Computer Science, English, Urdu, Pakistan Studies and Islamiyat. AS and A2: Maths, Physics, Chemistry, Biology, Business, Economics, Accounting, Computer Science, Sociology, Psychology and Law, with English at AS. The class finder at the top of this page always shows the current timetable."),
 ("Do you teach IGCSE students online?",
  "Yes. O Level and IGCSE students sit in the same class, because the two syllabuses are now very close. Tell us your syllabus code in the WhatsApp message, so the teacher knows which papers you are sitting."),
 ("Where do students in the Gulf sit their Cambridge exams?",
  f"At a Cambridge exam centre in their own country: usually their school, or for private candidates a registered centre, often the British Council. The UAE and Oman follow the Zone 4 timetable, the same as Pakistan. Saudi Arabia, Qatar, Bahrain and Kuwait follow Zone 3. See the {link(B+'/cambridge-exam-timetable-all-zones/','Cambridge exam timetable for every zone')}."),
 ("How do we pay the fee from abroad?",
  "Fees are charged in Pakistani rupees and paid by bank transfer, from Pakistan or from abroad. The account details are in the registration form. Your bank may charge its own fee for an international transfer."),
 ("Can we take a free online demo class first?",
  "Yes. The first class is free, online or in class. Book it on WhatsApp, tell us the subject and where you are joining from, and the team will book you into the next class."),
 ("Is it too late to join the May/June 2027 batch?",
  "Usually not, and this question comes in every month. The batches started in August and are still open. Message us on WhatsApp and the teacher will tell you where the class is in the syllabus and how to catch up."),
 ("Do you offer one-on-one online tuition?",
  "No. SJ Academy teaches small-batch live classes, online and in class. That keeps the fee per month rather than per hour, and someone else in the class usually asks the question you were about to."),
]

def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

faq_html = "\n".join(
    f'        <details{" open" if i==0 else ""}><summary>{q}</summary><div class="sj-faq-a"><p>{a}</p></div></details>'
    for i,(q,a) in enumerate(FAQ))

# ---------------- teachers ----------------
T = [
 ("Sir Salman Junaid", "A Level and O Level Maths, A Level Physics, online O Level Physics", B+"/wp-content/uploads/2025/06/salman-1-modified.png", 182,182,
  ["Ex-KGS faculty, 12+ years of teaching","NED University engineer","500+ solved past paper videos"]),
 ("Sir Sunyyan Junaid", "A Level Business (9609)", B+"/wp-content/uploads/2025/07/296167730_10159330125240939_9121453372746153911_n-min-300x203.jpg",300,203,
  ["8+ years in business, marketing and leadership","Writes his own model answers for every paper"]),
 ("Sir Khawar Shuaib", "A Level Economics (9708)", B+"/wp-content/uploads/2026/06/Khawar-2-768x615.jpeg",768,615,
  ["Teaching since 2014","Has taught A Level and IB Economics students in Pakistan, the UAE and the UK"]),
 ("Sir Umair", "A Level and O Level Biology", B+"/wp-content/uploads/2025/11/Umair-Pic-1-300x217.jpg",300,217,
  ["LUMS graduate","8+ years teaching IB and Cambridge A Level Biology"]),
 ("Sir Abdullah Zaman", "A Level Chemistry (9701)", B+"/wp-content/uploads/2025/12/Zaman-chemistry-300x222.jpeg",300,222,
  ["5+ years teaching O and A Level Chemistry"]),
 ("Sir Riza Walji", "A Level Computer Science (9618)", B+"/wp-content/uploads/2025/11/Sir-Riza-768x454.webp",768,454,
  ["9+ years of teaching"]),
 ("Sir Saifullah", "A Level Accounting (9706)", B+"/wp-content/uploads/2026/07/Saifullah-Accounts-768x829.jpeg",768,829,
  ["5+ years of teaching","CAIE-certified Accounting teacher"]),
 ("Sir Syed Aalyan Ali", "O Level Business and Economics", B+"/wp-content/uploads/2026/06/Alyaan-240x300.jpeg",240,300,
  ["IBA Karachi graduate, Accounting and Finance","7+ years of teaching"]),
 ("Sir Kashaan Ali", "O Level Islamiyat and Pakistan Studies", B+"/wp-content/uploads/2025/07/Kashan-Ali-768x431.jpeg",768,431,
  ["Teaching since 2003"]),
]
teacher_html = "\n".join(
  f'        <div class="sj-card sj-teacher"><img src="{src}" alt="{n}, {s.split(",")[0]} teacher at SJ Academy" width="{w}" height="{h}" loading="lazy" decoding="async"><div><b>{n}</b><span>{s}</span></div><ul>{"".join("<li>"+f+"</li>" for f in facts)}</ul></div>'
  for (n,s,src,w,h,facts) in T)

PAGE = f'''<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Caveat:wght@600&display=swap" rel="stylesheet"></noscript>

<div id="sj" class="sj-p-online-classes" data-family="enrol">

  <section class="sj-section sj-bg-dots" data-sj-hero>
    <div class="sj-wrap">
      <nav class="sj-crumbs" aria-label="Breadcrumb"><ol><li><a href="{B}/">Home</a></li><li aria-current="page">Online O &amp; A Level classes</li></ol></nav>
    </div>
    <div class="sj-wrap sj-grid sj-grid-hero">
      <div class="sj-stack">
        <h1 class="sj-h1"><span class="sj-pill"><span>Online O &amp; A Level classes &middot; Pakistan &amp; the Gulf</span></span>Live online. <span class="sj-hl">Never left out.</span></h1>
        <p class="sj-lead sj-measure">Online O Level, IGCSE and A Level classes, taught live by SJ Academy&rsquo;s Karachi teachers to students in Pakistan, the UAE, Saudi Arabia, Qatar, Oman, Bahrain and Kuwait. Recorded, and every answer marked.</p>
        <span class="sj-hand sj-tilt-l">same class, different city</span>
        {demo_link("sj-btn sj-btn-primary onl-phone-cta","Book a free demo on WhatsApp","hero_top")}
      </div>
      <div class="sj-offset sj-stack" id="onl-card">
        <h2 class="sj-h3">Find your class, in your time</h2>
        <div class="sj-choices" role="group" aria-label="Level">
          <label class="sj-choice"><input type="radio" name="onl-level" value="o"><span>O Level</span></label>
          <label class="sj-choice"><input type="radio" name="onl-level" value="as" checked><span>AS</span></label>
          <label class="sj-choice"><input type="radio" name="onl-level" value="a2"><span>A2</span></label>
        </div>
        <div class="onl-pick">
          <div class="sj-field"><label class="sj-label" for="onl-subject">Subject</label><select class="sj-select" id="onl-subject"><option value="math">Maths</option></select></div>
          <div class="sj-field"><label class="sj-label" for="onl-where">You are in</label><select class="sj-select" id="onl-where">
            <option value="pk">Pakistan</option><option value="ae">UAE</option><option value="om">Oman</option><option value="sa">Saudi Arabia</option><option value="qa">Qatar</option><option value="bh">Bahrain</option><option value="kw">Kuwait</option><option value="xx" hidden>Somewhere else</option>
          </select></div>
        </div>
        <div id="onl-out" aria-live="polite">
          <ul class="onl-rows">
            <li><span>Teacher</span><span>Sir Salman Junaid</span></li>
            <li><span>Classes</span><span>Mon, Wed &amp; Fri &middot; 5:00 - 6:00 PM, Pakistan time</span></li>
            <li><span>Fee</span><span>From Rs. 10,500 a month &middot; {link(B+'/fee-structure/','See full fees')}</span></li>
          </ul>
        </div>
        <div class="onl-acts">{demo_link("sj-btn sj-btn-primary","Book a free demo on WhatsApp","hero")}</div>
        <p class="sj-small sj-muted">One class free, then decide. Already sure? <a class="sj-link" href="{REG}" data-loc="hero">Register for a class</a></p>
        <noscript><p class="sj-small">Class times are on the {link(B+'/classes-schedule/','timetable page')}, in Pakistan time.</p></noscript>
      </div>
    </div>
    <div class="sj-wrap onl-gap">
      <div class="sj-proof">
        <span><b><span class="sj-circled">{CIRCLE}4,500+</span></b>students taught</span>
        <a href="{MAPS}" target="_blank" rel="noopener"><b>5.0 on Google</b>from 226 reviews</a>
        <span><b>Recorded</b>miss a class, watch it later</span>
      </div>
    </div>
  </section>

  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">The problem</div>
        <h2 class="sj-h2">Online usually means a video. <span class="sj-hl">Or a muted square.</span></h2>
        <p class="onl-top">Cambridge tuition from abroad, or from a city without a good centre, tends to go one of three ways. None of them is a class.</p>
      </div>
      <div class="sj-grid sj-grid-3 onl-pins">
        <div class="sj-pinned"><span class="sj-pin" aria-hidden="true"></span><b>A recording you watch alone</b><p>It explains the topic. It does not notice when you are lost, and it never marks what you write.</p></div>
        <div class="sj-pinned"><span class="sj-pin" aria-hidden="true"></span><b>A class built for another clock</b><p>Lessons that start before your school ends, or long after it, because nobody planned them for your time zone.</p></div>
        <div class="sj-pinned"><span class="sj-pin" aria-hidden="true"></span><b>One-to-one, billed by the hour</b><p>Useful for one gap, expensive for a whole syllabus, and nobody else is there to ask the question you were too shy to ask.</p></div>
      </div>
      <p class="sj-measure">What works online is what works in a classroom: a teacher, a timetable, other students, and answers that come back marked. So that is exactly what the online class is.</p>
    </div>
  </section>

  <section class="sj-section sj-bg-brown">
    <div class="sj-wrap onl-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">How it works</div>
        <h2 class="sj-h2">The Karachi class, <span class="sj-hl">on your screen</span></h2>
        <p class="sj-measure">There is no separate online product. You join the class that is already running, with the teacher who runs it, and you are marked the way the room is marked.</p>
        <ol class="sj-steps">
          <li><b>Join the live class</b><span>The same lesson the students in Karachi are sitting, at the same time, with the same teacher. Ask your question when it comes up, not in an email later.</span></li>
          <li><b>Write the answer</b><span>Past paper questions in class and after it, because Cambridge marks what you write, not what you followed.</span></li>
          <li><b>Get it marked</b><span>Send your answers in online. They come back marked against the mark scheme, so you see which line lost the mark.</span></li>
          <li><b>Missed it? Watch it</b><span>Classes are recorded, so a school trip, an exam or a dropped connection does not cost you a topic.</span></li>
        </ol>
      </div>
      <div class="onl-photo">
        <div class="sj-polaroid"><span class="sj-tape" aria-hidden="true"></span><img src="{B}/wp-content/uploads/2026/10/IMG_6923_Original-1-1.webp" alt="Sir Sunyyan Junaid teaching an A Level Business class at SJ Academy in Karachi" width="768" height="432" loading="lazy" decoding="async"><span class="sj-hand">the room your screen joins</span></div>
      </div>
    </div>
  </section>

  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">Your time zone</div>
        <h2 class="sj-h2">Evening in Karachi. <span class="sj-hl">Afternoon</span> in the Gulf.</h2>
        <p class="onl-top">The UAE and Oman are 1 hour behind Pakistan. Saudi Arabia, Qatar, Bahrain and Kuwait are 2 hours behind. None of them changes its clocks, so a class time you pick in November is the same in May. Most weekday classes run between 4 PM and 9 PM Pakistan time, with some weekend classes in the early afternoon.</p>
      </div>
      <div class="onl-two onl-two-z">
        <div class="sj-table-wrap"><table class="sj-table sj-table-stack"><thead><tr><th scope="col">Pakistan</th><th scope="col">UAE and Oman</th><th scope="col">Saudi, Qatar, Bahrain, Kuwait</th></tr></thead><tbody>
          <tr><td data-label="Pakistan">4:00 PM</td><td data-label="UAE and Oman">3:00 PM</td><td data-label="Saudi, Qatar, Bahrain, Kuwait">2:00 PM</td></tr>
          <tr class="is-key"><td data-label="Pakistan">6:00 PM</td><td data-label="UAE and Oman">5:00 PM</td><td data-label="Saudi, Qatar, Bahrain, Kuwait">4:00 PM</td></tr>
          <tr><td data-label="Pakistan">7:00 PM</td><td data-label="UAE and Oman">6:00 PM</td><td data-label="Saudi, Qatar, Bahrain, Kuwait">5:00 PM</td></tr>
          <tr><td data-label="Pakistan">9:00 PM</td><td data-label="UAE and Oman">8:00 PM</td><td data-label="Saudi, Qatar, Bahrain, Kuwait">7:00 PM</td></tr>
        </tbody></table></div>
        <div class="sj-card sj-stack">
          <h3 class="sj-h3">Your exams run on your zone&rsquo;s timetable</h3>
          <p>The UAE and Oman sit Cambridge exams on the Zone 4 timetable, the same as Pakistan. Saudi Arabia, Qatar, Bahrain and Kuwait sit them on Zone 3. Each zone has its own dates and times, so plan revision around yours.</p>
          <p class="sj-row">{link(B+'/cambridge-exam-timetable-all-zones/','Timetables for every zone',True,'zones')} {link(B+'/caie-zone-4-timetable/','Zone 4 timetable',True,'zones')}</p>
          <p class="sj-small sj-muted">From Cambridge&rsquo;s administrative zone lookup. Check with your exams officer.</p>
        </div>
      </div>
      <p class="sj-measure">A class that starts before your school ends? Some subjects run a second batch at another time. Ask on WhatsApp which one fits.</p>
    </div>
  </section>

  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">Your teachers</div>
        <h2 class="sj-h2">Taught by the <span class="sj-hl">same teachers</span></h2>
        <p class="onl-top">Online students are taught by the same teachers as the classroom in Karachi. These are the teachers behind the main subjects. Every teacher, including English, Urdu, Sociology, Psychology and Law, is on the {link(B+'/meet-the-teachers/','teachers page')}.</p>
      </div>
      <div class="sj-grid sj-grid-3 onl-teach">
{teacher_html}
      </div>
    </div>
  </section>

  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div class="sj-measure">
        <div class="sj-eyebrow">What you get</div>
        <h2 class="sj-h2">Everything the room gets. <span class="sj-hl">Plus a replay.</span></h2>
      </div>
      <div class="sj-grid sj-grid-3 onl-get">
        <div class="sj-card"><b>A live class, not a video</b><p>So you can ask the question the moment it comes up.</p></div>
        <div class="sj-card"><b>The same class as Karachi</b><p>So online students are never the second batch of anything.</p></div>
        <div class="sj-card"><b>Answers marked online</b><p>Against the mark scheme, so you see which line lost the mark.</p></div>
        <div class="sj-card"><b>Recorded classes</b><p>So a missed class is not a missed topic.</p></div>
        <div class="sj-card"><b>Past paper practice</b><p>In every subject, so May looks like something you have seen before.</p></div>
        <div class="sj-card"><b>One free class first</b><p>So you can test the teacher and the connection before you pay.</p></div>
      </div>
    </div>
  </section>

  <section class="sj-section sj-bg-canvas">
    <div class="sj-wrap onl-two">
      <div class="sj-stack">
        <div class="sj-eyebrow">For parents</div>
        <h2 class="sj-h2">No surprises, <span class="sj-hl">wherever you are</span></h2>
        <p class="sj-measure">You may be a flight away from the classroom. The fee, the attention and the updates should not depend on that.</p>
      </div>
      <div class="sj-card sj-stack">
        <ul class="sj-ticks">
          <li>{TICK}<span>From Rs. 8,500 a month per subject at O Level and Rs. 10,500 at AS and A2. a month, not an hour, with 10% off when you pay 3 months upfront</span></li>
          <li>{TICK}<span>Paid in Pakistani rupees by bank transfer, from Pakistan or abroad</span></li>
          <li>{TICK}<span>Classes are kept small, and every answer your child writes is marked, so nobody hides behind a switched-off camera</span></li>
          <li>{TICK}<span>If your child starts falling behind, the teacher will tell you. You can ask for an update at any time on WhatsApp</span></li>
          <li>{TICK}<span>Your child can sit one class free before you pay anything</span></li>
        </ul>
        <p class="sj-row">{demo_link("sj-link sj-link-go","Book a free demo class","parents")} {link(B+'/fee-structure/','See full fees')}</p>
      </div>
    </div>
  </section>

  <section class="sj-section sj-bg-dots">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">SJ Academy students</div>
        <h2 class="sj-h2">&ldquo;I never feel <span class="sj-hl">left out</span>&rdquo;</h2>
      </div>
      <div class="sj-grid sj-grid-3">
        <div class="sj-card sj-review sj-tagged"><span class="sj-tag">studying from abroad</span><p class="sj-review-text">"As a student studying online from abroad, I can say this academy has been amazing! &#8230; The classes are highly interactive and well organised! I never feel left out despite being behind a screen. Sir Sunyyan has been a wonderful business teacher &#8230; He makes complex topics much easier to learn and keeps every business class interesting."</p><div class="sj-review-by"><span class="sj-avatar" aria-hidden="true">GB</span><span><b>Ghazifa Batool</b><br>Online A Level Business student</span></div></div>
        <div class="sj-card sj-review"><p class="sj-review-text">"&#8230; i went from a 50 to 72 in my past paper practices using his tips to solve questions quickly and easily. He focuses on each student&#39;s progress closely &#8230;"</p><div class="sj-review-by"><span class="sj-avatar" aria-hidden="true">AZ</span><span><b>Aiman Zahra</b><br>A Level Maths &middot; Google review</span></div></div>
        <div class="sj-card sj-review"><p class="sj-review-text">"I studied A Level Business with Sir Sunyyan at SJ Academy and honestly had a really good experience. He explains concepts in a very simple way and focuses a lot on how to actually apply them in exam questions, which helped me a lot. His feedback on answers was also really useful because I knew exactly what I needed to improve."</p><div class="sj-review-by"><span class="sj-avatar" aria-hidden="true">H</span><span><b>Hamza</b><br>A Level Business &middot; Google review</span></div></div>
      </div>
      <p>SJ Academy is rated 5.0 on Google from 226 reviews. {link(MAPS,'Read them on Google',True,'reviews',True)}</p>
    </div>
  </section>

  <section class="sj-section sj-bg-white">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">Not ready yet?</div>
        <h2 class="sj-h2">Start with the <span class="sj-hl">free tools</span></h2>
      </div>
      <div class="sj-grid sj-grid-4">
        <a class="sj-tile" href="{B}/a-level-past-papers/"><b>A Level past papers</b><p>Question papers and mark schemes for 13 subjects, by year and paper. Free.</p><span class="sj-link sj-link-go">Open past papers</span></a>
        <a class="sj-tile" href="{B}/o-level-past-papers/"><b>O Level past papers</b><p>Every O Level subject we teach, with mark schemes. Free.</p><span class="sj-link sj-link-go">Open past papers</span></a>
        <a class="sj-tile" href="{B}/cambridge-exam-timetable-all-zones/"><b>Exam timetable, every zone</b><p>May/June 2027 dates for Zones 1 to 6, with a country finder. Free.</p><span class="sj-link sj-link-go">Find your dates</span></a>
        <a class="sj-tile" href="{B}/a-level-grade-strategy-tool/"><b>A Level grade calculator</b><p>The A2 marks you need for your target grade. Free.</p><span class="sj-link sj-link-go">Open the calculator</span></a>
      </div>
      <p class="sj-small sj-muted">Looking for one subject? See the {link(B+'/a-level-tuition-center-karachi/','A Level tuition page')} or the {link(B+'/o-level-tuition-center-karachi/','O Level tuition page')}. Every class there can be taken online.</p>
    </div>
  </section>

  <section class="sj-section sj-bg-canvas">
    <div class="sj-wrap sj-stack-lg">
      <div>
        <div class="sj-eyebrow">FAQ</div>
        <h2 class="sj-h2">Questions about <span class="sj-hl">online classes</span></h2>
      </div>
      <div class="sj-faq">
{faq_html}
      </div>
      <p class="sj-small sj-muted">SJ Academy is an independent tuition centre and is not affiliated with or endorsed by Cambridge.</p>
    </div>
  </section>

  <section class="sj-section sj-bg-yellow">
    <div class="sj-wrap sj-stack onl-final">
      <h2 class="sj-h2">Sit one live class before you pay for any</h2>
      <p class="sj-measure">Book a free online demo and tell us where you are joining from. Worst case, you get a free class at a sensible hour.</p>
      <div class="sj-row">{demo_link("sj-btn sj-btn-primary","Book a free demo on WhatsApp","final_band")}</div>
      <p>or <a class="sj-link" href="{REG}" data-loc="final_band">register for a class</a></p>
    </div>
  </section>

  <div class="sj-bar">
    {demo_link("sj-btn sj-btn-primary","Book a free demo","bottom_bar")}
    <a class="sj-btn sj-btn-wa" href="{Q}" target="_blank" rel="noopener" data-loc="bottom_bar">WhatsApp us</a>
  </div>
</div>
'''

P = "#sj.sj-p-online-classes"
CSS = f'''<style>
{P} .onl-top{{margin-top:var(--sj-s3)}}
{P} .onl-gap{{margin-top:var(--sj-s6)}}
{P} .onl-pick{{display:grid;gap:var(--sj-s3)}}
{P} .onl-rows{{border-top:1.5px solid var(--sj-ink)}}
{P} .onl-rows li{{display:grid;grid-template-columns:84px minmax(0,1fr);gap:10px;padding:11px 0;border-bottom:1px solid var(--sj-line);color:var(--sj-ink)}}
{P} .onl-rows li>span:first-child{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--sj-muted);padding:3px 0}}
{P} .onl-rows small{{display:block;font-size:14px;color:var(--sj-muted)}}
{P} .onl-rows .onl-slot+.onl-slot{{margin-top:8px}}
{P} .onl-acts{{display:grid;gap:var(--sj-s3)}}
{P} .onl-two{{display:grid;gap:var(--sj-s6);grid-template-columns:minmax(0,1fr)}}
{P} .onl-pins .sj-pinned{{text-align:left;padding:24px 18px 18px}}
{P} .onl-pins .sj-pinned p{{margin-top:6px;font-size:15px;line-height:1.5}}
{P} .onl-photo .sj-polaroid{{max-width:440px;margin:14px auto 8px}}
{P} .onl-teach .sj-teacher img{{object-position:50% 20%}}
{P} .onl-get b{{display:block;font-weight:500;color:var(--sj-ink)}}
{P} .onl-get p{{margin-top:4px;font-size:15px;color:var(--sj-muted)}}
{P} .sj-proof .sj-circled{{margin-left:-10px}}
{P} .onl-final{{text-align:center;display:grid;justify-items:center}}
{P} .onl-final .sj-row{{justify-content:center}}
{P} .onl-phone-cta{{display:none}}
@media (max-width:899px){{.joinchat,#back-to-top{{display:none!important}}{P} .onl-phone-cta{{display:flex;width:fit-content}}}}
@media (min-width:600px){{{P} .onl-pick{{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}}}
@media (min-width:900px){{{P} .onl-two{{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:var(--sj-s7);align-items:center}}{P} .onl-two-z{{grid-template-columns:minmax(0,1fr) minmax(0,1fr);align-items:start}}}}
</style>
'''

JS = r'''<script>
(function(){
  var root=document.getElementById('sj'); if(!root||!root.classList.contains('sj-p-online-classes')) return;
  var $=function(id){return document.getElementById(id)};
  var each=function(list,fn){Array.prototype.forEach.call(list,fn)};
  var SHEET='https://docs.google.com/spreadsheets/d/e/2PACX-1vRNaIRWzVbWjAz6uXXzEngSykiYmSrY_jeeRCjLgMXf1aF8Zo39EqRCM7s8VuE4RWzf0edXe7UhTCf8/pub?single=true&output=tsv&gid=';
  var WA='https://wa.me/923362144454?text=';
  var GID={o:'674937139',as:'1456859397',a2:'1559855613'};
  var LV={o:{name:'O Level',code:'O',fee:'From Rs. 8,500 a month'},as:{name:'AS',code:'AS',fee:'From Rs. 10,500 a month'},a2:{name:'A2',code:'A2',fee:'From Rs. 10,500 a month'}};
  var SUBJECTS=[['math','Maths',/math/],['phys','Physics',/phys/],['chem','Chemistry',/chem/],['bio','Biology',/bio/],['comp','Computer Science',/comp|\bcs\b/],['acc','Accounting',/acc/],['bus','Business',/bus/],['eco','Economics',/eco/],['pak','Pakistan Studies',/pak|p\.?\s?st/],['isl','Islamiyat',/isl/],['urdu','Urdu',/urdu/],['eng','English',/eng/],['psy','Psychology',/psy/],['soc','Sociology',/soc/],['law','Law',/law/]];
  var CODE={o:{math:'4024',phys:'5054',chem:'5070',bio:'5090',acc:'7707',bus:'7081',eco:'2281',pak:'2059',isl:'2058',eng:'1123',urdu:'3248',comp:'2210'},
            a:{math:'9709',phys:'9702',chem:'9701',bio:'9700',bus:'9609',eco:'9708',acc:'9706',comp:'9618',eng:'9695',soc:'9699',psy:'9990',law:'9084',urdu:'9686'}};
  var TEACH={o:{math:'Sir Salman Junaid',phys:'Sir Salman Junaid (online batch), Sir Basharat (in class)',bio:'Sir Umair',bus:'Sir Syed Aalyan Ali',eco:'Sir Syed Aalyan Ali',pak:'Sir Kashaan Ali',isl:'Sir Kashaan Ali',eng:'Miss Tayyaba Yaseen',urdu:'Miss Asmat Zafar',comp:'Sir Riza Walji'},
             a:{math:'Sir Salman Junaid',phys:'Sir Salman Junaid',chem:'Sir Abdullah Zaman',bio:'Sir Umair',bus:'Sir Sunyyan Junaid',eco:'Sir Khawar Shuaib',acc:'Sir Saifullah',comp:'Sir Riza Walji',eng:'Miss Tayyaba Yaseen',soc:'Miss Tayyaba Yaseen',psy:'Miss Muzna Zaidi',urdu:'Miss Asmat Zafar'}};
  var PAGE={o:{math:'o-level-math-tuition',phys:'o-level-physics-tuition',chem:'o-level-chemistry-tuitions',bio:'o-level-biology-tuition',acc:'o-level-accounting-tuition',bus:'o-level-business-tuition',eco:'o-level-economics-tuition',pak:'o-level-pakistan-studies-tuition',isl:'o-level-islamiat-tuition'},
            a:{math:'a-level-maths-tuition',phys:'a-level-physics-tuition',chem:'a-level-chemistry-tuition',bio:'a-level-biology-tuition',bus:'a-level-business-tuition',eco:'a-level-economics-tuition',acc:'a-level-accounting-tuition',comp:'a-level-computer-science-tuition'}};
  var ZONE={pk:['Asia/Karachi','Pakistan',300],ae:['Asia/Dubai','UAE',240],om:['Asia/Muscat','Oman',240],sa:['Asia/Riyadh','Saudi',180],qa:['Asia/Qatar','Qatar',180],bh:['Asia/Bahrain','Bahrain',180],kw:['Asia/Kuwait','Kuwait',180]};
  var TZMAP={'Asia/Karachi':'pk','Asia/Dubai':'ae','Asia/Muscat':'om','Asia/Riyadh':'sa','Asia/Qatar':'qa','Asia/Bahrain':'bh','Asia/Kuwait':'kw'};
  var TIME=/\d{1,2}(?::\d{2})?\s*-\s*\d{1,2}(?::\d{2})?\s*(?:am|pm)?/i;
  var DAY3=['mon','tue','wed','thu','fri','sat','sun'];
  var st={level:'as',subject:'math',where:'pk',data:{}},sheets={},myTz='';
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]})}
  function lvKey(l){return l==='o'?'o':'a'}

  /* where the visitor is: from the link (?country=ae) or the browser's time zone */
  try{myTz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}
  var qs={};location.search.replace(/[?&]([^=&]+)=([^&]*)/g,function(_,k,v){qs[k]=decodeURIComponent(v).toLowerCase()});
  if(ZONE[qs.country]){st.where=qs.country}else if(TZMAP[myTz]){st.where=TZMAP[myTz]}else if(myTz&&myTz!=='Asia/Karachi'){
    st.where='xx';var xo=$('onl-where').querySelector('option[value="xx"]');xo.hidden=false;xo.textContent='My time zone ('+myTz.split('/').pop().replace(/_/g,' ')+')';ZONE.xx=[myTz,'your local',null]}
  if(LV[qs.level]){st.level=qs.level}
  if(qs.subject){st.subject=qs.subject}
  $('onl-where').value=st.where;
  each(root.querySelectorAll('input[name="onl-level"]'),function(i){i.checked=i.value===st.level});

  /* timetable sheet (shares its cache with the homepage, timetable and subject pages) */
  function parseTsv(text){
    var rows=[],row=[],f='',q=false;
    for(var i=0;i<text.length;i++){var c=text[i],n=text[i+1];
      if(c==='"'&&q&&n==='"'){f+='"';i++;continue}
      if(c==='"'){q=!q;continue}
      if(c==='\t'&&!q){row.push(f);f='';continue}
      if((c==='\n'||c==='\r')&&!q){if(c==='\r'&&n==='\n')i++;row.push(f);rows.push(row);row=[];f='';continue}
      f+=c}
    row.push(f);rows.push(row);
    rows=rows.filter(function(r){return r.some(function(v){return String(v||'').trim()!==''})});
    if(rows.length<2) return null;
    var days=rows[0].slice(1).map(function(d){return String(d||'').trim()});
    return {days:days,rows:rows.slice(1).map(function(r){return {time:String(r[0]||'').trim(),cells:r.slice(1,days.length+1)}}).filter(function(r){return r.time})};
  }
  function load(gid,cb){
    if(sheets[gid]!==undefined) return cb(sheets[gid]);
    try{var s=sessionStorage.getItem('sjh-tt-'+gid);if(s){var v=JSON.parse(s);if(v&&v._t&&Date.now()-v._t<600000){sheets[gid]=v;return cb(v)}}}catch(e){}
    if(!window.fetch) return cb(null);
    fetch(SHEET+gid).then(function(r){if(!r.ok)throw 0;return r.text()}).then(function(t){
      var d=parseTsv(t);sheets[gid]=d;try{if(d){d._t=Date.now();sessionStorage.setItem('sjh-tt-'+gid,JSON.stringify(d))}}catch(e){}cb(d);
    }).catch(function(){cb(null)});
  }
  function flags(s){var b=/batch[\s-]*(\d+)/i.exec(s),t=TIME.exec(s);return {online:/online/i.test(s),batch:b?b[1]:'',time:t?t[0]:''}}
  function clean(s){return s.replace(/[()]/g,' ').replace(/online/ig,' ').replace(/batch[\s-]*\d+/ig,' ').replace(TIME,' ').replace(/\s+/g,' ').trim()}
  function subj(raw){var l=raw.toLowerCase();for(var i=0;i<SUBJECTS.length;i++)if(SUBJECTS[i][2].test(l))return SUBJECTS[i];return null}
  function item(text,extra){var name=clean(text);if(!/[a-z]/i.test(name))return null;var s=subj(name);if(!s)return null;var f=flags(text);
    return {key:s[0],label:s[1],online:f.online||(extra&&extra.online)||false,batch:f.batch||(extra&&extra.batch)||'',time:f.time||(extra&&extra.time)||''}}
  function parseCell(text){
    var s=String(text||'').replace(/\[/g,'(').replace(/\]/g,')').trim(); if(!s||s==='-') return [];
    var segs=[],buf='',depth=0,i,c;
    for(i=0;i<s.length;i++){c=s[i];
      if(c==='('){if(depth===0){if(buf.trim())segs.push(['t',buf]);buf=''}else buf+=c;depth++;continue}
      if(c===')'){if(depth>0){depth--;if(depth===0){segs.push(['g',buf]);buf=''}else buf+=c}continue}
      buf+=c}
    if(buf.trim()) segs.push([depth>0?'g':'t',buf]);
    var out=[];
    segs.forEach(function(sg){
      var parts=sg[1].split('+');
      if(sg[0]==='t'){parts.forEach(function(p){var it=item(p,null);if(it)out.push(it)});return}
      var f=flags(sg[1]),made=[];
      parts.forEach(function(p){var it=item(p,f);if(it)made.push(it)});
      if(made.length){out=out.concat(made);return}
      var last=out[out.length-1]; if(!last) return;
      if(f.online)last.online=true; if(f.batch)last.batch=f.batch; if(f.time)last.time=f.time;
    });
    return out;
  }
  function build(d){
    var classes=[],keys={};
    d.rows.forEach(function(r){r.cells.forEach(function(cell,di){
      var day=DAY3.indexOf(String(d.days[di]||'').toLowerCase().slice(0,3)); if(day<0) return;
      parseCell(cell).forEach(function(it){it.day=day;it.when=it.time||r.time;classes.push(it);keys[it.key]=it.label})})});
    var subjects=SUBJECTS.filter(function(s){return keys[s[0]]}).map(function(s){return [s[0],s[1]]});
    return {classes:classes,subjects:subjects};
  }

  /* times: Pakistan clock time on a weekday, shown in the chosen zone */
  function range(s){
    var m=/(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\s*-\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)?/i.exec(s); if(!m) return null;
    var ap=(m[6]||m[3]||'pm').toLowerCase();
    function mins(h,mm,p){h=+h%12;if(p==='pm')h+=12;return h*60+(+mm||0)}
    var a=mins(m[1],m[2],(m[3]||ap).toLowerCase()),b=mins(m[4],m[5],ap);
    if(a>=b&&a-720>=0&&a-720<b)a-=720;
    if(b<=a)b+=720;
    return [a,b];
  }
  function fmt(mn){var h=Math.floor(mn/60)%24,m=mn%60,p=h>=12?'PM':'AM',hh=h%12||12;return hh+':'+(m<10?'0':'')+m+' '+p}
  function shift(day,mn,zone){
    var z=ZONE[zone];
    if(zone==='pk') return {day:day,t:fmt(mn)};
    if(z[2]!==null){var x=mn-(300-z[2]),d=day;while(x<0){x+=1440;d=(d+6)%7}while(x>=1440){x-=1440;d=(d+1)%7}return {day:d,t:fmt(x)}}
    try{
      var ms=Date.UTC(2026,10,9+day,0,0)+(mn-300)*60000;
      var parts=new Intl.DateTimeFormat('en-GB',{timeZone:z[0],weekday:'short',hour:'numeric',minute:'2-digit',hour12:true}).formatToParts(new Date(ms)),o={};
      parts.forEach(function(p){o[p.type]=p.value});
      return {day:DAY3.indexOf(String(o.weekday).toLowerCase().slice(0,3)),t:o.hour+':'+o.minute+' '+String(o.dayPeriod||'').toUpperCase()};
    }catch(e){return {day:day,t:fmt(mn)+' (Pakistan)'}}
  }
  function daysTxt(ds){ds=ds.slice().sort();var n=ds.map(function(d){return DAY3[d].charAt(0).toUpperCase()+DAY3[d].slice(1)});return n.length>1?n.slice(0,-1).join(', ')+' & '+n[n.length-1]:n[0]}
  function slots(data){
    var G={},order=[];
    data.classes.filter(function(c){return c.key===st.subject}).forEach(function(c){
      var k=(c.online?'on':'ic')+'|'+c.batch+'|'+c.when;
      if(!G[k]){G[k]={online:c.online,batch:c.batch,when:c.when,days:[]};order.push(k)}
      if(G[k].days.indexOf(c.day)<0)G[k].days.push(c.day)});
    return order.map(function(k){return G[k]}).sort(function(a,b){return Math.min.apply(null,a.days)-Math.min.apply(null,b.days)||(range(a.when)||[0])[0]-(range(b.when)||[0])[0]});
  }
  function slotView(s){
    var r=range(s.when),zone=st.where,local='',pk='';
    if(r){
      var L={};s.days.forEach(function(d){var a=shift(d,r[0],zone),b=shift(d,r[1],zone),k=a.t+' - '+b.t;(L[k]=L[k]||[]).push(a.day)});
      local=Object.keys(L).map(function(k){return daysTxt(L[k])+' \u00b7 '+k}).join('; ');
      pk=daysTxt(s.days)+' \u00b7 '+fmt(r[0])+' - '+fmt(r[1]);
    }else{local=daysTxt(s.days)+' \u00b7 '+s.when;pk=local}
    var label=zone==='pk'?'Pakistan time':ZONE[zone][1]+' time';
    var tag=s.online?'Online batch':'Live from the Karachi class';
    if(s.batch)tag+=', batch '+s.batch;
    return {local:local+', '+label,pk:pk,tag:tag,plain:local+' '+label+(zone==='pk'?'':' ('+pk+' Pakistan time)')};
  }

  function wa(first){
    var lk=lvKey(st.level),code=CODE[lk][st.subject]||'',name=(st.data.subjects||[]).filter(function(s){return s[0]===st.subject})[0];
    var sub=(name?name[1]:'')+(code?' ('+code+')':'');
    var where=st.where==='xx'?myTz:{pk:'Pakistan',ae:'UAE',om:'Oman',sa:'Saudi Arabia',qa:'Qatar',bh:'Bahrain',kw:'Kuwait'}[st.where];
    var ref='ONL-'+LV[st.level].code+(st.where==='pk'?'':'-'+(st.where==='xx'?'XX':st.where.toUpperCase()));
    var msg="Hi SJ Academy, I'd like to book a free online demo class.\nLevel: "+LV[st.level].name+"\nSubject: "+sub+"\nSession: May/June 2027\nMode (in class or online): Online\nJoining from: "+where+(first?"\nClass time: "+first:"")+"\n(Ref: "+ref+")\nMy name is ";
    var href=WA+encodeURIComponent(msg);
    each(root.querySelectorAll('[data-onl-demo]'),function(a){a.setAttribute('href',href)});
  }
  function draw(){
    var d=st.data,out=$('onl-out');
    if(!d.subjects){return}
    if(!d.subjects.some(function(s){return s[0]===st.subject})) st.subject=d.subjects.length?d.subjects[0][0]:'';
    var sel=$('onl-subject');
    sel.innerHTML=d.subjects.map(function(s){return '<option value="'+s[0]+'"'+(s[0]===st.subject?' selected':'')+'>'+esc(s[1])+'</option>'}).join('');
    var lk=lvKey(st.level),list=slots(d),views=list.map(slotView),t=TEACH[lk][st.subject],pg=PAGE[lk][st.subject];
    var h='<ul class="onl-rows">';
    if(t) h+='<li><span>Teacher</span><span>'+esc(t)+'</span></li>';
    h+='<li><span>Classes</span><span>'+(views.length?views.map(function(v){return '<span class="onl-slot" style="display:block">'+esc(v.local)+'<small>'+esc(v.tag)+(st.where==='pk'?'':' \u00b7 '+esc(v.pk)+' in Pakistan')+'</small></span>'}).join(''):'Ask on WhatsApp for the current timing')+'</span></li>';
    h+='<li><span>Fee</span><span>'+LV[st.level].fee+' \u00b7 <a class="sj-link" href="https://www.sjacademy.pk/fee-structure/">See full fees</a></span></li>';
    if(pg) h+='<li><span>More</span><span><a class="sj-link sj-link-go" href="https://www.sjacademy.pk/'+pg+'/">About this subject</a></span></li>';
    h+='</ul>';
    out.innerHTML=h;
    wa(views.length?views[0].plain:'');
  }
  function fail(){
    $('onl-out').innerHTML='<p class="sj-small">The class times did not load. Even online classes need the internet to cooperate. See the <a class="sj-link" href="https://www.sjacademy.pk/classes-schedule/">timetable page</a>, or ask on WhatsApp and we will send your times.</p>';
    wa('');
  }
  function refresh(){
    var lv=st.level;
    $('onl-out').innerHTML='<span class="sj-skel"></span><span class="sj-skel"></span><span class="sj-skel"></span>';
    load(GID[lv],function(d){if(lv!==st.level)return;if(!d){fail();return}st.data=build(d);draw()});
  }
  each(root.querySelectorAll('input[name="onl-level"]'),function(i){i.addEventListener('change',function(){if(i.checked){st.level=i.value;refresh()}})});
  $('onl-subject').addEventListener('change',function(){st.subject=this.value;draw()});
  $('onl-where').addEventListener('change',function(){st.where=this.value;draw()});
  wa('');
  refresh();
})();
</script>
'''

STD = open('/tmp/claude-0/-home-claude/794291a6-3cee-531e-830a-45777dfe5109/scratchpad/stdscript.js').read()

faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip_tags(a)}} for q,a in FAQ]}
crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":B+"/"},{"@type":"ListItem","position":2,"name":"Online O & A Level classes","item":B+"/online-o-a-level-classes/"}]}
org = {"@type":"EducationalOrganization","name":"SJ Academy","url":B+"/","telephone":"+92-336-2144454","address":{"@type":"PostalAddress","streetAddress":"Plot 29C, Lane 5, Seher Commercial Area, DHA Phase 7","addressLocality":"Karachi","addressCountry":"PK"}}
course = {"@context":"https://schema.org","@type":"Course","name":"Online Cambridge O Level, IGCSE and A Level classes","description":"Live online O Level, IGCSE, AS and A2 classes taught by SJ Academy's Karachi teachers to students in Pakistan, the UAE, Saudi Arabia, Qatar, Oman, Bahrain and Kuwait. Online students join the same class as the Karachi classroom; classes are recorded and written answers are marked online against the Cambridge mark scheme.","url":B+"/online-o-a-level-classes/","inLanguage":"en","educationalLevel":"Cambridge O Level, Cambridge IGCSE and Cambridge International AS and A Level","provider":org,"hasCourseInstance":[{"@type":"CourseInstance","courseMode":"Online","location":{"@type":"VirtualLocation","url":B+"/online-o-a-level-classes/"}}]}
LD = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=True)}</script>\n' for x in (course, crumbs, faq_ld))

out = PAGE + "\n" + CSS + "\n" + JS + "\n" + STD + "\n" + LD

def to_ascii(s):
    res=[]
    for ch in s:
        if ord(ch) < 128: res.append(ch)
        else: res.append(f"&#{ord(ch)};")
    return "".join(res)
out = to_ascii(out)
open("online-o-a-level-classes-elementor-widget.html","w").write(out)
print(len(out.encode()), "bytes")
