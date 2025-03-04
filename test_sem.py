from tests.utils_tests import run_test

def test_no_main1():
    run_test("""
        class Man1 : Object {
            run [|
                x := 1.
            ]
        }
        """,
        31)
    
def test_no_main2():
    run_test("""
        class MyInt : Integer {}
        class Man2 : Object {
            run [|
                x := 1.
            ]
        }
        """,
        31)
    
def test_no_main3():
    run_test("""
        """,
        31)
    
def test_no_run1():
    run_test("""
        class Main : Object {
            ru1 [|
                x := 1.
            ]
        }
        """,
        31)
    
def test_no_run2():
    run_test("""
        class Main : Object {
            ru2: [:b|
                x := b.
            ]
            r [|
                x := 1.
            ]
        }
        """,
        31)
    
def test_no_run3():
    run_test("""
        class Main : Object {
            run: [:b|
                x := b.
            ]
            r [|
                x := 1.
            ]
        }
        """,
        31)

def test_no_run4():
    run_test("""
        class Main : Object {}
        """,
        31)
    
def test_undefined_class1():
    run_test("""
        class Main : Object {
            run [|
                x := MyInt1 new.
            ]
        }
        """,
        32)
    
def test_undefined_class2():
    run_test("""
        class Main : Object {
            run [|
                x := MyInt2 from: 2.
            ]
        }
        """,
        32)
    
def test_undefined_class3():
    run_test("""
        class Main : Object {
            run [|]
        }
        class MyInt3 : Int4 {}
        """,
        32)
    
def test_undefined_var1():
    run_test("""
        class Main : Object {
            run [|
                x := y.
            ]
        }
        """,
        32)
    
def test_undefined_var2():
    run_test("""
        class Main : Object {
            run [|
                x := y.
                y := 1.
            ]
        }
        """,
        32)
    
def test_undefined_var3():
    run_test("""
        class Main : Object {
            run [|
                x := y.
                y := 1.
                z := y.
            ]
        }
        """,
        32)
    
def test_undefined_var4():
    run_test("""
        class Main : Object {
            run [|
                x := 1 plus: y.
                y := 1.
                z := y.
            ]
        }
        """,
        32)
    
def test_undefined_var5():
    run_test("""
        class Main : Object {
            run [|
                x := 1 plus: 1 plus: y.
                y := 1.
                z := y.
            ]
        }
        """,
        32)
    
def test_undefined_class_method1():
    run_test("""
        class Main : Object {
            run [|
                x := Integer ne.
            ]
        }
        """,
        32)
    
def test_undefined_class_method2():
    run_test("""
        class Main : Object {
            run [|
                x := String b.
            ]
        }
        """,
        32)
    
def test_undefined_class_method3():
    run_test("""
        class Main : Object {
            run [|
                x := Integer read.
            ]
        }
        """,
        32)
    
def test_undefined_class_method4():
    run_test("""
        class Main : Object {
            run [|
                x := Integer ne: (Integer from:1) be: 2.
            ]
        }
        """,
        32)

def test_undefined_class_method5():
    run_test("""
        class Main : Object {
            run [|
                x := Integer from: (Integer from:1 be: 2).
            ]
        }
        """,
        32)
    
def test_undefined_class_method6():
    run_test("""
        class Main : Object {
            run [|
                x := FakeString read.
            ]
        }
        class FakeString : Integer {}
        """,
        32)

def test_run_param():
    run_test("""
        class Main : Object {
            run [:a|
                x := a.
            ]
        }
        """,
        33)
    
def test_arity1():
    run_test("""
        class Main : Object {
            run [:a|
                x := a.
                y := a plus: 1.
            ]
        }
        """,
        33)
    
def test_arity2():
    run_test("""
        class Main : Object {
            run [|
                x := self abc2: 2.
            ]
            abc2: [|]
        }
        """,
        33)
    
def test_arity3():
    run_test("""
        class Main : Object {
            run [|
                x := self p3: 2.
            ]
            p3: [:a :b|]
        }
        """,
        33)
    
def test_arity4():
    run_test("""
        class Main : Object {
            run [|
                x := self p4: 2 aa4a: 2.
            ]
            p4:aa4a: [:a :b :c|]
        }
        """,
        33)
    
def test_collision_var1():
    run_test("""
        class Main : Object {
            run [|]
            a1: [:x | x := 1.]
        }
        """,
        34)

def test_collision_var2():
    run_test("""
        class Main : Object {
            run [|]
            a2:b2: [:x :x | a := 1.]
        }
        """,
        35)
        
def test_class_redef1():
    run_test("""
        class Main : Object {
            run [|]
        }
        class A:Integer{}
        class A:Integer{}
        """,
        35)

