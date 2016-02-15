import ast
from pythonwhat.State import State
from pythonwhat.Reporter import Reporter
from pythonwhat.Test import Test


def test_while_loop(index=1,
                    test=None,
                    body=None,
                    orelse=None,
                    expand_message=True):
    state = State.active_state
    rep = Reporter.active_reporter

    index = index - 1

    student_env, solution_env = state.student_env, state.solution_env

    state.extract_while_calls()
    student_whiles = state.student_while_calls
    solution_whiles = state.solution_while_calls

    try:
        lineno_student, test_student, body_student, orelse_student = student_whiles[
            index]
    except:
        rep.do_test(Test("Define more `while` loops."))
        return

    lineno_solution, test_solution, body_solution, orelse_solution = solution_whiles[
        index]

    def sub_test(closure, subtree_student, subtree_solution, incorrect_part):
        if closure:
            failed_before = rep.failed_test
            child = state.to_child_state(subtree_student, subtree_solution)
            closure()
            child.to_parent_state()
            if expand_message and (failed_before is not rep.failed_test):
                rep.feedback_msg = rep.feedback_msg + " in the " + incorrect_part + \
                    " of the `while` loop on line " + str(lineno_student) + "."

    sub_test(test, test_student, test_solution, "condition")
    sub_test(body, body_student, body_solution, "body")
    sub_test(orelse, orelse_student, orelse_solution, "else part")
