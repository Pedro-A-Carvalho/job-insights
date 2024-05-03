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
        jobs_with_salaries = [
            job
            for job in jobs
            if job["min_salary"] != ""
            and job["max_salary"] != ""
            and int(job["max_salary"]) >= int(job["min_salary"])
        ]
        try:
            if isinstance(salary, int) or isinstance(salary, str):
                filtered_jobs = [
                    job
                    for job in jobs_with_salaries
                    if self.matches_salary_range(job, int(salary))
                ]
                # print("*" * 10)
                # print("*" * 10)
                # print(jobs)
                # print(salary)
                # print(filtered_jobs)
                # print("*" * 10)
                # print(jobs_with_salaries)
                # print("*" * 10)
                # print("*" * 10)
                return filtered_jobs
            return []
        except ValueError:
            return []
        # pass
