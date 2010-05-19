from logilab.common.testlib import TestCase, unittest_main

from logilab.common.tasksqueue import *

class TaskTC(TestCase):

    def test_eq(self):
        self.failIf(Task('t1') == Task('t2'))
        self.failUnless(Task('t1') == Task('t1'))

    def test_cmp(self):
        self.failUnless(Task('t1', LOW) < Task('t2', MEDIUM))
        self.failIf(Task('t1', LOW) > Task('t2', MEDIUM))
        self.failUnless(Task('t1', HIGH) > Task('t2', MEDIUM))
        self.failIf(Task('t1', HIGH) < Task('t2', MEDIUM))


class PrioritizedTasksQueueTC(TestCase):

    def test_priority(self):
        queue = PrioritizedTasksQueue()
        queue.put(Task('t1'))
        queue.put(Task('t2', MEDIUM))
        queue.put(Task('t3', HIGH))
        queue.put(Task('t4', LOW))
        self.assertEquals(queue.get().id, 't3')
        self.assertEquals(queue.get().id, 't2')
        self.assertEquals(queue.get().id, 't1')
        self.assertEquals(queue.get().id, 't4')

    def test_remove_equivalent(self):
        queue = PrioritizedTasksQueue()
        queue.put(Task('t1'))
        queue.put(Task('t2', MEDIUM))
        queue.put(Task('t1', HIGH))
        queue.put(Task('t3', MEDIUM))
        queue.put(Task('t2', MEDIUM))
        self.assertEquals(queue.qsize(), 3)
        self.assertEquals(queue.get().id, 't1')
        self.assertEquals(queue.get().id, 't2')
        self.assertEquals(queue.get().id, 't3')
        self.assertEquals(queue.qsize(), 0)

    def test_remove(self):
        queue = PrioritizedTasksQueue()
        queue.put(Task('t1'))
        queue.put(Task('t2'))
        queue.put(Task('t3'))
        queue.remove('t2')
        self.assertEquals([t.id for t in queue], ['t3', 't1'])
        self.assertRaises(ValueError, queue.remove, 't4')

if __name__ == '__main__':
    unittest_main()
