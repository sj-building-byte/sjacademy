const universityData = [
    // --- LUMS - Business Programs (SDSB) ---
    {
        university: "LUMS",
        program: "BSc (Honours) Management Science",
        group: "Business/SDSB",
        aLevel: {
            minSubjects: "3 Full-Credit A-Level Subjects",
            requiredSubjects: "Any three full-credit A-Level subjects. (Maths is highly recommended).",
            gradeRequirement: "Average of 2 B's and 1 C grade across the best three full-credit A-Level subjects (No grade less than 'E').",
            oLevelRequirement: "Minimum 8 subjects with an average grade of at least 'B'. IBCC Equivalence is mandatory.",
            testRequirement: "LCAT or SAT/ACT is mandatory.",
            additionalNotes: "The three best subjects cannot include Advanced Subsidiary (AS) or General Paper (GP). Accepted into a Business stream."
        }
    },
    {
        university: "LUMS",
        program: "BSc (Honours) Accounting and Finance",
        group: "Business/SDSB",
        aLevel: {
            minSubjects: "3 Full-Credit A-Level Subjects",
            requiredSubjects: "Any three full-credit A-Level subjects. (Maths or Accounting highly recommended).",
            gradeRequirement: "Average of 2 B's and 1 C grade across the best three full-credit A-Level subjects (No grade less than 'E').",
            oLevelRequirement: "Minimum 8 subjects with an average grade of at least 'B'. IBCC Equivalence is mandatory.",
            testRequirement: "LCAT or SAT/ACT is mandatory.",
            additionalNotes: "The three best subjects cannot include AS or GP. Accepted into a Business stream."
        }
    },

    // --- LUMS - Science & Engineering Programs (SBASSE) ---
    {
        university: "LUMS",
        program: "BS Computer Science (SBASSE)",
        group: "Science/SBASSE",
        aLevel: {
            minSubjects: "3 Full-Credit A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and one Science/Engineering subject (e.g., Chemistry or Computer Science).",
            gradeRequirement: "Average of 2 B's and 1 C grade across the best three full-credit A-Level subjects (No grade less than 'E').",
            oLevelRequirement: "Minimum 8 subjects with an average grade of at least 'B'. IBCC Equivalence for **Science** subjects is mandatory.",
            testRequirement: "LCAT or SAT/ACT is mandatory.",
            additionalNotes: "IBCC Equivalence must be equivalent to the Pre-Engineering or Pre-Medical stream (depending on major)."
        }
    },
    {
        university: "LUMS",
        program: "BS Electrical Engineering (SBASSE)",
        group: "Science/SBASSE",
        aLevel: {
            minSubjects: "3 Full-Credit A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and Chemistry are strongly recommended.",
            gradeRequirement: "Average of 2 B's and 1 C grade across the best three full-credit A-Level subjects (No grade less than 'E').",
            oLevelRequirement: "Minimum 8 subjects with an average grade of at least 'B'. IBCC Equivalence for **Pre-Engineering** is mandatory.",
            testRequirement: "LCAT or SAT/ACT is mandatory.",
            additionalNotes: "IBCC Equivalence must be equivalent to the Pre-Engineering Stream."
        }
    },

    // --- LUMS - Humanities & Social Sciences Programs (MGSHSS) ---
    {
        university: "LUMS",
        program: "BA (Honours) Economics / Political Science / History / CLCA",
        group: "Humanities/MGSHSS",
        aLevel: {
            minSubjects: "3 Full-Credit A-Level Subjects",
            requiredSubjects: "Any three full-credit A-Level subjects.",
            gradeRequirement: "Average of 2 B's and 1 C grade across the best three full-credit A-Level subjects (No grade less than 'E').",
            oLevelRequirement: "Minimum 8 subjects with an average grade of at least 'B'. IBCC Equivalence is mandatory.",
            testRequirement: "LCAT or SAT/ACT is mandatory.",
            additionalNotes: "Students are admitted into a general HSS stream and choose their major later."
        }
    },

    // --- IBA - Business Programs ---
    {
        university: "IBA Karachi",
        program: "BBA (Bachelor of Business Administration)",
        group: "Business/IBA",
        aLevel: {
            minSubjects: "3 Principal A-Level Subjects",
            requiredSubjects: "Any three principal A-Level subjects.",
            gradeRequirement: "Minimum of **2 B's and 1 C** across the three principal subjects (No grade less than 'C').",
            oLevelRequirement: "Minimum 65% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "IBA Aptitude Test (Maths and English) is mandatory.",
            additionalNotes: "SAT exemption policy applies for high scores (Composite 1200+ and specific section scores)."
        }
    },
    {
        university: "IBA Karachi",
        program: "BS Accounting & Finance (BSAF)",
        group: "Business/IBA",
        aLevel: {
            minSubjects: "3 Principal A-Level Subjects",
            requiredSubjects: "Any three principal A-Level subjects. Maths highly recommended.",
            gradeRequirement: "Minimum of **2 B's and 1 C** across the three principal subjects (No grade less than 'C').",
            oLevelRequirement: "Minimum 65% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "IBA Aptitude Test (Maths and English) is mandatory.",
            additionalNotes: "This program has strong exemptions from professional bodies (ICAP/ACCA/CIMA)."
        }
    },

    // --- IBA - Science & Computing Programs ---
    {
        university: "IBA Karachi",
        program: "BS Computer Science (BSCS)",
        group: "Computing/IBA",
        aLevel: {
            minSubjects: "3 Principal A-Level Subjects",
            requiredSubjects: "Must include **Mathematics** as one of the three principal subjects.",
            gradeRequirement: "Minimum of **1 B and 2 C's** across the three principal subjects (No grade less than 'C').",
            oLevelRequirement: "Minimum 60% in HSSC equivalence. Background must be Pre-Engineering or General Group with Mathematics.",
            testRequirement: "IBA Aptitude Test (Maths and English) is mandatory.",
            additionalNotes: "IBCC Equivalence must be equivalent to the Pre-Engineering or General Group with Mathematics."
        }
    },
    {
        university: "IBA Karachi",
        program: "BS Economics & Mathematics",
        group: "Social Sciences/IBA",
        aLevel: {
            minSubjects: "3 Principal A-Level Subjects",
            requiredSubjects: "Must include **Mathematics** as one of the three principal subjects.",
            gradeRequirement: "Minimum of **1 B and 2 C's** across the three principal subjects (No grade less than 'C').",
            oLevelRequirement: "Minimum 60% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "IBA Aptitude Test (Maths and English) is mandatory.",
            additionalNotes: "This is a quantitative social science degree."
        }
    },

    // --- NUST Requirements (Retained for completeness) ---
    {
        university: "NUST",
        program: "Engineering Programmes (All Disciplines)",
        group: "Engineering",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and Chemistry (or Computer Science if applying for Computing programs).",
            gradeRequirement: "Minimum 60% aggregate marks in HSSC equivalence. IBCC Equivalence is mandatory.",
            oLevelRequirement: "SSC / O-Levels (Science Group) is required. Minimum 60% aggregate marks in SSC equivalence.",
            testRequirement: "NUST Entry Test (NET-Engineering) is mandatory.",
            additionalNotes: "Merit is based on 75% NET score and 25% Academic score. Must qualify in relevant A-Level subjects for equivalence."
        }
    },

    // --- FAST National University (NUCES) Requirements ---
    {
        university: "FAST (NUCES)",
        program: "BS Computer Science / AI / Data Science / SE",
        group: "Computing",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics is mandatory at HSSC/A-Level equivalent.",
            gradeRequirement: "Minimum 50% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "FAST-NUCES Admission Test is mandatory (50% weightage) OR valid SAT score.",
            additionalNotes: "Merit is 50% Test Score, 40% HSSC/A-Level, 10% SSC/O-Level."
        }
    },
    {
        university: "FAST (NUCES)",
        program: "BBA / BS Accounting & Finance / Business Analytics",
        group: "Business/Management",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any combination of subjects. Mathematics is not mandatory but helpful.",
            gradeRequirement: "Minimum 50% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "FAST-NUCES Admission Test is mandatory (50% weightage) OR valid SAT score.",
            additionalNotes: "Merit is 50% Test Score, 40% HSSC/A-Level, 10% SSC/O-Level. Test includes English, Analytical, and Basic Math."
        }
    },
    {
        university: "FAST (NUCES)",
        program: "BS Engineering Programs (Electrical / Civil / Computer)",
        group: "Engineering",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Pre-Engineering equivalent: Mathematics, Physics, and Chemistry (or Computer Science for Comp. Engg.).",
            gradeRequirement: "Minimum 60% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "FAST-NUCES Admission Test is mandatory (33% weightage).",
            additionalNotes: "Merit is 33% Test Score, 50% HSSC/A-Level, 17% SSC/O-Level, as per PEC guidelines."
        }
    },

    // --- Aga Khan University (AKU) Requirements ---
    {
        university: "AKU (Aga Khan University)",
        program: "MBBS (Bachelor of Medicine, Bachelor of Surgery)",
        group: "Medical",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Science stream (Biology, Chemistry, Physics/Maths).",
            gradeRequirement: "IBCC Equivalence with at least B grades in Biology, Chemistry, and Physics/Mathematics.",
            testRequirement: "AKU Admission Test is mandatory (70% weightage).",
            additionalNotes: "Academic performance (FSc Pre-Medical or A-Level equivalent) is 30% of merit. Minimum 70% in FSc Pre-Medical or equivalent is required."
        }
    },
    {
        university: "AKU (Aga Khan University)",
        program: "Pre-University Programmes (General Eligibility)",
        group: "General",
        aLevel: {
            minSubjects: "6 O-Level/IGCSE Subjects",
            requiredSubjects: "Evidence of completing 6 subjects in O-Levels/IGCSE.",
            gradeRequirement: "Minimum 'B' grade in at least four of the 6 O-Level/IGCSE subjects, including English.",
            testRequirement: "AKU Admission Test is required for shortlisting (70% weightage).",
            additionalNotes: "Accepts provisional applications from students writing exams in 2025. This is a general guide; specific degree requirements vary."
        }
    },

    // --- GIKI (Ghulam Ishaq Khan Institute) Requirements ---
    {
        university: "GIKI (Top Engineering)",
        program: "BS Engineering Programs (All Disciplines)",
        group: "Engineering/CS",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and Chemistry/Computer Studies/IT.",
            gradeRequirement: "Overall 60% equivalence as per IBCC formula. D grade or above in Mathematics & Physics.",
            testRequirement: "GIK Institute Admission Test (85% weightage) OR SAT-II (Maths IIC & Physics).",
            additionalNotes: "IBCC equivalence is mandatory. Merit is 85% Test Score + 15% Academic Score."
        }
    },
    {
        university: "GIKI (Top Engineering)",
        program: "BS Computer Science / AI / Cyber Security",
        group: "Computing",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and any other subject.",
            gradeRequirement: "Overall 60% equivalence as per IBCC formula. D grade or above in Mathematics & Physics.",
            testRequirement: "GIK Institute Admission Test (85% weightage) OR SAT-II (Maths IIC & Physics).",
            additionalNotes: "Equivalent to Pre-Engineering/ICS background. Merit is 85% Test Score + 15% Academic Score."
        }
    },
    {
        university: "GIKI (Top Engineering)",
        program: "BS Management Sciences",
        group: "Management/Business",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any subject combination.",
            gradeRequirement: "Overall 60% equivalence as per IBCC formula.",
            testRequirement: "GIK Common Admissions Test (GCAT) OR SAT-II (in any two subjects).",
            additionalNotes: "GCAT measures reading, writing, and mathematical skills."
        }
    },

    // --- COMSATS University Islamabad (CUI) Requirements ---
    {
        university: "COMSATS Islamabad (CUI)",
        program: "BS Engineering Programs (PEC Accredited)",
        group: "Engineering",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Pre-Engineering equivalent: Mathematics, Physics, Chemistry.",
            gradeRequirement: "Minimum 60% in HSSC equivalence. IBCC equivalence is mandatory.",
            testRequirement: "NTS NAT-IE or SAT I with minimum score of 1200.",
            additionalNotes: "Admission is based on merit of NAT/SAT score and Academic record."
        }
    },
    {
        university: "COMSATS Islamabad (CUI)",
        program: "BS Computer Science / Data Science / AI",
        group: "Computing",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics at HSSC/A-Level equivalent.",
            gradeRequirement: "Minimum 50% in HSSC equivalence. IBCC equivalence is mandatory.",
            testRequirement: "NTS NAT-ICS or SAT I.",
            additionalNotes: "Students with Pre-Medical who have passed additional Maths are eligible."
        }
    },
    {
        university: "COMSATS Islamabad (CUI)",
        program: "BBA / BS Accounting & Finance",
        group: "Business",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any combination of subjects.",
            gradeRequirement: "Minimum 50% in HSSC equivalence. IBCC equivalence is mandatory.",
            testRequirement: "NTS NAT I or SAT I.",
            additionalNotes: "Merit lists are prepared based on the NTS/SAT scores and academic record."
        }
    },

    // --- UET Lahore (University of Engineering & Technology) Requirements ---
    {
        university: "UET Lahore",
        program: "BSc Engineering Programs (All Disciplines)",
        group: "Engineering",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Physics, Mathematics, and Chemistry/Computer Science.",
            gradeRequirement: "Minimum 60% in HSSC equivalence. IBCC equivalence is mandatory with minimum 'C' grades in required subjects.",
            testRequirement: "ECAT (Engineering College Admission Test) is **mandatory**.",
            additionalNotes: "Merit is typically 70% HSSC/A-Level marks and 30% ECAT score. Only Punjab domiciled applicants are eligible for most programs."
        }
    },
    {
        university: "UET Lahore",
        program: "BS Computer Science / Applied Computing",
        group: "Computing",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics is mandatory. Pre-Engineering or ICS equivalent.",
            gradeRequirement: "Minimum 50% in HSSC equivalence. IBCC equivalence is mandatory.",
            testRequirement: "ECAT is required for most computing programs.",
            additionalNotes: "Check specific campus (Lahore/Faisalabad) requirements as they can differ."
        }
    },

    // --- King Edward Medical University (KEMU) / Public Medical Requirements ---
    {
        university: "KEMU (Public Medical)",
        program: "MBBS / BDS",
        group: "Medical",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Biology, Chemistry, and Physics (or Mathematics). Pre-Medical equivalent is mandatory.",
            gradeRequirement: "Minimum 60% aggregate in HSSC equivalent (A-Levels). IBCC Equivalence is mandatory.",
            testRequirement: "MDCAT (Medical and Dental College Admission Test) is **mandatory**.",
            additionalNotes: "Admission merit is heavily based on MDCAT score (50%) and academic performance. Only specific provincial domiciles are eligible for quota seats."
        }
    },
    {
        university: "KEMU (Public Medical)",
        program: "Allied Health Sciences (AHS)",
        group: "Allied Health",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Science subjects (Pre-Medical background equivalent).",
            gradeRequirement: "Minimum 60% aggregate in HSSC equivalent (A-Levels). IBCC Equivalence is mandatory.",
            testRequirement: "KEMU's or Provincial Entry Test may be required.",
            additionalNotes: "Merit is typically calculated based on FSc/A-Level equivalence marks. Requires a strong background in sciences."
        }
    },

    // --- University of Karachi (UoK) / Public General Requirements ---
    {
        university: "University of Karachi (UoK)",
        program: "BS Computer Science (BSCS)",
        group: "Computing",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics is mandatory. Pre-Engineering or ICS equivalent.",
            gradeRequirement: "Minimum 50% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "UoK Pre-Admission Test is mandatory for highly competitive programs.",
            additionalNotes: "Admission merit is 50% based on the UoK Test score and 50% academic record. Test includes General Knowledge, English, and Aptitude."
        }
    },
    {
        university: "University of Karachi (UoK)",
        program: "BBA / BS Commerce / Business",
        group: "Business/Commerce",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any subject combination.",
            gradeRequirement: "Minimum 45% to 50% in HSSC equivalence, depending on the program. IBCC Equivalence is mandatory.",
            testRequirement: "UoK Pre-Admission Test is required for Business/Commerce disciplines.",
            additionalNotes: "Admission policies and merit percentages can vary significantly by department. Strong test performance is key."
        }
    },
    {
        university: "University of Karachi (UoK)",
        program: "BS/BA Programs (Arts, Humanities, Social Sciences)",
        group: "General/Arts",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any subject combination.",
            gradeRequirement: "Minimum 45% in HSSC equivalence. IBCC Equivalence is mandatory.",
            testRequirement: "No test generally required for non-professional degrees, but required for specific departments (e.g., Law, Mass Comms).",
            additionalNotes: "Admission is primarily merit-based on academic record."
        }
    },

    // --- University of Toronto (UoT), Canada Requirements ---
    {
        university: "University of Toronto (Canada)",
        program: "Engineering, Computer Science, and Science",
        group: "International Science/Engineering",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and one other subject (e.g., Chemistry or Computer Science).",
            gradeRequirement: "A*AA to AAA is generally required for competitive programs. Admission is based on predicted and final grades.",
            testRequirement: "No separate admissions test required. Admission is based primarily on grades and a supplementary application/essay.",
            additionalNotes: "O-Level/IGCSE is also assessed. Requires strong English proficiency test scores (IELTS/TOEFL)."
        }
    },
    {
        university: "University of Toronto (Canada)",
        program: "Rotman Commerce / Arts & Science",
        group: "International Business/Arts",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Rotman Commerce often requires Mathematics. Arts & Science is more flexible.",
            gradeRequirement: "AAA to AAB is generally required for competitive programs.",
            testRequirement: "No separate admissions test required. Supplementary application is mandatory.",
            additionalNotes: "Competition is extremely high. Final admission decision is based on a holistic review of grades and application documents."
        }
    },

    // --- University of Manchester (UK) Requirements ---
    {
        university: "University of Manchester (UK)",
        program: "M.Eng. / BSc Computer Science",
        group: "International UK",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics is mandatory. Further Maths or Physics often recommended.",
            gradeRequirement: "A*AA to AAA is the standard offer. Offers are made based on predicted grades.",
            testRequirement: "No separate test required, but STEP (for Maths/CS) may be requested for conditional offers.",
            additionalNotes: "Requires application via UCAS. Students must meet English language requirements (IELTS/PTE)."
        }
    },
    {
        university: "University of Manchester (UK)",
        program: "BSc Business & Management / Accounting & Finance",
        group: "International UK",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any three subjects. Mathematics is highly desirable for Finance programs.",
            gradeRequirement: "AAB to AAA is the standard offer.",
            testRequirement: "No separate test required. Admission is based on grades and UCAS Personal Statement.",
            additionalNotes: "Accepts O-Level English grade C or equivalent for English requirement if not met by IELTS/TOEFL."
        }
    },

    // --- Monash University (Australia) Requirements ---
    {
        university: "Monash University (Australia)",
        program: "Engineering / IT / Science",
        group: "International Australia",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Prerequisites often include Mathematics and Physics/Chemistry (depending on the course).",
            gradeRequirement: "The required aggregate is calculated using a Monash formula based on the best three A-Levels. Typically equates to AAB or higher.",
            testRequirement: "No separate test required. Monash uses a calculated ATAR equivalent.",
            additionalNotes: "Accepts 5 O-Levels at grade C or higher. Must meet English language requirements (IELTS/TOEFL)."
        }
    },
    {
        university: "Monash University (Australia)",
        program: "Business / Commerce / Arts",
        group: "International Australia",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any three subjects.",
            gradeRequirement: "The required aggregate is calculated using a Monash formula. Typically equates to AAB to BBB.",
            testRequirement: "No separate test required. Admission is based on academic history.",
            additionalNotes: "Admission is competitive. Requires strong academic transcripts and proof of English proficiency."
        }
    },

    // --- PIEAS (Pakistan Institute of Engineering & Applied Sciences) Requirements ---
    {
        university: "PIEAS (Elite Engineering)",
        program: "BS Engineering & Sciences (Physics, Elec. Engg., CS)",
        group: "Engineering/Sciences",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Physics, Chemistry, and Mathematics (for all engineering/science programs).",
            gradeRequirement: "Minimum 60% aggregate in HSSC equivalent (A-Levels). IBCC Equivalence is mandatory.",
            testRequirement: "PIEAS Admission Test is **mandatory** (60% weightage) OR SAT Subject Test scores in Physics, Chemistry/Maths.",
            additionalNotes: "Merit is heavily test-based. Academic record (40% weightage) requires strong grades in science subjects."
        }
    },

    // --- NED University of Engineering & Technology Requirements ---
    {
        university: "NED University (Karachi)",
        program: "BE/BS Engineering Programs (Civil, Mech, Elec, etc.)",
        group: "Engineering",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and Chemistry/Computer Science (Pre-Engineering/ICS equivalent).",
            gradeRequirement: "Minimum 60% in HSSC equivalent (A-Levels) for Engineering/CS. Minimum 55% for other BS programs.",
            testRequirement: "NED Entry Test is **mandatory** (50% weightage). Qualifying score must be achieved.",
            additionalNotes: "Merit is 50% HSSC/A-Level equivalence and 50% NED Entry Test score. IBCC Equivalence with minimum 'C' grades is required."
        }
    },
    {
        university: "NED University (Karachi)",
        program: "BS Computer Science / Software Engineering",
        group: "Computing",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematics, Physics, and Computer Science (or Pre-Engineering equivalent).",
            gradeRequirement: "Minimum 60% in HSSC equivalent (A-Levels).",
            testRequirement: "NED Entry Test is mandatory (50% weightage).",
            additionalNotes: "Same merit formula as Engineering. Students must appear in the relevant test section (e.g., Computer Science)."
        }
    },

    // --- SZABIST (Shaheed Zulfikar Ali Bhutto Institute) Requirements ---
    {
        university: "SZABIST (Business & Computing)",
        program: "BBA / BS Accounting & Finance / Media Sciences",
        group: "Business/Media",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Any three subjects. No specific subject required for BBA.",
            gradeRequirement: "Minimum 50% marks in HSSC equivalent (A-Levels). IBCC Equivalence is mandatory.",
            testRequirement: "SZABIST Entrance Test and Interview are **mandatory**.",
            additionalNotes: "The test includes English, Math, and General Knowledge. Strong performance in the test is key for admission."
        }
    },
    {
        university: "SZABIST (Business & Computing)",
        program: "BS Computer Science / Software Engineering / AI",
        group: "Computing",
        aLevel: {
            minSubjects: "3 A-Level Subjects",
            requiredSubjects: "Mathematical background is preferred (Mathematics at A-Level/Intermediate equivalent).",
            gradeRequirement: "Minimum 50% marks in HSSC equivalent (A-Levels).",
            testRequirement: "SZABIST Entrance Test and Interview are mandatory.",
            additionalNotes: "Students without Mathematics background may have to take deficiency courses."
        }
    },
];

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get references to DOM elements
    const universitySelect = document.getElementById('university');
    const programSelect = document.getElementById('program');
    const showRequirementsBtn = document.getElementById('showRequirementsBtn');
    const requirementsDisplay = document.getElementById('requirementsDisplay');
    const requirementsContent = document.getElementById('requirementsContent');

    // Populate university dropdown with unique universities
    const universities = [...new Set(universityData.map(item => item.university))];
    universities.forEach(university => {
        const option = document.createElement('option');
        option.value = university;
        option.textContent = university;
        universitySelect.appendChild(option);
    });

    // Update program dropdown when university changes
    universitySelect.addEventListener('change', function() {
        // Clear existing program options
        programSelect.innerHTML = '<option value="">Select Program</option>';
        
        // Hide requirements display
        requirementsDisplay.style.display = 'none';
        
        const selectedUniversity = this.value;
        if (selectedUniversity) {
            // Filter programs for selected university
            const programs = universityData.filter(item => item.university === selectedUniversity);
            programs.forEach(item => {
                const option = document.createElement('option');
                option.value = item.program;
                option.textContent = item.program;
                programSelect.appendChild(option);
            });
        }
    });

    // Handle button click event
    showRequirementsBtn.addEventListener('click', function() {
        const selectedUniversity = universitySelect.value;
        const selectedProgram = programSelect.value;

        // Basic validation
        if (!selectedUniversity || !selectedProgram) {
            alert('Please select both University and Program');
            return;
        }

        // Find the matching data entry
        const selectedData = universityData.find(
            item => item.university === selectedUniversity && item.program === selectedProgram
        );

        if (selectedData) {
            // Display requirements
            const aLevel = selectedData.aLevel;
            requirementsContent.innerHTML = `
                <div class="requirement-item">
                    <strong>Minimum A-Level Subjects:</strong>
                    <p>${aLevel.minSubjects}</p>
                </div>
                <div class="requirement-item highlight">
                    <strong>Required Subjects:</strong>
                    <p>${aLevel.requiredSubjects}</p>
                </div>
                <div class="requirement-item highlight">
                    <strong>Grade Requirement:</strong>
                    <p>${aLevel.gradeRequirement}</p>
                </div>
                <div class="requirement-item">
                    <strong>O-Level Requirement:</strong>
                    <p>${aLevel.oLevelRequirement}</p>
                </div>
                <div class="requirement-item">
                    <strong>Test Requirement:</strong>
                    <p>${aLevel.testRequirement}</p>
                </div>
                <div class="requirement-item">
                    <strong>Additional Notes:</strong>
                    <p>${aLevel.additionalNotes}</p>
                </div>
            `;
            requirementsDisplay.style.display = 'block';
            
            // Scroll to requirements
            requirementsDisplay.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
            alert('Requirements not found for the selected combination');
        }
    });
});

