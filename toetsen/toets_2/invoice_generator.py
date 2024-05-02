from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
import json
import os

# Functie om factuur te maken
def create_invoice(json_file_path, output_folder):
    # Open het JSON-bestand en laad de gegevens
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Toegang tot de informatie in de dictionary
    ordernummer = data['order']['ordernummer']
    orderdatum = data['order']['orderdatum']
    betaaltermijn = data['order']['betaaltermijn']

    klant_naam = data['order']['klant']['naam']
    klant_adres = data['order']['klant']['adres']
    klant_postcode = data['order']['klant']['postcode']
    klant_stad = data['order']['klant']['stad']
    klant_kvk_nummer = data['order']['klant']['KVK-nummer']

    producten = data['order']['producten']
    for product in producten:
        productnaam = product['productnaam']
        aantal = product['aantal']
        prijs_per_stuk_excl_btw = product['prijs_per_stuk_excl_btw']
        btw_percentage = product['btw_percentage']

        factuur_bedrag = prijs_per_stuk_excl_btw * aantal
        btw_bedrag = factuur_bedrag * btw_percentage / 100
        totaal_factuur_bedrag = factuur_bedrag + btw_bedrag

        # Maak PDF-factuur
        file_name = os.path.splitext(os.path.basename(json_file_path))[0] + ".pdf"
        file_path = os.path.join(output_folder, file_name)

        c = canvas.Canvas(file_path, pagesize=A4)

        # Voeg afbeelding toe
        c.drawImage(image_path, 75, 730, width=150, height=50)

        # Voeg bedrijfsinformatie toe
        c.setFont("Helvetica-Bold", 10)
        c.drawString(450, 700, 'Kioprex')
        c.drawString(450, 690, 'Heul 10')
        c.drawString(450, 680, 'Giessenburg 3381 DC')
        c.drawString(450, 670, 'KvK:12345678')
        c.drawString(450, 660, 'NL001234567B01')

        # Voeg klantinformatie toe
        c.setFont("Helvetica", 10)
        c.drawString(75, 660, klant_naam)
        c.drawString(75, 650, klant_adres)
        c.drawString(75, 640, klant_postcode)
        c.drawString(75, 630, klant_stad)

        # Voeg betalingsinformatie toe
        c.drawString(75, 500, f"Gelief binnen {betaaltermijn} uitbetalen op NL00ABCB123456789")

        # Voeg factuurtitel toe
        c.setFont("Helvetica", 20)
        c.drawString(75, 530, "Factuur")

        # Voeg factuurgegevens toe in tabellen
        data1 = [['Factuurnummer', 'Factuurdatum', 'Vervaldatum', 'KvKnummer'],
                 [ordernummer, orderdatum, betaaltermijn, klant_kvk_nummer]]

        data2 = [['Aantal', 'Omschrijving', '', 'Prijs', 'Bedrag', 'Btw'],
                 [aantal, productnaam, '', prijs_per_stuk_excl_btw, f'{round(prijs_per_stuk_excl_btw * aantal, 2)}',
                  f'{btw_percentage}%']]

        data3 = [['Totaal exclusief Btw', '', '', '', f'{""}', ''],
                 ['Btw(%)', '', '', '', f'{round(btw_bedrag, 2)}', ''],
                 ['Totaal inclusief', '', '', '', f'{round(totaal_factuur_bedrag, 2)}', '']]

        custom_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # Gebruik een vet lettertype
            ('FONTSIZE', (0, 0), (-1, -1), 8),  # Kleinere lettergrootte
            ('LINEABOVE', (0, 1), (-1, 1), 1, (0, 0, 0)),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Verticaal centreren
        ])

        table1 = Table(data1, colWidths=[100, 100, 100, 100])
        table1.setStyle(custom_style)
        page_width, page_height = A4
        table1.wrap(page_width, page_height)
        table_height1 = table1._height
        y_position1 = page_height - 350 - table_height1
        table1.drawOn(c, 75, y_position1)

        table2 = Table(data2, colWidths=[50, 150, 50, 50, 50, 50])
        table2.setStyle(custom_style)
        table2.wrap(page_width, page_height)
        table_height2 = table2._height
        y_position2 = y_position1 - 20 - table_height2
        table2.drawOn(c, 75, y_position2)

        table3 = Table(data3)
        table3.setStyle(custom_style)
        table3.wrap(page_width, page_height)
        table_height3 = table3._height
        y_position3 = y_position2 - 20 - table_height3
        table3.drawOn(c, 75, y_position3)

        c.save()

# Map waarin je JSON-bestanden zich bevinden
input_folder = "/Users/y.alkurdi/Documents/GitHub/toetsen/toets_2/test_set_softwareleverancier"
# Map waarin je de nieuwe PDF-bestanden wilt opslaan
output_folder = "/Users/y.alkurdi/Documents/GitHub/toetsen/toets_2/nieuw_pdf"
# Afbeeldingspad
image_path = '/Users/y.alkurdi/Desktop/Work_Stof/logo.png'

for filename in os.listdir(input_folder):
    # Controleer of het bestand eindigt op .json
    if filename.endswith(".json"):
        # Volledig pad naar het JSON-bestand
        json_file_path = os.path.join(input_folder, filename)
        # Maak de factuur voor dit JSON-bestand
        create_invoice(json_file_path, output_folder)
