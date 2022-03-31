# Original Code:

# class Worker:
#
#     def work(self):
#         print("I'm working!!")
#
#
# class Manager:
#
#     def __init__(self):
#         self.worker = None
#
#     def set_worker(self, worker):
#         assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)
#
#         self.worker = worker
#
#     def manage(self):
#         if self.worker is not None:
#             self.worker.work()
#
# class SuperWorker:
#
#     def work(self):
#         print("I work very hard!!!")
#
#
#
# worker = Worker()
# manager = Manager()
# manager.set_worker(worker)
# manager.manage()
#
# super_worker = SuperWorker()
# try:
#     manager.set_worker(super_worker)
# except AssertionError:
#     print("manager fails to support super_worker....")


# Refactored Code:

from abc import ABC, abstractmethod


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class NormalWorker(AbstractWorker):
    def work(self):
        print("I'm working!!")


class SuperWorker(AbstractWorker):
    def work(self):
        print("I work very hard!!!")


class LazyWorker(AbstractWorker):
    def work(self):
        print('This is so boooring...')


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, AbstractWorker):
            raise AssertionError('`worker` must be of type AbstractWorker')
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


normal_worker = NormalWorker()
manager = Manager()
manager.set_worker(normal_worker)
manager.manage()

super_worker = SuperWorker()

manager.set_worker(super_worker)
manager.manage()


