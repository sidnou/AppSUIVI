from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from datetime import date
from reportlab.pdfgen import canvas

AUJOURD_HUI = date.today().strftime("%d/%m/%Y")


# Classe Création d'un fichier PDF
class GenPdf:

    def __init__(self, data: set, nom_fichier: str, titre, nc):
        # Nombre de Numéro suivi
        self.nombreNumeroSuivi = nc
        # Données 
        self.data = data
        self.data1 = [[f"Nombre de Colis: {nc}",
                       f"Date: {AUJOURD_HUI}\nNom et Prénom:\nSignature:\n\n\n"
                       ]]
        self.data2 = [['RECEPTION DES COLIS PAR CHRONOPOST ']]
        self.nom_fichier = nom_fichier
        self.titre = titre
        # Tableau des Numéros de suivis 
        self.table = Table(self.data, colWidths=[80 * mm, 80 * mm])  # dimension des cellule du tableau
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
        # Tableau signature et non prénom
        self.table1 = Table(self.data1, colWidths=[80 * mm, 80 * mm], spaceBefore=(15 * mm), rowHeights=(50 * mm))
        self.style1 = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                  ('FONTSIZE', (0, 0), (-1, 0), 12)])
        self.table1.setStyle(self.style1)

        # self.table2 = Table(self.data2, colWidths=[80 * mm, 80 * mm], rowHeights=(25 * mm))
        # self.style2 = TableStyle([('ALIGN', (0,0 ), (0, 0), 'CENTER'),
        #                           ('FONTSIZE', (0, 0), (0, 0), 20)])
        # self.table2.setStyle(self.style2)

        # # création du style pour l'en-tête
        # styles = getSampleStyleSheet()
        # styleN = styles["Normal"]
        # styleH = styles["Heading1"]
        # styleH.alignment = 1
        #
        # # création de l'en-tête
        # header = Paragraph("Titre de l'en-tête", styleH)
        # header_table = Table([[header]])
        # header_table.setStyle(TableStyle([
        #     ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),
        #     ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        #     ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        #     ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        #     ("FONTSIZE", (0, 0), (-1, -1), 14),
        #     ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
        # ]))

    # En-tëte
    def header(self):
        c = canvas.Canvas(self.nom_fichier)
        c.saveState()
        c.setFont('Courier-Bold', 14)
        c.drawCentredString(letter[0] / 2.0, letter[1] - 15, self.titre)
        c.restoreState()

    # Création du fichier PDF
    def generateur_pdf(self):
        self.pdf = SimpleDocTemplate(self.nom_fichier, pagesize=letter)
        self.pdf.build([self.table2, self.table, self.table1])
        # self.pdf.multiBuild([self.table2, self.table, self.table1])


if __name__ == '__main__':
    data = [
        ['Numéro de Suivi Chronopost', 'Numéro de Suivi Chronopost'],
        ['Test 1', 'Test2']
    ]
    testPdf = GenPdf(data, "test-exemple-pdf.pdf", "test", '15')
    testPdf.generateur_pdf()
