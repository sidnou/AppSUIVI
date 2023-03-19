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
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Données pour remplir le tableau
data = []
for i in range(10):
    data.append(['Ligne %s, Colonne 1' % i, 'Ligne %s, Colonne 2' % i, 'Ligne %s, Colonne 3' % i])
    print(data)
# Création du document PDF
pdf = SimpleDocTemplate("exemple.pdf", pagesize=letter)

# Création du tableau avec les données
table = Table(data, colWidths=[60*mm, 60*mm, 60*mm])

# Configuration du style du tableau
style = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 14),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
    ('GRID',(0,0),(-1,-1),1,colors.black)
])

# Appliquer le style au tableau
table.setStyle(style)

# Ajouter le tableau au document PDF
pdf.multiBuild([table])
