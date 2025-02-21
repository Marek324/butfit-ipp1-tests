from tests.utils_tests import run_test

def test_missing_colon():
    run_test("""
        class Main Object { 
            run [ | x := 5. ]
        }
        """,
        22)
    
def test_invalid_class_id1():
    run_test("""
        class main : Object { 
            run [ | x := 5. ]
        }
        """,
        22)
    
def test_invalid_class_id2():
    run_test("""
        class Main : object { 
            run [ | x := 5. ]
        }
        """,
        22)
    
def test_unterminated_block():
    run_test("""
        class Main Object { 
            run [ | x := 5.
        }
        """,
        22)
    
def test_block_missing_pipe():
    run_test("""
        class Main Object { 
            run [ x := 5. ]
        }
        """,
        22)
    
def test_missing_dot():
    run_test("""
        class Main Object { 
            run [ | x := 5 ]
        }
        """,
        22)
    
def test_unterminated_class():
    run_test("""
        class Main Object { 
            run [ | x := 5. ]
        """,
        22)
    
def test_missing_class():
    run_test("""
        Main : Object { 
            run [ | x := 5. ]
        }
        """,
        22)
    
def test_missing_class_id():
    run_test("""
        class : Object { 
            run [ | x := 5. ]
        }
        """,
        22)
    
def test_missing_class_body():
    run_test("""
        class Main: Object 
        """,
        22)

def test_invalid_parameter1():
    run_test("""
        class Main Object { 
            run [ x := 5. | ]
        }
        """,
        22)
    
def test_invalid_parameter2():
    run_test("""
        class Main Object { 
            run [ x := 5. | y ]
        }
        """,
        22)
    
def test_invalid_parameter3():
    run_test("""
        class Main : Object {
            run [
                :Main |
                x := 5.
            ]
        }
        """, 
        22)
    
def test_invalid_parameter4():
    run_test("""
        class Main : Object {
            run [
                Main |
                x := 5.
            ]
        }
        """, 
        22)
    

def test_unclosed_parentheses():
    run_test("""
        class Main : Object { 
            run [ | x := (5. ]
        }
        """,
        22)
    
def test_invalid_send():
    run_test("""
        class Main : Object { 
            run [ | x := 5 timesRepeat:. ]
        }
        """,
        22)

def test_selector1():
    run_test("""
        class Main : Object { 
            Integer [ | x := 5.  ]
        }
        """,
        22)
    
def test_selector2():
    run_test("""
        class Main : Object { 
            I_run [ | x := 5.  ]
        }
        """,
        22)
    
def test_selector3():
    run_test("""
        class Main : Object { 
            :run [ | x := 5.  ]
        }
        """,
        22)
    
def test_selector4():
    run_test("""
        class Main : Object { 
            run: a [ | x := 5.  ]
        }
        """,
        22)
    
def test_selector5():
    run_test("""
        class Main : Object { 
            run: a: b [ | x := 5.  ]
        }
        """,
        22)
    
def test_block_param_space():
    run_test("""
        class Main : Object {
            run [ : y |
                x := 5.
            ]
        }
        """,
        22)

def test_selector_space1():
    run_test("""
        class Main : Object {
            run [|
                x := a add : b.
            ]
        }
        """,
        22)
    
def test_selector_space2():
    run_test("""
        class Main : Object {
            run :[|
                x := a add: b.
            ]
        }
        """,
        22)
    
def test_selector_space3():
    run_test("""
        class Main : Object {
            run: a : [|
                x := a add: b.
            ]
        }
        """,
        22)
