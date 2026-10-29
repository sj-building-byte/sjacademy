# SJ Academy Instagram Analysis (@sjacademypk)

**Data (Meta Business Suite exports, 30 Sep 2026):**
- Posts: 373 posts published 1 Jan to 29 Sep 2026, lifetime metrics per post. `04_Data/Instagram/Instagram_Posts_Export_2026-09-30.csv`, script `05_Scripts/Analysis/instagram_analysis.py`
- Stories: 1,042 stories, same period. `04_Data/Instagram/Instagram_Stories_Export_2026-09-30.csv`, script `05_Scripts/Analysis/instagram_stories_analysis.py`
- Audience: top cities, countries, age and gender (percentages). `04_Data/Instagram/Instagram_Audience_2026-09-30.csv`
- Ads: 42 ads transcribed from 3 Meta ad-list screenshots (no date range visible). `04_Data/Instagram/Instagram_Ads_From_Screenshots_2026-09-30.csv`, screenshots in `04_Data/Instagram/Screenshots/`

**Still missing:** total follower count and growth, link-in-bio taps, DM automation results, and what happened after ad conversations (enquiries, enrolments). "Reach" totals below are the sum of per-post reach, not unique accounts. Recent posts are still accumulating lifetime numbers, so September looks lower than it will end up.

Themes were assigned from captions with keyword rules, so treat theme numbers as directional.

---

## 1. Headline numbers (Jan to Sep 2026)

| Metric | Value |
|---|---|
| Posts | 373 (about 1.4 per day): 229 carousels, 140 reels, 4 images |
| Views | 18.24M |
| Reach (sum of per-post) | 8.34M |
| Shares | 460,291 |
| Saves | 114,208 |
| Follows from posts | 13,160 |

This is a strong account for an academy: engagement per reach (about 10 to 14% on organic posts) and share rates are high. The issue is not reach. It is turning reach into followers, website visits and enquiries.

## 2. Key findings

### 2.1 Carousels grow the account; reels spread it
| Organic posts | Posts | Median views | Shares per 1k reach | Saves per 1k reach | Follows per 1k reach | Follows |
|---|---:|---:|---:|---:|---:|---:|
| Carousels | 228 | 36,452 | 50.6 | 22.6 | 1.83 | 8,270 |
| Reels | 134 | 19,627 | 82.5 | 4.1 | 0.83 | 2,329 |

Carousels delivered **78% of organic follows** and 5x the save rate. Reels get shared more but convert viewers to followers at less than half the rate. Very short reels (under 8 s) have the highest share rate (97.8 per 1k) and the lowest follow rate (0.57 per 1k).

**Yet the mix moved towards reels:** August had 37 reels vs 24 carousels, the most reel-heavy month, without a lift in median reach or follows.

### 2.2 Useful content wins saves and follows
| Organic theme | Posts | Median views | Saves per 1k | Follows per 1k |
|---|---:|---:|---:|---:|
| Tech, apps, tools | 24 | 36,118 | **42.0** | 1.83 |
| Subject / exam technique | 35 | 38,611 | 24.9 | **2.33** |
| Study plan / revision method | 41 | 28,223 | 18.8 | 1.45 |
| Careers / university | 21 | 36,297 | 16.3 | 1.25 |
| Exam news / leaks | 40 | **49,396** | 6.0 | 1.54 |
| Promo / enrolment (organic) | 34 | 35,876 | 14.2 | 1.34 |
| Memes / relatable (incl. untagged short posts) | ~70 | 21,000 to 48,000 | 7 to 10 | ~0.9 to 1.2 |
| Results / celebration | 42 | 29,577 | 9.4 | 0.86 |

**Most-saved posts** are all practical tools or methods:
1. "Stop solving O/A Level math like it's 1999": scientific calculator tricks (5,004 saves, 255 follows)
2. "Your phone can be your best study tool" (3,402 saves)
3. "You're doing past papers wrong" (2,777 saves, 216 follows)
4. "Top O Level topics that repeatedly come in exams" (2,351 saves)
5. "Career choices to pay attention to" (2,149 saves)
6. Summer plan, "started late, don't panic", 8-week A* plan, apps for 2027, C-to-A in 60 days (1,488 to 2,077 saves each)

