from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    #set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 24, 200, 24)

    # creating horizontal lines
    gap = 40
    while gap < 290:
        pdf.line(10, gap, 200, gap)
        gap = gap + 10

    # set the footer
    pdf.ln(260)

    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # creating horizontal lines
        gap = 20
        while gap < 290:
            pdf.line(10, gap, 200, gap)
            gap = gap + 10

        # set the footer
        pdf.ln(272)

        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)


pdf.output("output.pdf")