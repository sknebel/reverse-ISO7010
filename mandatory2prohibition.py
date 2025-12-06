import xml.etree.ElementTree as ET
from pathlib import Path
import re
def prohibition2mandatory(tree):
    for child in tree.getroot().findall(".//{http://www.w3.org/2000/svg}*"):
        style = child.attrib.get("style")
        if style:
            if m := re.search(r"fill:\s*(#[0-9A-Fa-f]+)", style):
                child.attrib["fill"] = m.group(1)
                child.attrib["style"] = child.attrib["style"].replace(m.group(),"")
            elif m := re.search(r"fill:rgb\(0,83,135\);", style):
                child.attrib["fill"] = "#23548c"
                child.attrib["style"] = child.attrib["style"].replace(m.group(),"")
            elif m := re.search(r"fill:004488;", style):
                child.attrib["fill"] = "#23548c"
                child.attrib["style"] = child.attrib["style"].replace(m.group(),"")
            elif m := re.search(r"fill:white;", style):
                child.attrib["fill"] = "#000"
                child.attrib["style"] = child.attrib["style"].replace(m.group(),"")

            style = child.attrib.get("style")
            if m := re.search(r"stroke:white;", style):
                child.attrib["style"] = child.attrib["style"].replace(m.group(),"stroke:black;")


            
        fill=child.attrib.get("fill")
        #if fill=="#b71f2e":
        #    child.clear()
        if fill in ("#fff","#ffffff"):
            child.attrib["fill"] = "#000"
        elif fill in ("#004488",):
            child.attrib["fill"] = "#fff"
        elif fill and fill.startswith("#2"):
            child.attrib["fill"] = "#fff"
        #elif not fill:
        #    child.attrib["fill"]="#fff"
        stroke = child.attrib.get("stroke")
        if stroke:
            print("stroke")
        if stroke in ("#fff","#ffffff"):
            child.attrib["stroke"]="#000"

            
    return tree


if __name__=="__main__":
    source_dir = Path("source_images/gallery-dl/wikimediacommons/Category:ISO_7010_mandatory_action_signs/")
    target_dir = Path("outputs/mandatory2prohibition")
    README = []
    for sp in source_dir.glob("*.svg"):
        tree = prohibition2mandatory(ET.parse(sp))
        tp = target_dir.joinpath(sp.name)
        tree.write(tp)
        README.append(f"![image](<{sp.name}>)\n")
    with open(target_dir.joinpath("README.md"),"w") as f:
        f.writelines(README)
        
        

    