These map almost one-to-one onto the blog pillars (Student Tech, Websites and Apps, Exam Resources, Careers). Instagram has already tested which blog topics students want.

### 2.3 Memes and results posts reach far but add few followers
They are shared heavily (64 to 76 per 1k reach) but have the lowest follow rates. Keep them for reach and brand warmth, but they shouldn't be the backbone.

### 2.4 Exam news and leak coverage is the biggest reach driver, with risk
Highest median reach of any theme (19,914). The A Level Business 9609 Paper 1 leak carousel (5 May) got 360K views, 15,236 shares and 434 follows. The Paper 2 follow-up got 171K views.

It works because students need the information. But it carries risks:
- accuracy (rumours vs confirmed facts)
- being seen to spread leaked material
- relations with Cambridge

Keep it to verified reporting and what students should do next. Never share leaked content itself.

### 2.5 Comment-to-get automation works (started June)
19 organic "comment X to get the link" posts: **median 75 comments vs 5** for other posts, and **2.40 follows per 1k reach vs 1.41**. The top ones: "UNI" (979 comments), thresholds (651), grade tool (641).

Unknown: whether those DMs capture anything (email, WhatsApp, a UTM-tagged site visit).

### 2.6 About a fifth of follows came from likely boosted posts
Ten posts show reach above views, or reach above 40K with engagement under 2%. That pattern is typical of paid promotion. Nearly all are enrolment and practicals promos. Together they brought **2,561 follows (19%)**, including the 2 March "All classes, under one roof" reel with 1,908 follows. Organic promo posts perform weakly (7.3% engagement, low shares), so paid is doing the promotional work.

Please confirm which posts were boosted and what was spent. Without spend, cost per follow and cost per lead can't be judged.

### 2.7 More posts, not more growth
| Quarter | Posts | Follows (all) | Organic follows (excl. likely boosted) | Organic follows per post |
|---|---:|---:|---:|---:|
| Q1 | 109 | 5,994 | ~3,760 | ~34 |
| Q2 | 112 | 3,743 | ~3,640 | ~32 |
| Q3 | 152 | 3,423 | ~3,200 | ~21 |

Organic follows stayed roughly flat at 3.2 to 3.8K per quarter while posting rose by 40% in Q3. Follows per post fell by about a third. Q3 is still accruing, but the trend is clear: extra volume, mostly short reels, has not added growth.

### 2.8 Instagram is not sending people to the website or into enquiries
- Only **77 of 373** captions mention the website or link in bio. Only **40** have a WhatsApp or DM call to action.
- GA4 (13 Aug to 9 Sep 2026): Organic Social sent **3,095 sessions but only 2 key events**.
- Teachers are named in only **10 captions** (Sir Salman 4, Sir Umair 3, Sir Kashan 2, Sir Sunyyan 1), although exam-technique content is the best follow driver. The teachers are the brand's strongest asset and are barely credited.

### 2.9 Timing
Differences by weekday are small. The export's time zone is not stated, so there is no reliable "best hour" conclusion. Test timing deliberately instead.


## 2A. Who the audience is (audience export)

The export does not say whether these percentages describe followers or accounts reached, and **its age brackets start at 18**. Under-18 students (most O Level and many AS students) are not represented, so the real student share is larger than shown.

**Location**
| Where | Share |
|---|---:|
| Karachi | 27.2% |
| Lahore | 13.5% |
| Islamabad + Rawalpindi | 9.5% |
| Faisalabad, Hyderabad, Multan, Peshawar, Gujranwala | 8.5% |
| Pakistan total | 75.7% |
| **Rest of Pakistan outside Karachi (derived)** | **~48.5%** |
| Outside Pakistan | ~24.3% (Bangladesh 4.2%, Saudi Arabia 1.6%, Egypt 1.5%, Brunei 1.3%, India 1.3%, UAE 1.0%, Maldives, Sri Lanka, Mauritius) |

