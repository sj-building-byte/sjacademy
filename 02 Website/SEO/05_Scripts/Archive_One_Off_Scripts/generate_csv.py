import csv
import os

os.makedirs("Scholarship_Data", exist_ok=True)

files = {
    "Karachi.csv": [
        ["City","College","Tier","Min_A_Stars","Min_Total_As","Min_Points","Student_Type","Model","Conditions"],
        ["Karachi","Alpha College","100% Waiver",7,9,0,"Any","Quantitative","Rs. 4000 monthly admin fee applies."],
        ["Karachi","The Lyceum","Need-Based Aid",0,0,0,"Any","Holistic","Apply for aid only after securing academic admission. Must maintain academic standing."],
        ["Karachi","Cedar College","Merit Waiver",0,0,0,"Any","Holistic","Holistic evaluation on final grades. Offers must be unconditional to switch subjects."],
        ["Karachi","Nixor College","Holistic Waiver",0,0,0,"Any","Holistic","Grades are just a baseline. Heavy weight placed on essays and interviews assessing leadership."],
        ["Karachi","Karachi Grammar School (KGS)","Need-Based Aid",0,0,0,"Any","Holistic","Highly selective on pure academic merit. Offers robust need-based financial aid rather than grade matrices."],
        ["Karachi","Foundation Public School (FPS)","100% Waiver",0,4,0,"Any","Quantitative","Interview required to evaluate alignment with core values."],
        ["Karachi","Foundation Public School (FPS)","75% Waiver",0,3,0,"Any","Quantitative","Interview required to evaluate alignment with core values."],
        ["Karachi","Foundation Public School (FPS)","50% Waiver",0,2,0,"Any","Quantitative","Interview required to evaluate alignment with core values."],
        ["Karachi","Whales College","10% to 100% Waiver",0,4,0,"Any","Quantitative","Minimum 4 As required to qualify; percentage scales with higher grades."],
        ["Karachi","Sceptre College","Merit Waiver",0,0,0,"Any","Quantitative","Strict retention: 85% attendance min C grade internally and strict rule compliance."],
        ["Karachi","Highbrow College","Holistic Waiver",0,0,0,"Any","Holistic","Blends academic baseline with strong emphasis on extracurricular engagement."],
        ["Karachi","Beaconhouse College Programme (BCP)","Merit Waiver",0,0,0,"Any","Quantitative","Awards scale directly with final CAIE O Level results and interview performance."]
    ],
    "Lahore.csv": [
        ["City","College","Tier","Min_A_Stars","Min_Total_As","Min_Points","Student_Type","Model","Conditions"],
        ["Lahore","SICAS","100% Waiver",0,0,40,"Any","Quantitative","Requires 40+ points (A*=10 A=5). Maintain 3.67 GPA in A-Levels; drops below 3.00 revoke scholarship."],
        ["Lahore","SICAS","75% Waiver",0,0,35,"Any","Quantitative","Requires 35 points (A*=10 A=5). Maintain high GPA."],
        ["Lahore","SICAS","50% Waiver",0,0,30,"Any","Quantitative","Requires 30 points (A*=10 A=5). Maintain high GPA."],
        ["Lahore","SICAS","30% Waiver",0,0,25,"Any","Quantitative","Requires 25 points (A*=10 A=5). Maintain high GPA."],
        ["Lahore","LACAS","100% Waiver (Internal)",0,6,0,"Internal","Quantitative","For existing LACAS students only."],
        ["Lahore","LACAS","100% Waiver (External)",0,7,0,"External","Quantitative","For external applicants."],
        ["Lahore","LACAS","75% Waiver (Internal)",0,5,0,"Internal","Quantitative","For existing LACAS students only."],
        ["Lahore","LACAS","75% Waiver (External)",0,6,0,"External","Quantitative","For external applicants."],
        ["Lahore","LACAS","50% Waiver (Internal)",0,4,0,"Internal","Quantitative","For existing LACAS students only."],
        ["Lahore","LACAS","50% Waiver (External)",0,5,0,"External","Quantitative","For external applicants."],
        ["Lahore","LACAS","25% Waiver (Internal)",0,3,0,"Internal","Quantitative","For existing LACAS students only."],
        ["Lahore","LACAS","25% Waiver (External)",0,4,0,"External","Quantitative","For external applicants."],
        ["Lahore","LGS Johar Town (JT) Boys","Merit Waiver",0,0,0,"Any","Quantitative","Requires baseline of 8 O Level subjects. Must maintain straight As in A-Levels."],
        ["Lahore","Learning Alliance","100% Tuition & Charges",0,10,0,"Any","Quantitative","10+ As required. Must maintain good attendance discipline and internal AS grades."],
        ["Lahore","Learning Alliance","100% Tuition Waiver",0,8,0,"Any","Quantitative","8 to 9 As. Lab charges may still apply."],
        ["Lahore","Learning Alliance","75% Tuition Waiver",0,7,0,"Any","Quantitative","Lab charges may still apply."],
        ["Lahore","Learning Alliance","50% Tuition Waiver",0,6,0,"Any","Quantitative","Lab charges may still apply."],
        ["Lahore","Learning Alliance","25% Tuition Waiver",0,5,0,"Any","Quantitative","Lab charges may still apply."],
        ["Lahore","LGS Defence","Holistic / Need",0,0,0,"Any","Holistic","Flexible blend of academic merit special talent and need-based financial aid."],
        ["Lahore","Roots International","100% Waiver",0,8,0,"Any","Quantitative","Requires 8 A*/As. Scales down incrementally for fewer As."],
        ["Lahore","Roots International","75% Waiver",0,7,0,"Any","Quantitative","Requires 7 A*/As."],
        ["Lahore","Beaconhouse College Programme (BCP)","Merit Waiver",0,0,0,"Any","Quantitative","Awards scale directly with final CAIE O Level results."],
        ["Lahore","Aitchison College","Need-Based Aid",0,0,0,"Any","Holistic","Highly competitive academic baseline; extensive need-based financial aid."],
        ["Lahore","The City School (Ravi)","Merit Waiver",0,0,0,"Any","Quantitative","Scales directly with the number of As secured in CAIE."],
        ["Lahore","Bloomfield Hall","Merit / Need",0,0,0,"Any","Holistic","Combines merit for top achievers with need-based provisions."]
    ],
    "Islamabad_Rawalpindi.csv": [
        ["City","College","Tier","Min_A_Stars","Min_Total_As","Min_Points","Student_Type","Model","Conditions"],
        ["Islamabad/Rawalpindi","Roots Ivy International","100% Waiver",0,0,0,"Any","Quantitative","Requires straight A*/A. Mandatory entry test/interview required. Scales down incrementally."],
        ["Islamabad/Rawalpindi","Roots Millennium","Merit Waiver",0,0,0,"Any","Quantitative","Strictly merit-based. Local board students must secure 70%+ just for admission eligibility."],
        ["Islamabad/Rawalpindi","Froebel's International","Merit / Talent",0,0,0,"Any","Holistic","Offers academic merit and unique talent-based scholarships (sports arts public speaking)."],
        ["Islamabad/Rawalpindi","Headstart School","Holistic Waiver",0,0,0,"Any","Holistic","Admissions rely on a 30-min test (English Math Urdu) and a 15-min interview evaluating critical thinking."],
        ["Islamabad/Rawalpindi","Super Nova School","Merit Waiver",0,0,0,"Any","Quantitative","Tied to O Level achievements but all applicants must clear a mandatory entry test and interview."],
        ["Islamabad/Rawalpindi","Westminster International","Merit Waiver",0,0,0,"Any","Quantitative","Awarded to top-performing students based on O Level grades."],
        ["Islamabad/Rawalpindi","Beaconhouse College Programme (BMI)","Merit Waiver",0,0,0,"Any","Quantitative","Awards scale directly with final CAIE O Level results."],
        ["Islamabad/Rawalpindi","The City School (Capital)","Merit Waiver",0,0,0,"Any","Quantitative","Straightforward matrix granting tuition waivers based on A*s and As."],
        ["Islamabad/Rawalpindi","LGS Islamabad","Holistic / Need",0,0,0,"Any","Holistic","Assesses students via a mix of O Level performance metrics and financial need evaluations."],
        ["Islamabad/Rawalpindi","Schola Nova","Holistic Waiver",0,0,0,"Any","Holistic","Focuses on holistic candidate evaluations supplementing academics with interviews."]
    ],
    "Other_Cities.csv": [
        ["City","College","Tier","Min_A_Stars","Min_Total_As","Min_Points","Student_Type","Model","Conditions"],
        ["Faisalabad","TUF / Collegiate Programmes","Merit Waiver",0,0,0,"Any","Quantitative","Board Position Holders secure 100% waivers; 90%+ receive proportional discounts."],
        ["Faisalabad","Beaconhouse College Programme (BCP)","Merit Waiver",0,0,0,"Any","Quantitative","Awards scale directly with final CAIE O Level results."],
        ["Faisalabad","LGS Faisalabad","Merit Waiver",0,0,0,"Any","Quantitative","Evaluates A-Level intake based on previous board/CAIE results for waivers."],
        ["Multan","Beaconhouse College Programme (BCP)","Merit Waiver",0,0,0,"Any","Quantitative","Standard BCP merit matrix applies."],
        ["Multan","LGS Multan","Merit / Need",0,0,0,"Any","Holistic","Awards based on O Level academic merit with need-based flexibility."],
        ["Multan","Bloomfield Hall","Merit Waiver",0,0,0,"Any","Quantitative","Grants merit scholarships specifically targeting top-tier CAIE O Level achievers."],
        ["Peshawar","Beaconhouse College Programme (BCP)","Merit Waiver",0,0,0,"Any","Quantitative","Adheres to central BCP policy of rewarding A* and A grades."],
        ["Peshawar","The City School Peshawar","Merit Waiver",0,0,0,"Any","Quantitative","Follows corporate City School matrix ensuring top performers receive percentage-based waivers."],
        ["Peshawar","LGS Peshawar","Merit Waiver",0,0,0,"Any","Quantitative","Evaluates O Level results to award scaling merit-based financial incentives."]
    ]
}

for filename, rows in files.items():
    filepath = os.path.join("Scholarship_Data", filename)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Created {filepath}")
