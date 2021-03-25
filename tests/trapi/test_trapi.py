import unittest
from biothings_explorer.trapi import TRAPI


class TestTRAPIClass(unittest.TestCase):
    def test_if_url_not_string_raise_exception(self):
        tp = TRAPI()
        with self.assertRaises(Exception):
            tp.url = {"a": "b"}

    def test_url_is_correctly_set(self):
        tp = TRAPI()
        self.assertEqual(tp.url, "https://dev.api.bte.ncats.io/query")
        tp.url = "https://api.bte.ncats.io/query"
        self.assertEqual(tp.url, "https://api.bte.ncats.io/query")

    def test_if_query_graph_not_dict_raise_exception(self):
        tp = TRAPI()
        qg = 1
        with self.assertRaises(Exception):
            tp.query_graph = qg

    def test_query_graph_is_correctly_set(self):
        qg = {"a": "b"}
        tp = TRAPI()
        tp.query_graph = qg
        self.assertEqual(qg, tp.query_graph)

    def test_if_query_graph_is_not_provided_should_raise_exception_when_query(self):
        tp = TRAPI()
        with self.assertRaises(Exception):
            tp.query()

    def test_if_query_graph_is_malformed_should_raise_exception_when_query(self):
        tp = TRAPI()
        tp.query_graph = {"a": "b"}
        with self.assertRaises(Exception):
            tp.query()

    def test_trapi_response_should_be_correctly_returned_if_query_is_right(self):
        tp = TRAPI()
        tp.query_graph = {
            "message": {
                "query_graph": {
                    "nodes": {
                        "n0": {"id": "NCBIGENE:1017", "category": "biolink:Gene"},
                        "n2": {"category": "biolink:Protein"},
                    },
                    "edges": {"e01": {"subject": "n0", "object": "n2"}},
                }
            }
        }
        res = tp.query()
        self.assertIn("message", res)
