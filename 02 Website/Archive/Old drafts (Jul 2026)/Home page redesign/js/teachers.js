// Teacher Data
const teachers = [
    {
        id: 100,
        name: "Sir Salman Junaid",
        isCoFounder: true,
        subjects: ["Math", "Physics"],
        level: ["O-Level", "A-Level"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Learn A Level Math with Sir Salman Junaid, an NED University engineer and former Karachi Grammar School (KGS) faculty member who makes abstract concepts visual, exam techniques precise, and past paper patterns easier to master. He is also the Co-founder of SJ Academy, bringing 12+ years of teaching excellence to the platform.",
        image: "https://ui-avatars.com/api/?name=Salman+Junaid&background=FCE004&color=453516&size=400&bold=true",
        experience: "12+ Years",
        affiliations: ["SJ Academy (Co-founder)", "Ex-KGS Faculty", "NED University"],
        socials: {
            linkedin: "https://linkedin.com/#",
            twitter: "https://twitter.com/#",
            instagram: "https://instagram.com/#"
        }
    },
    {
        id: 1,
        name: "Sir Sunyyan Junaid",
        isCoFounder: false,
        subjects: ["Business"],
        level: ["A-Level"],
        category: ["business", "a-level"],
        bio: "Sunyyan Junaid is a passionate educator with over 8 years of experience in business, marketing, and leadership. He brings real-world insights into the classroom. His teaching approach focuses on simplifying complex concepts, developing critical thinking, and helping students apply business theory to real-life scenarios.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/07/296167730_10159330125240939_9121453372746153911_n-min.jpg",
        experience: "8+ Years",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#",
            twitter: "https://twitter.com/#",
            youtube: "https://youtube.com/#"
        }
    },
    {
        id: 2,
        name: "Sir Khawar Shuaib",
        subjects: ["Economics"],
        level: ["A-Level", "IB"],
        category: ["business", "a-level"],
        bio: "KHAWAR SHUAIB is an experienced economics educator and entrepreneur with a strong background in teaching A-Level and IB Economics. He started his teaching career in 2014 and has since worked with students across Pakistan, the UAE, and the UK. His approach combines conceptual clarity with practical application.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2026/06/Khawar-2.jpeg",
        experience: "Since 2014",
        affiliations: ["Pakistan", "UAE", "UK"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 4,
        name: "Sir Abdullah Zaman",
        subjects: ["Chemistry"],
        level: ["O-Level", "A-Level"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Sir Abdullah Zaman is a dedicated and accomplished Chemistry educator with over five years of professional teaching experience in O Level and A Level. His teaching philosophy emphasizes conceptual understanding, analytical thinking, and real-world application of chemical principles.",
        image: "https://ui-avatars.com/api/?name=Abdullah+Zaman&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "5+ Years",
        affiliations: ["Lions Schooling System", "Iqra University", "Progressive Public School", "SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#",
            twitter: "https://twitter.com/#"
        }
    },
    {
        id: 5,
        name: "Sir Umair",
        subjects: ["Biology"],
        level: ["O-Level", "A-Level", "IB"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Muhammad Umair is a dedicated teacher for Biology with extensive experience in teaching multiple curricula. He began teaching at Beaconhouse as an IB Biology teacher and has taught IB and Cambridge A levels for the past 8 years. He also designed the new federal Biology curriculum for inter and matric.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/11/Umair-Pic-1.jpg",
        experience: "8+ Years",
        affiliations: ["Beaconhouse", "SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 6,
        name: "Sir Riza Walji",
        subjects: ["Computer Science"],
        level: ["O-Level", "A-Level", "IGCSE"],
        category: ["sciences", "o-level", "a-level"],
        bio: "Mohammed Riza Walji is a seasoned Computer Science educator with over nine years of teaching experience. He has developed a strong reputation for his subject expertise and engaging teaching style with a commitment to academic excellence and student success.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/11/Sir-Riza.webp",
        experience: "9+ Years",
        affiliations: ["Jaffar Public School", "Beaconhouse", "Links School", "Bay View Academy"],
        socials: {
            linkedin: "https://linkedin.com/#",
            twitter: "https://twitter.com/#"
        }
    },
    {
        id: 7,
        name: "Sir Shaibaz Ali",
        subjects: ["Accounts"],
        level: ["O-Level", "A-Level"],
        category: ["business", "o-level", "a-level"],
        bio: "Shahbaz Ali (CAT - ACCA) is an expert Accounting teacher who has been teaching since 2011. He brings extensive experience from various prestigious schools, ensuring top-tier accounting education for his students.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/11/Accounts-sir-scaled.jpg",
        experience: "Since 2011",
        affiliations: ["BSS (PECHS)", "LGS (DHA Campus)", "The Froebel's School", "Karachi High School"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 8,
        name: "Miss Asmat Zafar",
        subjects: ["Urdu"],
        level: ["O-Level", "A-Level"],
        category: ["humanities", "o-level", "a-level"],
        bio: "Miss Asmat Zafar is an experienced O/A Level Urdu teacher. She has served as Head of Urdu Department at Education Bay and worked as a Senior Author with the University of Cambridge. She is known for her clear teaching style and strong command of Urdu literature.",
        image: "https://ui-avatars.com/api/?name=Asmat+Zafar&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "Experienced",
        affiliations: ["Education Bay", "University of Cambridge", "St. Michael’s Convent"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 9,
        name: "Sir Kashaan Ali",
        subjects: ["Islamiat", "Pak Studies"],
        level: ["O-Level", "IGCSE"],
        category: ["humanities", "o-level"],
        bio: "Kashan Ali is an enthusiastic individual who has taught generations through his teaching career of 22 years. He began his career in 2003 and is associated with prestigious institutes.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/07/Kashan-Ali.jpeg",
        experience: "22 Years",
        affiliations: ["Bahria Foundation", "The City School", "LINKS", "The Indus Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 10,
        name: "Sir Saifullah",
        subjects: ["Accounts"],
        level: ["O-Level", "A-Level"],
        category: ["business", "o-level", "a-level"],
        bio: "Saifullah is an experienced Accounting educator specializing in O Level and A Level Accounting. He is a CAIE-certified Accounting teacher whose teaching approach emphasizes conceptual clarity, real-world application, and exam-focused preparation.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2025/11/Accounts-sir-scaled.jpg",
        experience: "5+ Years",
        affiliations: ["The City School", "The Next School", "The Academy", "Falconhouse"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 11,
        name: "Sir Aaliyan",
        subjects: ["Business", "Economics"],
        level: ["O-Level"],
        category: ["business", "o-level"],
        bio: "Syed Alyan Ali is a spirited instructor having over 7 years of experience in coaching O and A Level students. His lectures instill problem-solving techniques that help students apply theoretical concepts to practical situations.",
        image: "https://www.sjacademy.pk/wp-content/uploads/2026/06/Alyaan.jpeg",
        experience: "7+ Years",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 12,
        name: "Miss Muzna Zaidi",
        subjects: ["Psychology"],
        level: ["A-Level"],
        category: ["humanities", "a-level"],
        bio: "Miss Muzna Zaidi is an enthusiastic and insightful A-Level Psychology educator who specializes in simplifying complex psychological concepts. With a strong command of the Cambridge Psychology syllabus, she focuses on building critical thinking and analytical writing skills.",
        image: "https://ui-avatars.com/api/?name=Muzna+Zaidi&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "Currently pursuing degree",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#",
            instagram: "https://instagram.com/#"
        }
    },
    {
        id: 13,
        name: "Miss Tayyaba Yaseen",
        subjects: ["Sociology", "English"],
        level: ["O-Level", "A-Level", "IGCSE"],
        category: ["humanities", "o-level", "a-level"],
        bio: "Tayyaba Yaseen is a passionate and student-focused teacher with over 3 years of teaching experience. With a background in psychology, she designs lessons that are engaging, practical, and easy to grasp, encouraging curiosity and critical thinking.",
        image: "https://ui-avatars.com/api/?name=Tayyaba+Yaseen&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "3+ Years",
        affiliations: ["SJ Academy"],
        socials: {
            linkedin: "https://linkedin.com/#"
        }
    },
    {
        id: 3,
        name: "Sir Basharat",
        subjects: ["Chemistry", "Physics"],
        level: ["O-Level"],
        category: ["sciences", "o-level"],
        bio: "Not Available detail. An experienced educator in Chemistry and Physics, dedicated to building strong foundational knowledge for O-Level students.",
        image: "https://ui-avatars.com/api/?name=Sir+Basharat&background=FAFAFA&color=453516&size=300&bold=true",
        experience: "Experienced",
        affiliations: ["SJ Academy"],
        socials: {}
    }
];

document.addEventListener('DOMContentLoaded', () => {
    // Custom Cursor Logic
    const customCursor = document.getElementById('customCursor');
    
    if (customCursor) {
        window.addEventListener('mousemove', (e) => {
            const posX = e.clientX;
            const posY = e.clientY;
            
            customCursor.style.left = `${posX}px`;
            customCursor.style.top = `${posY}px`;
        });
    }

    const grid = document.getElementById('teachersGrid');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const modalOverlay = document.getElementById('teacherModal');
    const modalContent = document.getElementById('modalContent');
    const closeModal = document.getElementById('closeModal');

    // Render Function
    function renderTeachers(filter = 'all') {
        grid.innerHTML = '';
        
        const filtered = teachers.filter(t => filter === 'all' || t.category.includes(filter));
        
        filtered.forEach((teacher, index) => {
            const delay = index * 0.1; // Cascade animation
            const allTags = [...teacher.subjects, ...teacher.level];
            
            // Add a special highlight class to tags if it's a cofounder card
            const tagClass = teacher.isCoFounder ? 'tag highlight-tag' : 'tag';
            const tagsHTML = allTags.map(tag => `<span class="${tagClass}">${tag}</span>`).join('');
            
            // Social icons generator
            let socialsHTML = '';
            if(teacher.socials) {
                if(teacher.socials.linkedin) socialsHTML += `<a href="${teacher.socials.linkedin}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a>`;
                if(teacher.socials.twitter) socialsHTML += `<a href="${teacher.socials.twitter}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-twitter"></i></a>`;
                if(teacher.socials.instagram) socialsHTML += `<a href="${teacher.socials.instagram}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-instagram"></i></a>`;
                if(teacher.socials.youtube) socialsHTML += `<a href="${teacher.socials.youtube}" class="social-icon hover-target" target="_blank"><i class="fa-brands fa-youtube"></i></a>`;
            }

            const card = document.createElement('div');
            card.className = `teacher-card reveal-up ${teacher.isCoFounder ? 'featured' : ''}`;
            card.style.animationDelay = `${delay}s`;
            
            card.innerHTML = `
                <div class="card-top">
                    <div class="teacher-img-wrap">
                        <img src="${teacher.image}" alt="${teacher.name}" class="teacher-img">
                    </div>
                    <div class="card-header-info">
                        <h3 class="teacher-name">${teacher.name}</h3>
                        <div class="teacher-tags">
                            ${teacher.isCoFounder ? `<span class="tag highlight-tag" style="background:var(--orange);color:#fff;border:none;">Co-founder</span>` : ''}
                            ${tagsHTML}
                        </div>
                    </div>
                </div>
                <p class="teacher-bio-snippet">${teacher.bio}</p>
                <div class="card-footer">
                    <div class="social-links">
                        ${socialsHTML}
                    </div>
                    <button class="read-more-btn hover-target" data-id="${teacher.id}">
                        Full Profile
                    </button>
                </div>
            `;
            
            grid.appendChild(card);
        });

        // Add event listeners to new buttons
        document.querySelectorAll('.read-more-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = parseInt(e.currentTarget.getAttribute('data-id'));
                openModal(id);
            });
        });
    }

    // Modal Functionality
    function openModal(id) {
        const teacher = teachers.find(t => t.id === id);
        if (!teacher) return;
        
        const allTags = [...teacher.subjects, ...teacher.level];
        const tagsHTML = allTags.map(tag => `<span class="tag" style="background:#eee;border-color:#ccc;">${tag}</span>`).join('');
        
        let socialsHTML = '';
        if(teacher.socials) {
            if(teacher.socials.linkedin) socialsHTML += `<a href="${teacher.socials.linkedin}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-linkedin"></i> LinkedIn</a>`;
            if(teacher.socials.twitter) socialsHTML += `<a href="${teacher.socials.twitter}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-twitter"></i> Twitter</a>`;
            if(teacher.socials.instagram) socialsHTML += `<a href="${teacher.socials.instagram}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-instagram"></i> Instagram</a>`;
            if(teacher.socials.youtube) socialsHTML += `<a href="${teacher.socials.youtube}" class="modal-social-btn hover-target" target="_blank"><i class="fa-brands fa-youtube"></i> YouTube</a>`;
        }
        
        modalContent.innerHTML = `
            <div class="modal-header">
                <img src="${teacher.image}" alt="${teacher.name}" class="modal-img">
                <div class="modal-header-info">
                    <h2>${teacher.name}</h2>
                    <div class="teacher-tags" style="margin-bottom: 10px;">
                        ${teacher.isCoFounder ? `<span class="tag highlight-tag" style="background:var(--orange);color:#fff;border:none;">Co-founder</span>` : ''}
                        ${tagsHTML}
                    </div>
                    <div class="modal-socials">
                        ${socialsHTML}
                    </div>
                </div>
            </div>
            <div class="modal-bio">${teacher.bio}</div>
            
            <table class="kv-table">
                <tr class="kv-row">
                    <td class="kv-label">EXPERIENCE</td>
                    <td class="kv-value">${teacher.experience}</td>
                </tr>
                <tr class="kv-row">
                    <td class="kv-label">SUBJECTS</td>
                    <td class="kv-value">${teacher.subjects.join(', ')}</td>
                </tr>
                <tr class="kv-row">
                    <td class="kv-label">LEVELS</td>
                    <td class="kv-value">${teacher.level.join(', ')}</td>
                </tr>
                <tr class="kv-row">
                    <td class="kv-label">AFFILIATIONS</td>
                    <td class="kv-value">${teacher.affiliations.join(', ')}</td>
                </tr>
            </table>
        `;
        
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }

    function close() {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    closeModal.addEventListener('click', close);
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) close();
    });
    
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
            close();
        }
    });

    // Filtering Functionality
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterBtns.forEach(b => b.classList.remove('active'));
            e.currentTarget.classList.add('active');
            const filter = e.currentTarget.getAttribute('data-filter');
            renderTeachers(filter);
        });
    });

    // Initial Render
    renderTeachers();
});