**Age and gender (18+ only)**
| Age | Women | Men | Total |
|---|---:|---:|---:|
| 18-24 | 12.8% | 15.1% | 27.9% |
| 25-34 | 13.8% | 14.8% | 28.6% |
| **35-44** | **21.7%** | 6.5% | 28.2% |
| 45-54 | 8.9% | 3.4% | 12.3% |
| 55+ | 1.8% | 1.2% | 3.0% |
| **Total** | **59.0%** | 41.0% | |

**What it means**
1. **Parents are a core audience, above all mothers.** Women aged 35-44 are the largest single group (21.7%), and 43.5% of the adult audience is 35 or older. Parents usually decide on and pay for tuition. Yet almost no content is written for them. One of the few parent-facing posts ("That sudden grade drop isn't what you think. Your child didn't become lazy...") reached 59K views.
2. **Most of the audience can only be served online.** About half is in Pakistan outside Karachi, and another quarter is abroad (Bangladesh and the Gulf are the biggest markets that also take Cambridge exams). Only 27% can realistically attend DHA Phase 7. Instagram is the natural channel for the **nationwide online tuition** goal, but posts rarely mention online classes.
3. **Karachi is still the biggest single city** (27%), so local promotion to Karachi parents stays worthwhile, especially through paid targeting.

## 2B. Stories (stories export)

| Metric | Value |
|---|---|
| Stories | 1,042 (3.8 per day; 27 days with none) |
| Median reach per story | 616 (vs ~12,000 median reach per post) |
| Profile visits from stories | 5,444 |
| Link clicks | 3,683 (from only 101 stories with a link sticker) |
| Follows from stories | 85 |
| Replies | 384 total (median 0 per story) |
| Interactive sticker taps | 460 total; polls/quizzes appear in only ~4 captions |

**Findings**
1. **Stories reach the core audience, and it is small compared with post reach.** A typical story reaches ~600 accounts, while a typical post reaches ~12,000. Most post reach comes from non-followers (discovery), and only a small, loyal group watches stories daily. Without the total follower count, the exact share of followers who watch can't be calculated.
2. **Link stickers are the only measurable route from Instagram to the website, and they work.** Just 10% of stories had a link, but those produced 3,683 clicks, a **3.8% click rate**. Useful tools click best: grade calculator 11.6%, timetable finder 7.7%. News and petition links peaked in May (the leak story link reached 18.5%). **90% of stories carry no link at all.**
3. **News drives stories.** May (leak season) had 3x the usual median reach (1,676), 1,995 link clicks and 1,735 profile visits. Other months sit at 400 to 800 median reach.
4. **Long sequences lose some viewers, but not many.** Median reach falls from 696 on the first story of the day to ~545 by the fifth, then levels off. Up to 5 or 6 stories a day is fine. Beyond that, each extra story adds little.
5. **Stories hardly interact.** A median of 0 replies, with polls, quizzes and question boxes barely used. These are the easiest ways to learn what students and parents want, and to lift story reach.
6. **Tone risk with Cambridge.** Several May stories addressed @cambridgeint directly ("would rather call it a scam than admit that their system..."). They got high reach, but a Cambridge-teaching academy publicly accusing Cambridge carries reputational risk. Decide deliberately how confrontational the brand should be.
7. **Worth noting for the address investigation:** a 17 Feb 2026 story tagged @teachwink (reach 3,391). Given the shared-address issue, record what that story was about.


## 2C. Paid ads (42 ads from the ad list screenshots)

The screenshots show no date range, and may not include every campaign. For example, the 2 March "All classes, under one roof" reel reached 289K accounts, more than the listed ads explain. Totals below cover only the ads shown.

