from tests.utils_tests import run_valid_test


def test_minimal(monkeypatch, capsys):
    input = """
        class Main:Object{run[|]}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0"/>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)


def test_description1(monkeypatch, capsys):
    input = """
        class Main:Object{run[|]} "comment"
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
            <program language="SOL25" description="comment">
                <class name="Main" parent="Object">
                    <method selector="run">
                        <block arity="0"/>
                    </method>
                </class>
            </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_description2(monkeypatch, capsys):
    input = """
        class Main:Object{run[|]} "comment\nnewline"
        """
    exp_output = """
    <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25" description="comment&nbsp;newline">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0"/>
                </method>
            </class>
        </program>
    """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_description3(monkeypatch, capsys):
    input = """
        class Main:Object{run[|]} "comment" "another"
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
            <program language="SOL25" description="comment">
                <class name="Main" parent="Object">
                    <method selector="run">
                        <block arity="0"/>
                    </method>
                </class>
            </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_multiple_classes(monkeypatch, capsys):
    input = """
        class Main : Object {run [|]}
        class Main2 : Object {run [|]}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0"/>
                </method>
            </class>
            <class name="Main2" parent="Object">
                <method selector="run">
                    <block arity="0"/>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_multiple_methods(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [|]
            run2 [|]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0"/>
                </method>
                <method selector="run2">
                    <block arity="0"/>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_multiple_parameters(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [|]
            a:b:c: [:x :y :z |]
        ]
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0"/>
                </method>
                <method selector="a:b:c:">
                    <block arity="3">
                        <param order="1" name="x"/>
                        <param order="2" name="y"/>
                        <param order="3" name="z"/>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_multiple_assign(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 10.
                y := 5.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="Integer" value="10"/>
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="y"/>
                            <expr>
                                <literal class="Integer" value="5"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_inheritance(monkeypatch, capsys):
    input = """
        class Str : String {}
        class Main : Object {
            run [|
                x := Str2 read.  
            ]
        }
        class Str2 : Str {}
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Str" parent="String"/>
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <send selector="read">
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
            <class name="Str2" parent="Str"/>   
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_integer(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 10.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="Integer" value="10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_nil(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := nil.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="Nil" value="nil"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_true(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := true.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="True" value="true"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_false(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := false.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="False" value="false"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 'a10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string_lt(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 'a < 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a &lt; 10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string_gt(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 'a > 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a &gt; 10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string_amp(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 'a & 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a &amp; 10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string_apos(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 'a \\\' 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a &apos; 10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string_quot(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 'a " 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a &quot; 10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string_esc_nl(monkeypatch, capsys): # may be escaped newline
    input = """
        class Main : Object {
            run [| 
                x := 'a \\n 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a &nbsp; 10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_string_esc_backslash(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := 'a \\\\ 10'.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x"/>
                            <expr>
                                <literal class="String" value="a \\\\ 10"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_class_new(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := Integer new.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector ="new">
                                    <expr>
                                        <literal class="class" value="Integer" />
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_literal_class_from(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := Integer from: 1.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector ="from:">
                                    <expr>
                                        <literal class="class" value="Integer" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="1" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_assign_block(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := [|].
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector ="from:">
                                    <expr>
                                        <block arity="0"/>
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_assign_block_param(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                x := [:x|].
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector ="from:">
                                    <expr>
                                        <block arity="1">
                                            <parameter order="1" name="x"/>
                                        </block>
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)

def test_assign_var(monkeypatch, capsys):
    input = """
        class Main : Object {
            run [| 
                y := 1.
                x := y.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="y"/>
                            <expr>
                                <literal class="Integer" value="1"/>
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="y"/>
                            <expr>
                                <var name="y"/>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)


def test_example(monkeypatch, capsys):
    input = """
        class Main : Object {
            run "<- definice metody - bezparametrický selektor run"
            [ |
                x := self compute: 3 and: 2 and: 5.
                x := self plusOne: (self vysl).
                y := x asString .
            ]
            
            plusOne: 
            [ :x | 
                r := x plus: 1. 
            ]
            
            compute:and:and: 
            [ :x :y :z |    
                a := x plus: y.
                _ := self vysl: a.
                _ := (( self vysl) greaterThan: 0)
                ifTrue: [|u := self vysl: 1.]
                ifFalse: [|].
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25" description="&lt;- definice metody - bezparametrický selektor run">
            <class name="Main" parent="Object">
                <method selector="run">
                    <block arity="0">
                        <assign order="1">
                            <var name="x" />
                            <expr>
                                <send selector="compute:and:and:">
                                    <expr>
                                        <var name="self" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="3" />
                                        </expr>
                                    </arg>
                                    <arg order="2">
                                        <expr>
                                            <literal class="Integer" value="2" />
                                        </expr>
                                    </arg>
                                    <arg order="3">
                                        <expr>
                                            <literal class="Integer" value="5" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="x" />
                            <expr>
                                <send selector="plusOne:">
                                    <expr>
                                        <var name="self" />
                                    </expr>
                                    <arg order="1">
                                        <send selector="vysl">
                                            <expr>
                                                <var name="self" />
                                            </expr>
                                        </send>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="3">
                            <var name="y" />
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="x" />
                                    </expr>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>

                <method selector="plusOne:">
                    <block arity="1">
                        <parameter order="1" name="x" />
                        <assign order="1">
                            <var name="r" />
                            <expr>
                                <send selector="plus:">
                                    <expr>
                                        <var name="x" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="1" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>

                <method selector="compute:and:and:">
                    <block arity="3">
                        <parameter name="x" order="1" />
                        <parameter name="y" order="2" />
                        <parameter name="z" order="3" />
                        <assign order="1">
                            <var name="a" />
                            <expr>
                                <send selector="plus:">
                                    <expr>
                                        <var name="x" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <var name="y" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="2">
                            <var name="_" />
                            <expr>
                                <send selector="vysl:">
                                    <expr>
                                        <var name="self" />
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <var name="a" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                        <assign order="3">
                            <var name="_" />
                            <expr>
                                <send selector="ifTrue:ifFalse:">
                                    <expr>
                                        <send selector="greaterThan:">
                                            <expr>
                                                <send selector="vysl">
                                                    <expr>
                                                        <var name="self" />
                                                    </expr>
                                                </send>
                                            </expr>
                                            <arg order="1">
                                                <expr>
                                                    <literal class="Integer" value="0" />
                                                </expr>
                                            </arg>
                                        </send>
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <block arity="0">
                                                <assign order="1">
                                                    <var name="u" />
                                                    <expr>
                                                        <send selector="vysl:">
                                                        <expr>
                                                            <var name="self" />
                                                        </expr>
                                                        <arg order="1">
                                                            <expr>
                                                                <literal class="Integer" value="1" />
                                                            </expr>
                                                        </arg>
                                                        </send>
                                                    </expr>
                                                </assign>
                                            </block>
                                        </expr>
                                    </arg>
                                    <arg order="2">
                                        <expr>
                                            <block arity="0" />
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        </program>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)
