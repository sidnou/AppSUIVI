from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Classe Création d'un fichier PDF


class GenPdf():

    def __init__(self, data: set, nom_fichier: str, titre):
        # for i in range(40):
        #     self.data.append(i)
        self.data = data
        print(data)
        self.nom_fichier = nom_fichier
        self.titre = titre
        self.table = Table(self.data, colWidths=[60*mm, 60*mm, 60*mm])
        self.style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        self.table.setStyle(self.style)
    # Création du fichier PDF

    def generateur_pdf(self):
        self.pdf = SimpleDocTemplate(self.nom_fichier, pagesize=letter)
        self.pdf.multiBuild([self.table])


if __name__ =='__main__':
    data = [
        ['test','test1','test2'],
        ['dede','dede1','dede2']
            ]
    testPdf = GenPdf(data,"test-exemple-pdf.pdf","test")
    testPdf.generateur_pdf()
      