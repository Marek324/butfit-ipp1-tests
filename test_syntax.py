from tests.utils_tests import run_test

def test_missing_colon(monkeypatch, capsys):
    run_test("""
        class Main Object { 
            run [ | x := 5. ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_invalid_class_id1(monkeypatch, capsys):
    run_test("""
        class main : Object { 
            run [ | x := 5. ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_invalid_class_id2(monkeypatch, capsys):
    run_test("""
        class Main : object { 
            run [ | x := 5. ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_unterminated_block(monkeypatch, capsys):
    run_test("""
        class Main Object { 
            run [ | x := 5.
        }
        """,
        22, monkeypatch, capsys)
    
def test_block_missing_pipe(monkeypatch, capsys):
    run_test("""
        class Main Object { 
            run [ x := 5. ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_missing_dot(monkeypatch, capsys):
    run_test("""
        class Main Object { 
            run [ | x := 5 ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_unterminated_class(monkeypatch, capsys):
    run_test("""
        class Main Object { 
            run [ | x := 5. ]
        """,
        22, monkeypatch, capsys)
    
def test_missing_class(monkeypatch, capsys):
    run_test("""
        Main : Object { 
            run [ | x := 5. ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_missing_class_id(monkeypatch, capsys):
    run_test("""
        class : Object { 
            run [ | x := 5. ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_missing_class_body(monkeypatch, capsys):
    run_test("""
        class Main: Object 
        """,
        22, monkeypatch, capsys)

def test_invalid_parameter1(monkeypatch, capsys):
    run_test("""
        class Main Object { 
            run [ x := 5. | ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_invalid_parameter2(monkeypatch, capsys):
    run_test("""
        class Main Object { 
            run [ x := 5. | y ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_invalid_parameter3(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [
                :Main |
                x := 5.
            ]
        }
        """, 
        22, monkeypatch, capsys)
    
def test_invalid_parameter4(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [
                Main |
                x := 5.
            ]
        }
        """, 
        22, monkeypatch, capsys)
    

def test_unclosed_parentheses(monkeypatch, capsys):
    run_test("""
        class Main : Object { 
            run [ | x := (5. ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_invalid_send(monkeypatch, capsys):
    run_test("""
        class Main : Object { 
            run [ | x := 5 timesRepeat:. ]
        }
        """,
        22, monkeypatch, capsys)

def test_selector1(monkeypatch, capsys):
    run_test("""
        class Main : Object { 
            Integer [ | x := 5.  ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_selector2(monkeypatch, capsys):
    run_test("""
        class Main : Object { 
            I_run [ | x := 5.  ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_selector3(monkeypatch, capsys):
    run_test("""
        class Main : Object { 
            :run [ | x := 5.  ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_selector4(monkeypatch, capsys):
    run_test("""
        class Main : Object { 
            run: a [ | x := 5.  ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_selector5(monkeypatch, capsys):
    run_test("""
        class Main : Object { 
            run: a: b [ | x := 5.  ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_block_param_space(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [ : y |
                x := 5.
            ]
        }
        """,
        22, monkeypatch, capsys)

def test_selector_space1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := a add : b.
            ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_selector_space2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run :[|
                x := a add: b.
            ]
        }
        """,
        22, monkeypatch, capsys)
    
def test_selector_space3(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run: a : [|
                x := a add: b.
            ]
        }
        """,
        22, monkeypatch, capsys)
