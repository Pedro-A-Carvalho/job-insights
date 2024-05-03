from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salaries = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"] != "" and job["max_salary"].isdigit()
        ]
        return max(max_salaries)

    def get_min_salary(self) -> int:
        max_salaries = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"] != "" and job["min_salary"].isdigit()
        ]
        return min(max_salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if (
            "min_salary" not in job
            or "max_salary" not in job
            or not str(job.get("min_salary")).isnumeric()
            or not str(job.get("max_salary")).isnumeric()
            or int(job.get("min_salary")) >= int(job.get("max_salary"))
        ):
            raise ValueError("Min or Max salary are invalid")
        elif not isinstance(salary, str) and not isinstance(salary, int):
            # print("------------****************")
            # #     print(int(salary))
            # #     print(job)
            # print(isinstance(salary, str))
            # print(isinstance(salary, int))
            # print("------------****************")
            raise ValueError("Salary is an invalid value")
        else:
            return (
                int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
            )

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
