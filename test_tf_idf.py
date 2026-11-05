import unittest

from engine.tf_idf import calculate_document_frequency, calculate_frequency


class TestCalculateDocumentFrequency(unittest.TestCase):
    def test_token_list_documents(self):
        docs = [["kucing", "makan"], ["kucing", "tidur"], ["lainnya"]]
        self.assertEqual(
            calculate_document_frequency(["kucing"], docs), {"kucing": 2}
        )

    def test_string_documents_match_whole_tokens_only(self):
        # Regression: "ai" adalah substring dari "main"/"lain",
        # tapi bukan token utuh, jadi tidak boleh terhitung.
        self.assertEqual(
            calculate_document_frequency(["ai"], ["main", "lain"]), {"ai": 0}
        )
        self.assertEqual(
            calculate_document_frequency(["main"], ["main", "lain"]),
            {"main": 1},
        )

    def test_frequency(self):
        self.assertEqual(
            calculate_frequency(["a", "b", "a"]), {"a": 2, "b": 1}
        )


if __name__ == "__main__":
    unittest.main()
