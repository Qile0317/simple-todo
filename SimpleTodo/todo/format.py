
import datetime as dt

class TodoEncoder:
    
    @classmethod
    def to_string(cls,
        is_finished: bool,
        priority: str,
        start_date: dt.datetime,
        end_date: dt.datetime,
        task: str,
        project: str,
        context: str,
        maths: str,
    ) -> str:
        
        return " ".join([
            cls.completion(is_finished),
            cls.priority(priority),
            cls.date(start_date),
            cls.date(end_date),
            cls.task(task),
            cls.project(project),
            cls.context(context),
            cls.maths(maths),
        ])
    
    def completion(is_finished: bool):
        return 'x' if is_finished else '-'
    
    def priority(priority: str):
        return f"({priority})"
    
    def date(datetime: dt.datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    def task(task: str):
        return task
    
    def project(project: str):
        return f"+{project}"
    
    def context(context: str):
        return f"@{context}"
    
    def maths(maths: str):
        return f"={maths}"

class TodoDecoder:
    
    @classmethod
    def from_string(cls, string: list[str]):
        words = string.split(' ')
        return [
            cls.is_finished(words[0]),
            cls.priority(words[1]),
            cls.date(' '.join(words[2:4])),
            cls.date(' '.join(words[4:6])),
            cls.task(' '.join(words[6:-3])),
            cls.project(words[-3]),
            cls.context(words[-2]),
            cls.maths(words[-1]),
        ]
    
    def is_finished(completion: str):
        return completion == 'x'

    def priority(priority: str):
        return priority.strip('()')
    
    def date(string: str):
        try:
            return dt.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return dt.datetime.now()
    
    def task(task: str):
        return task
    
    def project(project: str):
        return project[1:]
    
    def context(context: str):
        return context[1:]
    
    def maths(maths: str):
        return maths[1:]