| Result type | Ads | Spend (PKR) | Share of spend | Results | Avg cost per result |
|---|---:|---:|---:|---:|---:|
| Messaging conversations | 20 | 184,783 | 58% | 795 conversations | PKR 232 |
| **No result reported** | **15** | **95,690** | **30%** | **0** | n/a |
| Link clicks (website visitors) | 5 | 27,662 | 9% | 5,356 clicks | PKR 5 |
| Profile visits | 2 | 11,475 | 4% | 1,052 visits | PKR 11 |
| **Total** | **42** | **319,611** | | 1.05M views | |

**Findings**
1. **30% of spend (PKR 95,690) went to ads that report no results.** Almost all of these used the **"Get more leads through messaging"** objective. The largest is "Register for O/A Level and IGCSE" (PKR 51,441, 110,591 viewers, 0 results). It matches the 17 July reel that reached 234K views in the organic export. Other examples: "Join Sir Salman's A Level Physics" (PKR 13,407) and "Join SJ Academy to achieve..." (PKR 5,996).

   "No result" does not necessarily mean nobody messaged. This objective only counts a lead when someone completes the lead questions set up in the chat flow. If those aren't set up, or people just chat, Meta reports nothing. Either way, this spend can't be measured. Check "View insights" on #31 to see whether conversations started.
2. **Messaging ads work, at very different costs.** 795 conversations at PKR 232 on average. The best cost PKR 100 to 150 per conversation, and all have a clear, timely offer:
   - Registration Open (no offer): PKR 101
   - Practicals post: PKR 127
   - Registration Open, early-bird discount: PKR 134, 76 conversations
   - **May/June 2027 batches: PKR 150, 225 conversations (the best volume)**
   - Comment "link": PKR 150

   The worst were the A Level Science practicals messaging ads: **PKR 1,207** and PKR 502 per conversation. Yet the same creative with a "website visitors" objective got clicks at **PKR 2.99**. That audience clicks but doesn't message.
3. **Website-visitor ads are the cheapest traffic (PKR 3 to 6 per click, 5,356 clicks),** but it isn't known whether those clicks became landing-page visits or enquiries. There are no UTM tags, and GA4 shows almost no social conversions.
4. **Ads built in Ads Manager (by Sunyyan Junaid)** perform steadily at PKR 100 to 236 per conversation, and cover "Physics 2027 Online" and "Maths O Level 2027". Boosts from the Instagram app vary much more, including most of the no-result spend.
5. **The key number is missing: enrolments.** PKR 232 per conversation only means something next to how many conversations became demo bookings and enrolments.

**What to change**
- **Stop using "Get more leads through messaging"** unless the lead questions are set up and tested. Use the **Messages (conversations) objective** that already delivers PKR 100 to 250 conversations.
- **Put budget behind what works:** timely batch/registration offers ("May/June 2027 batches", "Registration open"), subject-specific online classes (Physics, Maths) and comment-to-get posts. Pause any messaging ad above about PKR 300 per conversation after a few days.
- **Science practicals:** run them as website-visitor ads to a practicals landing page (clicks cost PKR 3), with a clear WhatsApp button on the page, instead of paying PKR 500 to 1,200 per chat.
- **Tag every website ad with UTMs** (e.g. `utm_source=instagram&utm_medium=paid&utm_campaign=mj27_batches`) so GA4 shows landing-page visits, WhatsApp clicks and form submissions per ad.
- **Label every ad conversation** in WhatsApp Business/Instagram DMs with the ad name ("MJ27 batches", "Physics online"). Record weekly how many became demo bookings and enrolments. That gives **cost per enrolment**, the number that decides budgets.
- **Split targeting to match the audience data:** a Karachi campaign (physical + online, parents 35+ included) and a Pakistan/abroad campaign (online classes).

---

## 3. Recommendations

