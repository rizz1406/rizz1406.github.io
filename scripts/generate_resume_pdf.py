from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "resume" / "rizwan-baig-resume.pdf"
BLUE = colors.HexColor("#2457E6")
INK = colors.HexColor("#172033")
MUTED = colors.HexColor("#43516A")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=20, leading=23, textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=MUTED, spaceAfter=7))
styles.add(ParagraphStyle(name="Section", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=INK, spaceBefore=8, spaceAfter=3))
styles.add(ParagraphStyle(name="Role", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=INK, spaceBefore=3))
styles.add(ParagraphStyle(name="Body", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11.5, textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle(name="ResumeBullet", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11.2, textColor=INK, leftIndent=10, firstLineIndent=-7, spaceAfter=1.5))

def p(text, style="Body"):
    return Paragraph(text, styles[style])

def section(title):
    return [Spacer(1, 3), p(title.upper(), "Section"), HRFlowable(width="100%", thickness=.45, color=colors.HexColor("#CBD5E1"), spaceAfter=3)]

story = [
    p("Rizwan Baig", "Name"),
    p("Data Analyst | Hyderabad, India", "Subtitle"),
    p("rizwanmirza95551@gmail.com &nbsp; | &nbsp; linkedin.com/in/rizwanbaig001 &nbsp; | &nbsp; github.com/rizz1406 &nbsp; | &nbsp; rizz1406.github.io", "Subtitle"),
]
story += section("Summary")
story += [p("Data Analyst with production experience building reliable data pipelines, reporting workflows, and analytics solutions for a major digital media client. Skilled in BigQuery, advanced SQL, GA4, Google Ad Manager, Looker Studio, Power BI, and Python automation.")]
story += section("Experience")
story += [
    p("Data Analyst, DataBeat <font color='#43516A'>| Jun 2025 - Present</font>", "Role"),
    p("Hyderabad | Client: TIME"),
    p("• Designed and delivered an automated Google Ad Manager inventory-forecasting pipeline, replacing manual reporting.", "ResumeBullet"),
    p("• Own dashboards, BigQuery datasets, and ETL pipelines from development and QA through deployment and monitoring.", "ResumeBullet"),
    p("• Build production SQL across Bronze/Silver/Gold layers and resolve reporting discrepancies across GA4, GAM, and BigQuery.", "ResumeBullet"),
    p("• Improve BigQuery cost and performance through partitioning, clustering, and CTE refactoring.", "ResumeBullet"),
    p("Data Researcher Intern, Collegedunia <font color='#43516A'>| Dec 2024 - 2025</font>", "Role"),
    p("Remote"),
    p("• Created structured LaTeX solution PDFs with AI-assisted tools for clear, accurate delivery.", "ResumeBullet"),
    p("• Researched and validated educational data to 95% accuracy while collaborating across research workflows.", "ResumeBullet"),
]
story += section("Skills")
story += [
    p("<b>Data Engineering:</b> ETL pipelines, data modelling, BigQuery datasets, Bronze/Silver/Gold architecture, partitioning, clustering, monitoring."),
    p("<b>Analytics Engineering:</b> Advanced SQL, window functions, CTEs, data reconciliation, data-quality checks, query optimisation."),
    p("<b>Digital Analytics & AdTech:</b> GA4, Google Ad Manager, Parse.ly, Marfeel, inventory forecasting."),
    p("<b>Business Intelligence:</b> Looker Studio, Power BI, Excel, Google Sheets, Python automation, API integration."),
]
story += section("Selected Projects")
story += [
    p("ResumeAI - Resume Tailor <font color='#43516A'>| Next.js, Claude AI</font>", "Role"),
    p("Tailors resumes to a job description and generates an ATS-focused PDF. Live: resume-tailor.vercel.app"),
    p("Pulse - Health Tracker <font color='#43516A'>| Web App</font>", "Role"),
    p("Private dashboard for logging and monitoring daily health metrics in one place. Live: pulse-v24w.onrender.com"),
]
story += section("Certifications")
story += [
    p("<b>Databricks Certified Data Engineer Associate</b> | Databricks"),
    p("<b>Drive Advertising Revenue with Google Ad Manager</b> | Google Skillshop | Completed July 2025"),
]
story += section("Education")
story += [
    p("<b>BTech, Computer Science & Design</b>, St. Martin's Engineering College, Hyderabad | 2021 - 2025 | CGPA: 7.0"),
    p("<b>Intermediate (MPC)</b>, Sri Chaitanya Junior College, Hyderabad | 2019 - 2021 | 94%"),
]

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=.58*inch, leftMargin=.58*inch, topMargin=.45*inch, bottomMargin=.42*inch, title="Rizwan Baig Resume", author="Rizwan Baig")
doc.build(story)
print(OUTPUT)
