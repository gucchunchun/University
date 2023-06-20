from enum import Enum

class Subject(Enum):
    Biology = 0
    History = 1
    Math = 2
    English = 3


class SubjectResult:
    subject: Subject
    score: float
    maxScore: int

    def GetPercentage(self):
        return (self.score / self.maxScore) * 100
    
    def __init__(self, subject, score, maxScore):
        self.subject = subject
        self.score = score
        self.maxScore = maxScore
        

class ExamResult:
    name: str

    def __init__(self, name):
        self.name = name
        self.arraySubjects = []

    def Add(self, subjectResult):
        self.arraySubjects.append(subjectResult)
    
    def PrintResults(self):
        print("\t" + self.name + "\n")
        for subj in self.arraySubjects:
            print(subj.subject.name + ' ' + str(subj.score) + " / " + str(subj.maxScore) + " --> percentage: " + str(subj.GetPercentage()) + "\n")


YunaExamResult = ExamResult("yuna")
YunaExamResult.Add(SubjectResult(Subject.Biology, 40.5, 100))
YunaExamResult.Add(SubjectResult(Subject.Math, 65.5, 100))
YunaExamResult.Add(SubjectResult(Subject.English, 20.5, 100))


examresult2 = ExamResult("bob")
examresult2.Add(SubjectResult(Subject.Biology, 55.5, 100))
examresult2.Add(SubjectResult(Subject.Math, 77.5, 100))
examresult2.Add(SubjectResult(Subject.English, 33.5, 100))

YunaExamResult.PrintResults()
examresult2.PrintResults()
