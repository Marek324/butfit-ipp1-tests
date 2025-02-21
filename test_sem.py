from tests.utils_tests import run_test

def test_no_main1(monkeypatch, capsys):
    run_test("""
        class Man : Object {
            run [|
                x := 1.
            ]
        }
        """,
        31, monkeypatch, capsys)
    
def test_no_main2(monkeypatch, capsys):
    run_test("""
        class MyInt : Integer {}
        class Man : Object {
            run [|
                x := 1.
            ]
        }
        """,
        31, monkeypatch, capsys)
    
def test_no_run1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            ru [|
                x := 1.
            ]
        }
        """,
        31, monkeypatch, capsys)
    
def test_no_run2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            ru: [:b|
                x := b.
            ]
            r [|
                x := 1.
            ]
        }
        """,
        31, monkeypatch, capsys)
def test_undefined_class1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := MyInt new.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_undefined_class2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := MyInt from: 2.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_undefined_method1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := 1 pluus: 2.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_undefined_method2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := 1 plus: 2.
                y := 1 pluss: 2.
            ]
        }
        """,
        32, monkeypatch, capsys)
    

def test_undefined_method3(monkeypatch, capsys):
    run_test("""
        class Int : Integer {}
        class Main : Object {
            run [|
                x := Int new.
                y := x pluss: 2.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_undefined_method4(monkeypatch, capsys):
    run_test("""
        class Int : Integer {}
        class Main : Object {
            run [|
                x := Int new.
                y := x plus: 2.
                z := x pluss: 2.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_undefined_method5(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := Int new.
                y := x plus: 2.
                z := x pluss: 2.
            ]
        }
        class Int : Integer {}
        """,
        32, monkeypatch, capsys)
    
def test_undefined_var1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := y.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_undefined_var2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := y.
                y := 1.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_undefined_var3(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := y.
                y := 1.
                z := y.
            ]
        }
        """,
        32, monkeypatch, capsys)
    
def test_run_param(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [:a|
                x := a.
            ]
        }
        """,
        33, monkeypatch, capsys)
    
def test_arity1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [:a|
                x := a.
                y := a plus: 1.
            ]
        }
        """,
        33, monkeypatch, capsys)
    
def test_arity2(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := 1 abc: 2.
            ]
            abc: [|]
        }
        """,
        33, monkeypatch, capsys)
    
def test_arity3(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := 1 p: 2.
            ]
            p: [:a :b|]
        }
        """,
        33, monkeypatch, capsys)
    
def test_arity4(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|
                x := 1 p: 2.
            ]
            p:aaa: [:a :b :c|]
        }
        """,
        33, monkeypatch, capsys)
    
def test_collision_var1(monkeypatch, capsys):
    run_test("""
        class Main : Object {
            run [|]
            a: [:x | x := 1.]
        }
        """,
        34, monkeypatch, capsys)
    