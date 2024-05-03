from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            self.jobs_list = list(reader)
        return self.jobs_list
        # pass

    def get_unique_job_types(self) -> List[str]:
        return list({job["job_type"] for job in self.jobs_list})

    def filter_by_multiple_criteria(
        self, jobs_dict, filters_dict
    ) -> List[dict]:
        if not isinstance(filters_dict, dict):
            raise TypeError("The filter must be a dict")
        industryFilter = filters_dict.get("industry") is None
        jobFilter = filters_dict.get("job_type") is None

        return [
            job
            for job in jobs_dict
            if (
                industryFilter
                or job.get("industry") == filters_dict.get("industry")
            )
            and (
                jobFilter
                or job.get("job_type") == filters_dict.get("job_type")
            )
        ]
        # pass
