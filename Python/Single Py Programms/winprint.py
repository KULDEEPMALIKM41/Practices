from win32printing import Printer

font = {
    "height": 10,
    "faceName":"Courier New"
}
with Printer(linegap=1, margin=(15, 15, 15, 15)) as printer:
	printer.text("									", font_config={"height":8})
	printer.text("									", font_config={"height":8})
	printer.text("SK Doodh Dairy, Panmodi", font_config={"height":12})
	printer.text("    \tPhone 9351716375, 9358633459 ", font_config={"height":8})
	printer.text("									", font_config={"height":8})
	printer.text("Date : 19/08/20 07:30:59 ", font_config=font)
	printer.text("Shift : Morning ", font_config=font)
	printer.text("Code : 05 \tCow", font_config=font)
	printer.text("Name : Kuldeep Mali ", font_config=font)
	printer.text("Weight : 2.2M ", font_config=font)
	printer.text("Fat : 4.2M ", font_config=font)
	printer.text("CLR : 27 ", font_config=font)
	printer.text("Price(Rs./Li.) : 32 ", font_config=font)
	printer.text("Total : 70 ", font_config=font)

	# printer.new_page()
    # printer.text("title5", font_config=font)
    # printer.text("title6", font_config=font)
    # printer.text("title7", font_config=font)
    # printer.text("title8", font_config=font)

# import win32ui
# import win32print
# import win32con

# INCH = 1440

# hDC = win32ui.CreateDC ()
# hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
# hDC.StartDoc ("Test doc")
# hDC.StartPage ()
# hDC.SetMapMode (win32con.MM_TWIPS)
# hDC.DrawText ("SK Doodh Dairy, Panmodi \nPhone 9351716375, 9358633459 \nDate : 19/08/20 07:30:59", (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
# hDC.EndPage ()
# hDC.EndDoc ()


# import win32ui
# # X from the left margin, Y from top margin
# # both in pixels
# X=50; Y=50
# multi_line_string = input_string.split()
# hDC = win32ui.CreateDC ()
# hDC.CreatePrinterDC (your_printer_name)
# hDC.StartDoc (the_name_will_appear_on_printer_spool)
# hDC.StartPage ()
# for line in multi_line_string:
#      hDC.TextOut(X,Y,line)
#      Y += 100
# hDC.EndPage ()
# hDC.EndDoc ()