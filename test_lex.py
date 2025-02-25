from tests.utils_tests import run_test

def test_unclosed_comment1():
    run_test("""
        class Main : Object {
            run [|
                "abc
                A_BH_oj := 10.
            ]
        }
        """,
        21)
    
def test_unclosed_comment2():
    run_test("""
        class Main : Object {
            "Toto je neuzavretý komentár
            run [| |]
        }
        """,
        21)

def test_num_literal1():
    run_test("""
        class Main : Object {
            run [|
                x := +-12.
            ]
        }
        """,
        21)
    
def test_num_literal2():
    run_test("""
        class Main : Object {
            run [|
                x := -+12.
            ]
        }
        """,
        21)
    
def test_num_literal3():
    run_test("""
        class Main : Object {
            run [|
                x := -.
            ]
        }
        """,
        21)
    
def test_num_literal4():
    run_test("""
        class Main : Object {
            run [|
                x := +-.
            ]
        }
        """,
        21)
    
def test_num_literal5():
    run_test("""
        class Main : Object {
            run [|
                x := -0,10.
            ]
        }
        """,
        21)
    
def test_str_literal1():
    run_test("""
        class Main : Object {
            run [|
                x := '\\a'.
            ]
        }
        """,
        21)
    
def test_str_literal2():
    run_test("""
        class Main : Object {
            run [|
                x := '\n'.
            ]
        }
        """,
        21)

def test_str_literal3():
    run_test("""
        class Main : Object {
            run [|
                x := 'abc.
            ]
        }
        """,
        21)
    
def test_str_literal4():
    run_test("""
        class Main : Object {
            run [|
                x := 'Nesprávny escape: \\x'.
            ]
        }
        """,
        21)

def test_selector1():
    run_test("""
        class Main : Object {
            run [|
                x := a a+: msg.
            ]
        }
        """,
        21)

def test_selector2():
    run_test("""
        class Main : Object {
            run [|
                x := a + 1.
            ]
        }
        """,
        21)
    
def test_id1():
    run_test("""
        class Main : Object {
            run [|
                x := a@.
            ]
        }
        """,
        21)

def test_id2():
    run_test("""
        class Main : Object {
            run [|
                x := _/a.
            ]
        }
        """,
        21)

