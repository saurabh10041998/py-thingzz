import datetime
import random
from typing import List


class WorkerDatabase:
    def get_all_workers(self) -> List[str]:
        return []


def get_emergency_workers() -> List[str]:
    return []


def is_available(name: str) -> bool:
    return True


worker_database = WorkerDatabase()
OWNER = 'Saurabh'


def schedule(worker: str, open_time: datetime.datetime):
    ...


def find_available_workers_for_time(open_time: datetime.datetime):
    workers = worker_database.get_all_workers()
    available_workers = [
        worker for worker in workers
        if is_available(worker)
    ]
    if available_workers:
        return available_workers

    # Get the list of emergency workers available
    # and schedule if they are available
    emergency_workers = get_emergency_workers()
    emergency_available_workers = [
        worker for worker in emergency_workers
        if is_available(worker)
    ]
    if emergency_available_workers:
        return emergency_available_workers

    # No one available ? Return owner as available
    # worker, they will find one
    return [OWNER]


def schedule_open_restaurant(
    open_time: datetime.datetime,
    number_of_workers_needed: int
):
    workers = find_available_workers_for_time(open_time)
    # Randomly select X number of workers
    # where X is number of workers needed
    for worker in random.sample(workers, number_of_workers_needed):
        schedule(worker, open_time)


assert find_available_workers_for_time(datetime.datetime.now()) == ['Saurabh']
