from abc import ABC, abstractmethod
from typing import List
from models import Job

class JobProvider(ABC):
    """
    Base class for all job providers.
    """

    @abstractmethod
    def fetch_jobs(self) -> List[Job]:
        """
        Return a list of jobs from this provider.
        """
        pass