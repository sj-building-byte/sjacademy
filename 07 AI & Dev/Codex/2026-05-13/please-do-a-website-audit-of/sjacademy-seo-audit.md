# SJ Academy SEO Audit and Working Sitemap

Audit date: 13 May 2026  
Site: https://www.sjacademy.pk/

## Executive Summary

SJ Academy has a strong SEO foundation for commercial education queries in Karachi. The site already targets the right money pages: O Level hub, A Level hub, individual subject pages, A Level lab practicals, schedule, past papers, tools, and education blog content.

The biggest wins are not a full rebuild. They are consolidation, crawl hygiene, better internal linking, and filling subject-page gaps. The current structure has some duplicate or legacy pages, repeated hidden form text appearing in crawlable content, and inconsistent navigation between what the academy offers and what has dedicated SEO landing pages.

## High-Priority Findings

1. Duplicate or competing O Level hubs

There is an older `/o-levels/` page and a newer, stronger `/o-level-tuition-center-karachi/` page. This can split ranking signals for "O Level tuition center in Karachi".

Recommendation: choose `/o-level-tuition-center-karachi/` as the canonical hub. Redirect or canonicalize `/o-levels/` if it is no longer needed.

2. Hidden forms are polluting crawlable text

Many pages expose long registration form text, payment details, repeated bank information, and "Please enable JavaScript" content in the text crawl. This dilutes the page topic and may make search snippets messy.

Recommendation: move modal/form content out of the static page body where possible, lazy-load it, or set form containers to avoid being indexed as primary page content. Keep one dedicated registration page for the full form.

3. Subject coverage is uneven

The A Level structure is stronger than O Level. O Level Math, Physics, Chemistry, Pakistan Studies, and Islamiat have visible pages, but offered subjects such as Biology, Computer Science, Business, Economics, Accounting, Urdu, English, and Add Maths should each have dedicated pages if they are actively offered.

Recommendation: create missing subject pages using the same pattern as the strong Math pages: parent pain points, syllabus coverage, past-paper practice, teacher profile, FAQs, CTA.

4. Navigation and footer labels are inconsistent

The footer references "Physics (5056)" in one place while the main O Level page uses Physics (5054). Some pages show different resource menus, for example CAIE Date Sheet and Past Papers appear on some menus but not others.

Recommendation: normalize syllabus codes and global navigation across templates.

5. Seasonal content needs lifecycle management

Pages and banners mention May/June 2026 workshops and admissions. These are valuable now, but will become stale quickly.

Recommendation: after each session, update the page title/body or redirect old campaign pages to the evergreen practicals hub.

## Recommended Site Architecture

Home

- O Level Tuition Center in Karachi
- A Level Tuition Center in Karachi
- A Level Lab Practicals
- Class Schedule
- Past Papers
- Blog
- Contact
- Registration

O Level hub

- O Level Math Tuition
- O Level Physics Tuition
- O Level Chemistry Tuition
- O Level Pakistan Studies Tuition
- O Level Islamiat Tuition
- O Level Biology Tuition
- O Level Computer Science Tuition
- O Level Business Studies Tuition
- O Level Economics Tuition
- O Level Accounting Tuition
- O Level English Tuition
- O Level Add Maths Tuition
- O Level Urdu Tuition

A Level hub

- A Level Math Tuition
- A Level Physics Tuition
- A Level Chemistry Tuition
- A Level Biology Tuition
- A Level Computer Science Tuition
- A Level Business Tuition
- A Level Economics Tuition
- A Level Accounting Tuition
- A Level Sociology Tuition
- A Level Psychology Tuition
- A Level Law Tuition
- A Level English General Paper Tuition

A Level Practicals

- Main A Level Lab Practicals hub
- A Level Physics Practicals
- A Level Chemistry Practicals
- A Level Biology Practicals
- Seasonal workshop pages such as May/June and Oct/Nov

Resources

- A Level Past Papers
- O Level Past Papers
- CAIE Zone 4 Timetable
- A Level Subject Combinations Tool
- University Admission Criteria Tool
- Periodic Table
- A Level Business Quiz
- eBooks

Trust and Local SEO

- Reviews
- Teachers / Faculty
- Results / Success Stories
- DHA Karachi tuition page
- Clifton Karachi tuition page
- Online O and A Level tuition page

## Page Template for New Subject Pages

Use this structure for every new subject page:

1. H1: "[Subject] Tuition in Karachi | SJ Academy"
2. Short intro: who it is for, level, online/in-class availability
3. Student pain points: why students lose marks in this subject
4. Syllabus coverage: Cambridge code, paper breakdown, topic list
5. Past paper strategy: how practice is handled
6. Teacher profile: credentials, experience, outcomes
7. Proof: testimonials, A/A* results, reviews
8. FAQs: fees, batch size, online options, schedule, registration
9. CTA: free demo, WhatsApp, class schedule
10. Internal links: hub page, past papers, schedule, registration

## Internal Linking Plan

- Home links to the two major commercial hubs, practicals, schedule, and past papers.
- O Level hub links to every O Level subject page and relevant O Level blog guides.
- A Level hub links to every A Level subject page, subject combinations tool, university criteria tool, and A Level past papers.
- Each subject page links to its relevant past papers, schedule, registration, and the parent hub.
- Practical pages link to A Level Physics, Chemistry, Biology, and the general lab practicals hub.
- Blog posts should include contextual CTAs, not only footer links.

## Schema Recommendations

- LocalBusiness / EducationalOrganization on homepage and contact page.
- Course schema on each subject tuition page.
- FAQPage schema on hubs, subject pages, practicals, and contact.
- BreadcrumbList schema sitewide.
- Article schema on blog posts.
- Review schema only if it follows Google guidelines and reviews are directly shown on page.

## Content Opportunities

High intent:

- O Level Biology Tuition Karachi
- O Level Computer Science Tuition Karachi
- O Level Add Maths Tuition Karachi
- IELTS Preparation Karachi
- Online O Level Tuition Pakistan
- Online A Level Tuition Pakistan

Supporting informational:

- O Level subject selection guide
- A Level subject combinations for medicine, engineering, business, law, CS
- CAIE Paper 3 and Paper 5 practical guide by subject
- How to use past papers effectively for O Levels
- How to move from C/D grade to A/A* in Math, Physics, Chemistry

Local:

- Best O Level academy in DHA Karachi
- A Level tuition near Clifton Karachi
- O and A Level coaching near Phase 7 DHA

## Technical SEO Checklist

- Confirm XML sitemap is live and submitted in Google Search Console.
- Confirm robots.txt references the XML sitemap.
- Crawl the site with Screaming Frog or Sitebulb to check status codes, canonicals, duplicate titles, duplicate H1s, and indexability.
- Remove repeated form/payment text from non-form pages.
- Add or verify canonical tags on duplicated hubs and seasonal pages.
- Compress and rename images with descriptive alt text.
- Check Core Web Vitals on mobile, especially pages with large images, forms, widgets, and chat.
- Update copyright/footer year consistently.

## Working Files

- Sitemap CSV: `sjacademy-seo-sitemap.csv`
- This audit: `sjacademy-seo-audit.md`

