from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from datetime import date

AUJOURD_HUI = date.today().strftime("%d/%m/%Y")
ENTETE_PAGE = "RECUPERATION PAR CHRONOPOST"


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

        self.nom_fichier = nom_fichier
        self.titre = titre

        self.pdf = SimpleDocTemplate(self.nom_fichier, pagesize=letter)

        # Tableau des Numéros de suivis
        self.table = Table(self.data, colWidths=[53 * mm, 53 * mm, 53 * mm])  # dimension des cellule du tableau
        self.style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        self.table.setStyle(self.style)
        # Tableau signature et non prénom
        self.table1 = Table(self.data1, colWidths=[80 * mm, 80 * mm], spaceBefore=(10 * mm), rowHeights=(50 * mm))
        self.style1 = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                                  ('FONTSIZE', (0, 0), (-1, 0), 15)])
        self.table1.setStyle(self.style1)

        # En-tëte

        # création du style pour l'en-tête
        self.styles = getSampleStyleSheet()
        self.styleN = self.styles["Normal"]
        self.styleH = self.styles["Heading1"]
        self.styleH.alignment = 1

        # création de l'en-tête
        self.header = Paragraph(ENTETE_PAGE, self.styleH)
        self.header_table = Table([[self.header]])
        self.header_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
        ]))

    # Création du fichier PDF
    def generateur_pdf(self):
        try:
            self.pdf.build([self.header_table, self.table, self.table1])
        except PermissionError:
            print("Fichier déjà ouvert")

        # self.pdf.multiBuild([self.table2, self.table, self.table1])


if __name__ == '__main__':
    data = [
        ['Numéro de Suivi Chronopost', 'Numéro de Suivi Chronopost', 'Numéro de Suivi Chronopost']
    ]
    data.extend([f'Test {n}', f'Test {20+n}', f'test {40+n}'] for n in range(20))
    testPdf = GenPdf(data, "test-exemple-pdf.pdf", "test", '15')
    testPdf.generateur_pdf()
