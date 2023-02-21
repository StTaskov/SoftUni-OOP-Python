class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skill_needed):
        if self.skills >= skill_needed and not self.language == new_language:
            old_language = self.language
            self.language = new_language
            return f"{self.name} switched from {old_language} to {new_language}"
        elif self.skills >= skill_needed and self.language == new_language:
            return f"{self.name} already knows {self.language}"
        return f"{self.name} needs {skill_needed - self.skills} more skills"


programmer = Programmer("Lemmy", "Java", 100)
print(programmer.change_language("Python", 50))
