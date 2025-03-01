import xml.etree.ElementTree as ET
import subprocess
import re

def run_arg_test(args, expected_code):
    args = ["python3.11", "parse.py"] + args
    process = subprocess.run(
        args,        
        capture_output=True,
        text=True
    )

    assert process.returncode == expected_code

    if expected_code == 0:
        assert len(process.stdout) != 0
    else:
        assert len(process.stderr) != 0

def run_test(input, expected_code):
    process = subprocess.run(
        ["python3.11", "parse.py"],
        input=input,        
        capture_output=True,
        text=True
    )

    print(process.stdout)
    
    assert process.returncode == expected_code
    
    assert len(process.stderr) != 0


def str_to_xml_s(x):
    return  ET.tostring(
            ET.fromstring(
            re.sub(r'&nbsp;', '\\\\n',
            re.sub(r'\s+=\s+', '=',
            re.sub(r'<\s+', '<',
            re.sub(r'\s+>', '>',
            re.sub(r'</\s+', '</',
            re.sub(r'\s+\/>', '/>',
            "".join(re.findall(r'<[^<>]*>', x.strip()))
            )))))))).decode('utf-8')

## Sort children based on their tags and attributes.
## Order can be different in equivalent xml.
## Children need to get in line 
def normalize_children(children):
    children[:] = sorted(children, key=lambda e: (e.tag, e.attrib.items()))

    return children

def compare_xml_elements(elem1, elem2):
    if elem1.tag != elem2.tag:
        return False
    if elem1.attrib != elem2.attrib:
        return False
    if len(elem1) != len(elem2):
        return False
    
    children1 = normalize_children(list(elem1))
    children2 = normalize_children(list(elem1))

    for child1, child2 in zip(children1, children2):
        if not compare_xml_elements(child1, child2):
            return False
        
    return True

def compare_xml_strings(xml_string1, xml_string2):
    try:
        elem1 = ET.fromstring(str_to_xml_s(xml_string1))
        elem2 = ET.fromstring(str_to_xml_s(xml_string2))
        return compare_xml_elements(elem1, elem2)
    except ET.ParseError:
        return False

def run_valid_test(input, expected_output):
    process = subprocess.run(
        ["python3.11", "parse.py"],
        input=input,        
        capture_output=True,
        text=True
    )

    print(process.stdout)

    assert process.returncode == 0 
    
    assert len(process.stderr) == 0
    assert len(process.stdout) != 0
    
    assert compare_xml_strings(process.stdout, expected_output)
    