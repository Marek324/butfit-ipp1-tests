from tests.utils_tests import run_test

def test_unclosed_comment1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                "abc
                A_BH_oj := 10.
            ]
        }
        """,
        21)
    
def test_unclosed_comment2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            "Toto je neuzavretý komentár
            run [| |]
        }
        """,
        21)

def test_num_literal1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := +-12.
            ]
        }
        """,
        21)
    
def test_num_literal2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := -+12.
            ]
        }
        """,
        21)
    
def test_num_literal3(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := -.
            ]
        }
        """,
        21)
    
def test_num_literal4(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := +-.
            ]
        }
        """,
        21)
    
def test_num_literal5(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := -0,10.
            ]
        }
        """,
        21)
    
def test_str_literal1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := '\\a'.
            ]
        }
        """,
        21)
    
def test_str_literal2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := '\\\n'.
            ]
        }
        """,
        21)
    
def test_str_literal3(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := '\\a'.
            ]
        }
        """,
        21)

def test_str_literal4(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := 'abc.
            ]
        }
        """,
        21)
    
def test_str_literal5(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := 'Nesprávny escape: \\x'.
            ]
        }
        """,
        21)

def test_selector1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := a a+: msg.
            ]
        }
        """,
        21)

def test_selector2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := a + 1.
            ]
        }
        """,
        21)
    
def test_id1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := a@.
            ]
        }
        """,
        21)

def test_id2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := _/a.
            ]
        }
        """,
        21)

