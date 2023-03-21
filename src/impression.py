# from reportlab.pdfgen import canvas
# import win32print
# import win32api
# import os

# # Créez un PDF avec ReportLab
# filename = "example.pdf"
# document_title = "My Example PDF"
# c = canvas.Canvas(filename)
# c.drawString(100, 750, "Welcome to Reportlab!")
# c.save()

# # Imprimez le PDF avec win32print
# printer_name = win32print.GetDefaultPrinter()
# filepath = os.path.abspath(filename)
# win32api.ShellExecute(0, "print", filepath, '/d:"%s"' % printer_name, ".", 0)

# print("Document imprimé!")

# # Generateur de PDF 
# class GenerateurPdf():
#     def __init__(self,fichier,titre,data):
#         self.fichier = fichier
#         self.titre = titre
#         self.data = data
        
#     def generateur(self):
#         c = canvas.Canvas(self.fichier)
#         c.save()
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from  reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.pdfgen import canvas

# Données pour remplir le tableau
data = []
for i in range(10):
    data.append(['Ligne %s, Colonne 1' % i, 'Ligne %s, Colonne 2' % i, 'Ligne %s, Colonne 3' % i])
    print(data)

data1 = [["", "Date: 20/03/2023\nNom et Prénom:\nSignature:\n\n\n"]]
pdf = SimpleDocTemplate("exemple.pdf", pagesize=letter)

# Création du tableau avec les données
table = Table(data, colWidths=[60*mm, 60*mm, 60*mm])
table1 = Table(data1,colWidths=[90*mm,90*mm],spaceBefore=(15*mm),rowHeights=(50*mm))


# Configuration du style du tableau
style = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 14),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    
])
style1 = TableStyle([
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('VALIGN',(0,0),(-1,-1),'TOP')
    
])
# Appliquer le style au tableau
table.setStyle(style)
table1.setStyle(style1)

# En-tête
# h1 = PS(
#     name = 'Heading1',
#     fontSize = 14,
#     leading = 16)
# Titre = Paragraph('Titre Test',h1)
def header():
     c = canvas.Canvas()
     c.saveState()
     c.setFont('Helvetica-bold', 14)
     c.drawCentredString(letter[0]/2.0,letter[1]-15,'Titre Test')
     c.restoreState()
     

# Ajouter le tableau au document PDF
pdf.
pdf.multiBuild([table,table1])

