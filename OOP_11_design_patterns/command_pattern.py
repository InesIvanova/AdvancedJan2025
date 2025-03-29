from abc import ABC, abstractmethod


class Checker(ABC):
    @abstractmethod
    def check(self, file) -> bool:
        pass



class HeadersPresentedChecker(Checker):
    required_columns = ("age", "gender", "town")
    def check(self, file) -> bool:
        for required_column in self.required_columns:
            if required_column not in file.columns:
                return False

        return True


class AgeChecker(Checker):

    def check(self, file):
        all_ages = file["age"]
        for age in all_ages:
            if age not in range(18,65):
                return False
        return True



checks = (HeadersPresentedChecker(), AgeChecker())


class FileApprover:
    def run(self, file):
        for rule in checks:
            rule.check(file)


    def visualise(self):
        return ""


a = FileApprover()
a.run()
a.visualise()

