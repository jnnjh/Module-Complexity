import unittest

from lru_cache import LruCache

class LruCacheTest(unittest.TestCase):
    def test_zero_limit_is_error(self):
        self.assertRaises(ValueError, lambda: LruCache(limit=0))

    def test_set_then_get(self):
        cache = LruCache(limit=10)

        self.assertIsNone(cache.get("greeting"))
        self.assertIsNone(cache.get("parting"))

        cache.set("greeting", "hello")

        self.assertEqual(cache.get("greeting"), "hello")
        self.assertIsNone(cache.get("parting"))

    def test_limit(self):
        limit = 3
        cache = LruCache(limit=limit)

        keys = ["a", "b", "c", "d", "e"]

        for key in keys:
            cache.set(key, f"{key}-1")

        hits = 0
        for key in keys:
            if cache.get(key) is not None:
                hits += 1

        self.assertEqual(hits, limit)

    def test_eviction_order_just_inserts(self):
        cache = LruCache(limit=2)

        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        self.assertIsNone(cache.get("a"))

    def test_eviction_order_after_gets(self):
        cache = LruCache(limit=2)

        cache.set("a", 1)
        cache.set("b", 2)
        cache.get("a")
        cache.get("b")
        cache.get("a")
        cache.set("c", 3)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("c"), 3)

    def test_update_existing_key(self):
        cache = LruCache(limit=2)
        cache.set("a", 1)
        cache.set("b", 2)
        
        # Update "a" - it should stay in the cache but change value
        cache.set("a", 100)
        self.assertEqual(cache.get("a"), 100)
        
        # Adding "c" should now evict "b", because "a" was recently updated
        cache.set("c", 3)
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 100)

    def test_limit_of_one(self):
        cache = LruCache(limit=1)
        cache.set("a", 1)
        self.assertEqual(cache.get("a"), 1)
        
        cache.set("b", 2) # This should immediately kick out "a"
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("b"), 2)

    def test_get_non_existent_key(self):
        cache = LruCache(limit=5)
        # Testing "None" return for keys never added
        self.assertIsNone(cache.get("missing_key"))

    def test_complex_values(self):
        cache = LruCache(limit=2)
        # Testing that we can store lists or dictionaries, not just strings
        cache.set("list", [1, 2, 3])
        self.assertEqual(cache.get("list"), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
