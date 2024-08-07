import unittest

from LeetCode.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_add(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)

        self.assertEqual(self.linked_list.head.val, 3)
        self.assertEqual(self.linked_list.head.next.val, 2)
        self.assertEqual(self.linked_list.head.next.next.val, 1)

    def test_find(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)

        found_node = self.linked_list.find(2)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.val, 2)

        not_found_node = self.linked_list.find(4)
        self.assertIsNone(not_found_node)

    def test_remove(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)

        # Remove middle element
        self.assertTrue(self.linked_list.remove(2))
        self.assertIsNone(self.linked_list.find(2))
        self.assertEqual(self.linked_list.head.val, 3)
        self.assertEqual(self.linked_list.head.next.val, 1)

        # Remove head element
        self.assertTrue(self.linked_list.remove(3))
        self.assertIsNone(self.linked_list.find(3))
        self.assertEqual(self.linked_list.head.val, 1)

        # Remove non-existent element
        self.assertFalse(self.linked_list.remove(4))

    def test_get_size(self):
        self.assertEqual(self.linked_list.get_size(), 0)
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.assertEqual(self.linked_list.get_size(), 3)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list.get_size(), 2)


if __name__ == "__main__":
    unittest.main()