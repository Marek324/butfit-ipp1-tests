import pytest
import sys
import io
import xml.etree.ElementTree as ET

from parse import main

def run_arg_test(args, expected_code, capsys):
    sys.argv = ['parse.py'] + args
    with pytest.raises(SystemExit) as e:
        main()
    
    assert e.value.code == expected_code
    captured_output = capsys.readouterr()
    if expected_code == 0:
        assert len(captured_output.out) != 0
    else:
        assert len(captured_output.err) != 0

def run_test(input, expected_code, monkeypatch, capsys):
    sys.argv = ['parse.py']
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input))
    with pytest.raises(SystemExit) as e:
        main()
    
    assert e.value.code == expected_code
    
    captured_output = capsys.readouterr()
    assert len(captured_output.err) != 0

def compare_xml_elements(elem1, elem2):
    if elem1.tag != elem2.tag:
        return False
    if elem1.attrib != elem2.attrib:
        return False
    if len(elem1) != len(elem2):
        return False
    for child1, child2 in zip(elem1, elem2):
        if not compare_xml_elements(child1, child2):
            return False
    return True

def compare_xml_strings(xml_string1, xml_string2):
    try:
        elem1 = ET.fromstring(xml_string1.strip())
        elem2 = ET.fromstring(xml_string2.strip())
        return compare_xml_elements(elem1, elem2)
    except ET.ParseError:
        return False  # Handle invalid XML

def run_valid_test(input, expected_output, monkeypatch, capsys):
    sys.argv = ['parse.py']
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input))
    try:
        ret = main()
        assert ret is None
    except SystemExit as e:
        assert e.code == 0
    
    captured_output = capsys.readouterr()
    assert len(captured_output.err) == 0
    assert len(captured_output.out) != 0
    
    assert compare_xml_strings(captured_output.out, expected_output)
    