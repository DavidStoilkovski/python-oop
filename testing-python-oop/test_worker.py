from unittest import TestCase, main


class TestWorker(TestCase):
    name = 'Worker1'
    salary = 2500
    energy = 85
    money = 0

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_instance_attributes_are_set_correct(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)
        self.assertEqual(self.money, self.worker.money)

    def test_worker_energy_is_incremented_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_error_is_raised_when_worker_tries_to_work_with_no_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_workers_money_increased_after_work(self):
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    def test_worker_energy_deacresed_after_work(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f'{self.name} has saved {self.money} money.', self.worker.get_info())


if __name__ == '__main__':
    main()

# Tested code
# class Worker:
#
#   def __init__(self, name, salary, energy):
#     self.name = name
#     self.salary = salary
#     self.energy = energy
#     self.money = 0
#
#   def work(self):
#     if self.energy <= 0:
#         raise Exception('Not enough energy.')
#
#     self.money += self.salary
#     self.energy -= 1
#
#   def rest(self):
#     self.energy += 1
#
#   def get_info(self):
#     return (f'{self.name} has saved {self.money} money.')
