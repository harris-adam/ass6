import unittest
from random import randint
from hash_table import HashTable
from time import perf_counter_ns

class TestHashTable(unittest.TestCase):

    def test_insert_and_get_simple(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        self.assertEqual(hash_table.get("key1"), "value1")

    def test_remove(self):
        hash_table = HashTable()
        hash_table.insert("key2", "value2")
        self.assertTrue(hash_table.remove("key2"))
        self.assertIsNone(hash_table.get("key2"))

    def test_larger_table(self):
        hash_table = HashTable()
        for i in range(20):
            hash_table.insert(f"key{i}", f"value{i}")
        for i in range(20):
            self.assertEqual(hash_table.get(f"key{i}"), f"value{i}")

    def test_collisions(self):
        hash_table = HashTable(slots=1)  # Force collisions
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        self.assertEqual(hash_table.get("key1"), "value1")
        self.assertEqual(hash_table.get("key2"), "value2")

    def test_update_value(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key1", "value2")
        self.assertEqual(hash_table.get("key1"), "value2")

    def test_nonexistent_key(self):
        hash_table = HashTable()
        self.assertIsNone(hash_table.get("nonexistent"))
        hash_table.insert("nonexistent", "value")
        self.assertEqual(hash_table.get("nonexistent"), "value")

    def test_insert_remove_insert(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.remove("key1")
        hash_table.insert("key1", "value2")
        self.assertEqual(hash_table.get("key1"), "value2")

    def test_very_large_number_of_items(self):
        hash_table = HashTable()
        for i in range(1000):
            hash_table.insert(f"key{i}", f"value{i}")
        for i in range(1000):
            self.assertEqual(hash_table.get(f"key{i}"), f"value{i}")
        self.assertEqual(hash_table.num_items, 1000)
        # try removing half
        for i in range(0, 1000, 2):
            hash_table.remove(f"key{i}")
        for i in range(0, 1000, 2):
            self.assertIsNone(hash_table.get(f"key{i}"))
        for i in range(1, 1000, 2):
            self.assertEqual(hash_table.get(f"key{i}"), f"value{i}")
        self.assertEqual(hash_table.num_items, 500)

    def test_resize(self):
        hash_table = HashTable()
        for i in range(15):
            hash_table.insert(f"key{i}", f"value{i}")
        for i in range(15):
            self.assertEqual(hash_table.get(f"key{i}"), f"value{i}")
        self.assertEqual(hash_table.num_items, 15)
        self.assertGreater(hash_table.slots, 10)  # initial slots was 10

if __name__ == '__main__':
    unittest.main()