from win32 import win32api
import win32print
import win32ui
import json
import sys
import win32con


def printBill(data, printer_name):
    line = "--------------------------------------------------------------------------------------------------"
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC(printer_name)
    dc.StartDoc("Print Text")
    dc.StartPage()
    # header
    y = -10
    font_name = "Arial"
    font_size = 80
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))

    dc.TextOut(145, y, data['shop_name'])

    font_size = 40
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))

    y = y + 65
    dc.TextOut(145, y, "R E S T U R E N T")
    font_size = 30
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))

    y = y + 40
    dc.TextOut(145, y, data['shop_address'])
    y = y + 35
    dc.TextOut(165, y, data['telephone'])

    font_size = 20
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    y = y + 25
    dc.TextOut(0, y, line)

    font_size = 30
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    y = y + 25

    tblData = "Table: " + data['table_id']
    if (data['table_id'] == ""):
        tblData = "Take Away"

    dc.TextOut(0, y, "Bill No: " + str(data['bill_id']))
    # dc.TextOut(0,y"Table: "+data['table_id'])
    dc.TextOut(390, y, tblData)
    y = y + 30
    dc.TextOut(0, y, data['date'])

    font_size = 20
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    y = y + 25
    dc.TextOut(0, y, line)

    font_size = 30
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 700  # 400 corresponds to normal weight
    }))
    y = y + 25

    total = 0.0

    dc.TextOut(90, y, "Qty")
    dc.TextOut(250, y, "Price")
    dc.TextOut(470, y, "Total")
    y = y + 35

    font_size = 20
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    dc.TextOut(0, y, line)

    font_size = 30
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    y = y + 25
    # --------------------------------------------------------------------------
    # dc.TextOut(300,y,"{:>10}".format("%.2f"%i["Price"]))
    # dc.TextOut(430,y, "{:>10}".format("%.2f"% (i["Quantity"] *i["Price"] )))

    for i in data["items"]:
        # dc.SetTextAlign(win32con.TA_LEFT | win32con.TA_BASELINE)
        dc.TextOut(0, y, i["Description"])
        y = y + 35
        dc.TextOut(100, y, str(i["Quantity"]))
        # dc.SetTextAlign(win32con.TA_RIGHT | win32con.TA_BASELINE)
        dc.TextOut(200, y, "{:>10}".format("%.2f" % i["Price"]))
        dc.TextOut(430, y, "{:>10}".format("%.2f" % (i["Quantity"] * i["Price"])))
        y = y + 35
        total = total + (i["Quantity"] * i["Price"])

    font_size = 20
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    dc.TextOut(0, y, line)

    font_size = 50
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    y = y + 25

    dc.TextOut(250, y, "Total: " + str("%.2f" % total))

    font_size = 20
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    y = y + 55
    dc.TextOut(0, y, line)

    font_size = 30
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))

    y = y + 25
    dc.TextOut(0, y, "Note: " + str(data["note"]))

    font_size = 20
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))
    y = y + 35
    dc.TextOut(0, y, line)

    font_size = 30
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 400  # 400 corresponds to normal weight
    }))

    y = y + 25
    dc.TextOut(150, y, "Thank You Come Again!")

    font_size = 20
    dc.SelectObject(win32ui.CreateFont({
        "name": font_name,
        "height": font_size,
        "weight": 700  # 400 corresponds to normal weight
    }))
    y = y + 35
    dc.TextOut(155, y, "Solution by CodGlo - 0779 438 974")

    y = y + 50
    dc.TextOut(155, y, "")

    dc.EndPage()
    dc.EndDoc()
    dc.DeleteDC()

    pass


def jsonTodict(filepath, printer_name):
    data = {}
    with open(filepath, 'r') as file:
        data = json.load(file)
    print(data)
    printBill(data, printer_name)
    pass


jsonTodict("11.json","")

# num_args = len(sys.argv)
# if (num_args == 3):
#     printer_name = sys.argv[1]
#     file_path = sys.argv[2]
#     jsonTodict(file_path, printer_name)