1. **Make useful carousels the backbone (about 50% of posts).** Tech and tools, exam technique, study methods, careers. Design each one to be saved: checklists, step-by-steps, "save this before your next paper".
2. **Put teachers on camera, by name.** A weekly teacher-tip reel (15 to 60 s) per core subject, credited in the caption ("Sir Salman, A Level Maths"). This builds trust for tuition and the E-E-A-T signals the blog needs.
3. **Keep memes, news and results for reach (about 25 to 30%), and give them a job.** Each should point somewhere: a follow CTA, a related carousel or a resource. Cover leaks with verified facts only.
4. **Scale comment-to-get, and capture the lead.** The DM should deliver a UTM-tagged link to the blog post or tool. Offer WhatsApp updates as an opt-in. Track comments, then link clicks, then site sessions, then leads.
5. **Connect Instagram to the website and GA4.**
   - Point the link in bio to a simple UTM-tagged links page on sjacademy.pk.
   - Use story link stickers on resource posts, and one website or WhatsApp CTA on every useful post.
   - Create a GA4 exploration for Instagram-referred sessions and leads.
6. **Build a blog and Instagram pipeline.**
   - Every top-saved carousel becomes (or links to) a blog post, and every blog post gets a carousel.
   - Direct matches already in the blog calendar:
     - calculator carousel (5,004 saves) → "Best Calculators for O and A Level" (5 to 9 Oct week)
     - phone and apps carousels → "Best Study Apps" (2 Nov week)
     - "past papers wrong" → mark scheme guide refresh
     - careers carousel → careers posts
     - memes → shareable posts
7. **Post fewer, better posts.** About one a day, with 4 to 5 carousels a week. Stop adding low-effort short reels that don't earn follows.
8. **Fix paid measurement and objectives (see 2C).** Stop the lead-messaging objective that reported nothing on 30% of spend, use Messages or website-visitor objectives, add UTMs, and track cost per enrolment.
9. **Create content for parents (new, from the audience data).** About 2 posts a week for parents, especially mothers: how to support revision, reading grade thresholds, choosing subjects, tuition costs, online vs physical classes, IBCC. Also use parent-targeted paid promotion for enrolment.
10. **Lead with online classes for the ~73% outside Karachi.** Mention live online classes in bios, promos and teacher reels. Consider separate enrolment promos: Karachi parents (physical and online) vs the rest of Pakistan and abroad (online).
11. **Put a link sticker on at least 1 story a day.** Link today's blog post, tool or resource with a UTM tag (e.g. `utm_source=instagram&utm_medium=story`). At the current 3.8% click rate, one link story a day at ~600 reach adds roughly 700 site visits a month, more in exam seasons.
12. **Use interactive stickers daily.** Polls, quizzes (past-paper questions) and question boxes ("Ask Sir Salman a Maths question"). Use the answers to choose blog and carousel topics.
13. **Keep stories to about 5 or 6 a day,** with the most important one (link or CTA) first.
14. **Get the remaining data.** Follower count and growth, link-in-bio taps, and the enrolments that came from ad conversations.

## 4. Suggested weekly Instagram template (about 7 posts)

| Day | Post | Purpose |
|---|---|---|
| Mon | Useful carousel (tech, apps, tools) tied to the week's blog post, plus link story | Saves, follows, affiliate/blog traffic |
| Tue | Teacher tip reel (named teacher, one subject) | Trust, tuition |
| Wed | Exam technique carousel (subject-specific) | Follows, saves |
| Thu | Meme or relatable reel (with follow CTA) | Reach, shares |
| Fri | Parent-focused carousel (supporting your child, costs, online vs physical, IBCC), or study plan / careers carousel | Parents, enquiries |
| Sat | Comment-to-get post (tool, resource, blog link) | Comments, leads |
| Sun | News/update or results/community post (seasonal), or boosted enrolment promo | Reach, enquiries |

**Stories, every day:** 5 or 6 frames: 1 link sticker (blog post, tool or resource with UTM), 1 interactive sticker (poll, quiz or question box), plus reshares and behind-the-scenes.

Adjust around the exam calendar: more news, results and comment-to-get in results months (January, August), and more revision plans and teacher tips in exam run-ups (March to May, September to October).
