# Use for print Header and footer in any code with TimeDtamp

from datetime import datetime

def Header(Hname, fobj):
    Border = "-" * 90
    title = Hname
    timestamp = datetime.now().strftime("Date: %Y-%m-%d    Time: %H:%M:%S")

    fobj.write(Border + "\n")
    fobj.write(f"{title.center(90)}\n")
    fobj.write(f"{timestamp.center(90)}\n")
    fobj.write(Border + "\n")

def Footer(Fname, fobj):
    Border = "-" * 90
    endline = Fname

    fobj.write(Border + "\n")
    fobj.write(f"{endline.center(90)}\n")
    fobj.write(Border + "\n")
