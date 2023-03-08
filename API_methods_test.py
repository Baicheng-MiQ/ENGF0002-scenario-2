# CHANGE ME!
def genTruthTable(question: str) -> dict:
    pass
    res = {
        "truthTableHeader": [],
        "truthTable": [[]]
    }
    return res

# CHANGE ME
def genAnswer(question: str) -> dict:
    pass
    res = {
        "answer": ""
    }
    return res

# CHANGE ME
def checkAnswer(question: str, answer: str) -> dict:
    pass
    res = {
        "isCorrect": True
    }
    return res


# Don't change the code below
def genTruthTableTest():
    # this test case from report 4.2.1
    question1: str = "(p & q -> r) & (!p -> !q | r)"
    expectedResult1: dict = {
        "truthTableHeader": ['p', 'q', 'r', question1],
        "truthTable": [
            [False, False, False, True],
            [False, False, True, True],
            [False, True, False, False],
            [False, True, True, True],
            [True, False, False, True],
            [True, False, True, True],
            [True, True, False, False],
            [True, True, True, True]
        ]
    }
    acturalResult1 = genTruthTable(question1)
    if expectedResult1["truthTableHeader"]!=acturalResult1["truthTableHeader"]:
        raise Exception("True Table Generation: Header is not correct")
    
    if len(expectedResult1["truthTable"])!=len(acturalResult1["truthTable"]):
        raise Exception("True Table Generation: Table length is not correct")
    
    for tableRow in expectedResult1["truthTable"]:
        if tableRow not in acturalResult1["truthTable"]:
            raise Exception("True Table Generation: Table content is not correct")
        
    print("✅ genTruthTableTest passed")


def genAnswerTest():
    question1: str = "((p -> q) | (r -> !q)) & ((p & r) -> q) "
    expectedResult1: dict ={
        "answer" : "(!p & !q & !r) | (!p & !q & r) | (!p & q & !r) | (!p & q & r) | (p & !q & !r)"
    }
    if genAnswer(question1) == expectedResult1:
            print("✅ genAnswerTest passed")

    splitedAnswer = genAnswer(question1)["answer"].split("|")
    if len(splitedAnswer) != len(splitedAnswer):
        raise Exception("Answer Generation: answer is not correct")
    for answer in splitedAnswer:
        if answer.strip() not in expectedResult1["answer"]:
            raise Exception("Answer Generation: answer is not correct")

    print("✅ genAnswerTest passed")



def checkAnswerTest():
    # question1, 2, 3 are basically the same, but with different receivedAnswer
    question1: str = "((p -> q) | (r -> !q)) & ((p & r) -> q) "
    receivedAnswer1: str = "(!p & !q & !r) | (!p & !q & r) | (!p & q & !r) | (!p & q & r) | (p & !q )" # wrong answer
    expectedResult1: dict = {
        "isCorrect": False
    }
    assert checkAnswer(question1, receivedAnswer1) == expectedResult1

    question2: str = "((p -> q) | (r -> !q)) & ((p & r) -> q) "
    receivedAnswer2: str = "(!p & !q & !r) | (!p & !q & r) | (!p & q & r) | (p & !q & !r) | (p & !q & r) | (p & q & r)" # correct answer
    expectedResult2: dict = {
        "isCorrect": True
    }
    assert checkAnswer(question2, receivedAnswer2) == expectedResult2

    question3: str = "((p -> q) | (r -> !q)) & ((p & r) -> q) "
    receivedAnswer3: str = "(!p & !q & !r) | (p & !q & r) | (p & q & r) | (!p & !q & r) | (p & !q & !r) | (!p & q & r)" # correct answer with different order
    expectedResult3: dict = {
        "isCorrect": True
    }
    assert checkAnswer(question3, receivedAnswer3) == expectedResult3

    print("✅ checkAnswerTest passed")

if __name__ == "__main__":
    genTruthTableTest()
    genAnswerTest()
    checkAnswerTest()

    print("All tests passed")
