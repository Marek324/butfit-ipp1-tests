from tests.utils_tests import run_valid_test

def test_valid1(monkeypatch, capsys):
    input = """
        class Main : Object { "Main class"
            run [
                | x := 10.
                x := x plus: 5.
            ]
        }
        """
    exp_output = """
        <?xml version="1.0" encoding="UTF-8"?>
        <program language="SOL25" description="Main class">
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
                            <var name="x"/>
                            <expr>
                                <send selector="plus:">
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="5"/>
                                        </expr>
                                    </arg>
                                </send>
                            </expr>
                        </assign>
                    </block>
                </method>
            </class>
        """
    run_valid_test(input, exp_output, monkeypatch, capsys)