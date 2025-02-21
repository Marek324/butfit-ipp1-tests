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
    
    xml1 = ET.fromstring(captured_output.out)
    xml2 = ET.fromstring(expected_output)
    assert ET.tostring(xml1) == ET.tostring(xml2)
    