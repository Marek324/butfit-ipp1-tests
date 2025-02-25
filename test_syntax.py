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
    
def test_reserved_id_asgn1():
    run_test("""
        class Main : Object {
            run [|
                self := 1.
            ]
        }
        """,
        22)
    
def test_reserved_id_asgn2():
    run_test("""
        class Main : Object {
            run [|
                super := 1.
            ]
        }
        """,
        22)

def test_reserved_id_asgn3():
    run_test("""
        class Main : Object {
            run [|
                true := 1.
            ]
        }
        """,
        22)
    
def test_reserved_id_asgn4():
    run_test("""
        class Main : Object {
            run [|
                false := 1.
            ]
        }
        """,
        22)
    
def test_reserved_id_asgn5():
    run_test("""
        class Main : Object {
            run [|
                nil := 1.
            ]
        }
        """,
        22)
    
def test_reserved_id_asgn6():
    run_test("""
        class Main : Object {
            run [|
                class := 1.
            ]
        }
        """,
        22)

def test_reserved_id_param1():
    run_test("""
        class Main : Object {
            run [|]
            a: [:self|]
        }
        """,
        22)
    
def test_reserved_id_param2():
    run_test("""
        class Main : Object {
            run [|]
            a: [:super|]
        }
        """,
        22)
    
def test_reserved_id_param3():
    run_test("""
        class Main : Object {
            run [|]
            a: [:true|]
        }
        """,
        22)
    
def test_reserved_id_param4():
    run_test("""
        class Main : Object {
            run [|]
            a: [:false|]
        }
        """,
        22)
    
def test_reserved_id_param5():
    run_test("""
        class Main : Object {
            run [|]
            a: [:nil|]
        }
        """,
        22)
    
def test_reserved_id_param6():
    run_test("""
        class Main : Object {
            run [|]
            a: [:class|]
        }
        """,
        22)

def test_reserved_id_sel1():
    run_test("""
        class Main : Object {
            run [|x := 1 self.]
        }
        """,
        22)

def test_reserved_id_sel2():
    run_test("""
        class Main : Object {
            run [|x := 1 super.]
        }
        """,
        22)
    
def test_reserved_id_sel3():
    run_test("""
        class Main : Object {
            run [|x := 1 true.]
        }
        """,
        22)
    
def test_reserved_id_sel4():
    run_test("""
        class Main : Object {
            run [|x := 1 false.]
        }
        """,
        22)
    
def test_reserved_id_sel5():
    run_test("""
        class Main : Object {
            run [|x := 1 nil.]
        }
        """,
        22)
    
def test_reserved_id_sel6():
    run_test("""
        class Main : Object {
            run [|x := 1 class.]
        }
        """,
        22)
    