from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import datetime

# Create PDF
pdf_path = r'c:\עמרי\Shmags 2\projects\university\notes\AI_Assistance_Disclosure.pdf'
doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                       rightMargin=0.75*inch, leftMargin=0.75*inch,
                       topMargin=0.75*inch, bottomMargin=0.75*inch)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#1f7a8f'),
    spaceAfter=0.3*inch,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#1f7a8f'),
    spaceAfter=0.15*inch,
    spaceBefore=0.2*inch,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=11,
    alignment=TA_JUSTIFY,
    spaceAfter=0.12*inch,
    leading=16
)

# Title
elements.append(Paragraph('AI Assistance Disclosure', title_style))
elements.append(Paragraph('HW #2: Functional Unit and System Boundary', styles['Heading3']))
elements.append(Spacer(1, 0.2*inch))

# Assignment overview
elements.append(Paragraph('<b>Assignment Overview</b>', heading_style))
elements.append(Paragraph(
    'This assignment required analysis of Life Cycle Assessment (LCA) methodology, with focus on defining functional units and system boundaries for milk production (dairy vs. soy milk). The work included: defining core LCA concepts, analyzing six lifecycle stages, comparing environmental impacts between product systems, and creating a system boundary diagram.',
    body_style
))

# How AI assisted
elements.append(Paragraph('<b>How AI (Claude Code) Assisted</b>', heading_style))
elements.append(Paragraph(
    '<b>1. Research and Academic Sourcing</b><br/>I conducted academic research to locate peer-reviewed LCA studies on dairy and soy milk production. I identified four primary sources (Poore & Nemecek 2018, Cao et al. 2009, Geburt et al. 2022, González-García et al. 2025) and verified that data in the assignment aligned with published research. This included correcting initial water usage estimates from approximate figures to precise peer-reviewed data (628 liters for dairy milk, 27-28 liters for soy milk).',
    body_style
))

elements.append(Paragraph(
    '<b>2. Brainstorming and Structuring</b><br/>I helped brainstorm the organization of six lifecycle stages, refine how each stage was described, and structure the comparison between dairy and soy milk systems. This included suggesting how to present processing details, environmental hotspots, and boundary justifications in a clear, logical flow.',
    body_style
))

elements.append(Paragraph(
    '<b>3. Phrasing and Academic Writing</b><br/>I provided feedback on phrasing technical concepts in clear, precise language appropriate for academic submission. This included refining definitions, ensuring consistency in terminology, and improving clarity of complex LCA concepts.',
    body_style
))

elements.append(Paragraph(
    '<b>4. Citation and Reference Management</b><br/>I formatted all academic citations in APA style, created a complete reference list, and integrated in-text citations throughout the assignment to support claims with peer-reviewed evidence.',
    body_style
))

# System boundary diagram
elements.append(Paragraph('<b>System Boundary Diagram</b>', heading_style))
elements.append(Paragraph(
    'The system boundary diagram included in the assignment was created using Python visualization based on a conceptual drawing you provided. I translated your diagram sketch into a professional, publication-quality graphic showing the six lifecycle stages, system boundary, energy inputs, and key inputs/outputs. The structure and layout were based on your original sketch; I handled the technical implementation and visual refinement.',
    body_style
))

# What was not AI-generated
elements.append(Paragraph('<b>What Was Not AI-Generated</b>', heading_style))
elements.append(Paragraph(
    '• Core analytical work and thinking about the assignment<br/>• Original functional unit definition<br/>• System boundary decisions and justifications<br/>• Technical details about milk production processes<br/>• All written content beyond structural and stylistic guidance<br/>• The conceptual approach and framework for analysis',
    body_style
))

# Summary
elements.append(Paragraph('<b>Summary</b>', heading_style))
elements.append(Paragraph(
    'This assignment represents your understanding of LCA methodology. AI assistance focused on academic rigor (sourcing and citation), clarity of expression, and visual presentation. The core analysis, decision-making, and content are your own work.',
    body_style
))

# Metadata
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(
    f'<i>Disclosure prepared: {datetime.now().strftime("%B %d, %Y")}</i>',
    styles['Normal']
))

# Build PDF
doc.build(elements)
print(f"PDF created: {pdf_path}")
