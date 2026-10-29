from pathlib import Path
import re, html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT

root=Path(__file__).parent
out=root/'output/pdf/SJ_Academy_SEO_Director_Report.pdf'
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyAudit',fontName='Helvetica',fontSize=9.4,leading=12.8,spaceAfter=7,textColor=colors.HexColor('#292929')))
styles.add(ParagraphStyle(name='CellAudit',parent=styles['BodyAudit'],fontSize=8.1,leading=10.7,spaceAfter=0))
styles.add(ParagraphStyle(name='TitleAudit',fontName='Helvetica-Bold',fontSize=23,leading=27,spaceAfter=16,textColor=colors.HexColor('#453516')))
styles.add(ParagraphStyle(name='HeadingAudit',fontName='Helvetica-Bold',fontSize=15,leading=19,spaceBefore=6,spaceAfter=12,textColor=colors.HexColor('#453516'),keepWithNext=True))
def fmt(s):
    s=html.escape(s).replace('’',"'").replace('“','&quot;').replace('”','&quot;').replace('–','-').replace('≥','&gt;=').replace('≤','&lt;=')
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<link href="\2" color="#9A4200"><u>\1</u></link>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'<font name="Helvetica">\1</font>',s)
    return s
def para(s,style='BodyAudit'): return Paragraph(fmt(s),styles[style])
story=[]
lines=(root/'SJ_Academy_SEO_Director_Report.md').read_text().splitlines()
i=0
while i<len(lines):
    line=lines[i].strip()
    if not line: i+=1;continue
    if line=='---PAGE---': story.append(PageBreak());i+=1;continue
    if line.startswith('# '): story.append(para(line[2:],'TitleAudit'));i+=1;continue
    if line.startswith('## '): story.append(para(line[3:],'HeadingAudit'));i+=1;continue
    if line.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.match(r'^:?-+:?$',c) for c in cells): rows.append([para(c,'CellAudit') for c in cells])
            i+=1
        n=len(rows[0]); widths={2:[150,361],3:[180,105,226],4:[95,110,110,196]}.get(n,[511/n]*n)
        if n==3 and any(x in rows[0][1].text.lower() for x in ['clicks','sessions']): widths=[295,108,108]
        t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#FCE004')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#453516')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F7F5EF')])]))
        story.extend([t,Spacer(1,9)]);continue
    if line.startswith('- '): story.append(para('• '+line[2:]));i+=1;continue
    block=[line];i+=1
    while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','---PAGE---','- ')):
        block.append(lines[i].strip());i+=1
    story.append(para(' '.join(block)))
def page(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#FCE004'));canvas.setLineWidth(3);canvas.line(42,812,553,812)
    canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#746D5F'))
    canvas.drawString(42,25,'SJ ACADEMY  |  SEO & AI SEARCH AUDIT  |  10 SEPTEMBER 2026')
    canvas.drawRightString(553,25,str(doc.page))
doc=SimpleDocTemplate(str(out),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=43,bottomMargin=43,title='SJ Academy SEO and AI Search Audit',author='SJ Academy Research')
doc.build(story,onFirstPage=page,onLaterPages=page)
print(out)
