import xml.etree.ElementTree as ET
from pathlib import Path
import re
def prohibition2mandatory(tree):
    for child in tree.getroot().findall(".//{http://www.w3.org/2000/svg}path"):
        style = child.attrib.get("style")
        if style:
            if m := re.search(r"fill:\s*(#[0-9A-Fa-f]+)", style):
                child.attrib["fill"] = m.group(1)
                child.attrib["style"] = child.attrib["style"].replace(m.group(),"")
            
        fill=child.attrib.get("fill")
        if fill=="#b71f2e":
            child.clear() 
        elif fill in ("#fff","#ffffff"):
            child.attrib["fill"] = "#24578e"
        elif fill in ("#000","#000000", "#0e1313"):
            child.attrib["fill"] = "#fff"
        elif not fill:
            child.attrib["fill"]="#fff"
        stroke = child.attrib.get("stroke")
        if stroke in ("#000","#000000"):
            child.attrib["stroke"]="#fff"

            
    return tree


if __name__=="__main__":
    source_dir = Path("source_images/gallery-dl/wikimediacommons/Category:ISO_7010_prohibition_signs/")
    target_dir = Path("outputs/prohibition2mandatory")
    README = []
    for sp in source_dir.glob("*.svg"):
        tree = prohibition2mandatory(ET.parse(sp))
        tp = target_dir.joinpath(sp.name)
        tree.write(tp)
        README.append(f"![image]({sp.name})\n")
    with open(target_dir.joinpath("README.md"),"w") as f:
        f.writelines(README)
        
        

    

