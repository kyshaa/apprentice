from fpdf import FPDF

# create FPDF object
# Layout ('P','L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()
pdf.image('ai.png', x = 11, y = 9, w = 40, h = 0, type = '', link = '')
# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('times', 'B', 25)

# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)
pdf.cell(45)
pdf.cell(150, 10, 'Alkisah Binti Mubin', ln=True, align='C')
pdf.cell(45)
pdf.set_font('times', '', 12)
pdf.cell(150, 10, 'Email : kishamubin17@gmail.com     Contact : +60 11-223 4456', ln=True, align='C')
pdf.ln(5)
pdf.line(x1 = 10, y1 = 35, x2 = 205, y2 = 35)



# company address
# new line
pdf.set_font('times', 'B', 12)
pdf.ln(17)
pdf.cell(80, 5, 'PERANTIS ISKANDAR', ln=True)
pdf.set_font('times', '', 12)
pdf.cell(80, 5, 'Educity Iskandar', ln=True)
pdf.cell(80, 5, '79100 Nusajaya', ln=True)
pdf.cell(160, 5, 'Johor.')
pdf.cell(1, 5, '15th October 2021.', ln=True)

# to whom it may concern
pdf.ln(20)
pdf.set_font('times', '', 12)
pdf.cell(80, 5, 'Good Day !', ln=True)

pdf.ln(10)
pdf.cell(65, 5, 'I am writing to express my interest in ')
pdf.set_font('times', 'B', 12)
pdf.cell(31, 5, 'AI programmer')
pdf.set_font('times', '', 12)
pdf.cell(1, 5, 'position at Educity Iskandar. I have been passionate in ', ln=True)
pdf.cell(80, 5, 'this field since I have accomplished my final year project with a greatest motivation during the bachelor study at ', ln=True)
pdf.cell(80, 5, 'Universiti Teknologi Malaysia. I believe that Educity Iskandar will not only be the best home for me to utilize my ', ln=True)
pdf.cell(80, 5, 'expertise but also will give me a wing to expand the skills and knowledge in AI.', ln=True)

pdf.ln(7)
pdf.cell(1, 5, 'I look forward to hearing from you. I can be reached through the email and contact number stated above. ', ln=True)

pdf.ln(25)
pdf.cell(80, 5, 'Sincerely,  ', ln=True)
pdf.ln(5)
pdf.cell(80, 5, 'Alkisah Binti Mubin,  ', ln=True)


"""
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('ai.png', 11, 9, 25)
        # font
        self.set_font('times', 'B', 16)
        # Padding
        self.cell(30)
        # Title
        self.cell(0, 12, 'Job Application Letter', border=True, ln=1, align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('times', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

# create FPDF object
# specify layout ('P','L')
# unit ('mm','cm','in')
# format ('A3','A4'(default),'Letter','Legal', (100,150)) numbers tu size (width, length)
pdf = FPDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

# add page
pdf.add_page()

# specify font, style, 
pdf.set_font('helvetica', 'BIU', 16)
pdf.set_font('times', '', 12)


# add text
#pdf.cell(50)
pdf.cell(100, 10, "Perantis Iskandar", 0, 1, 'L')

pdf.set_font('Times', '', 12)
pdf.cell(210, 10, 'Powered by FPDF.', 0, 0, 'C')
"""

pdf.output('application_letter.pdf')
